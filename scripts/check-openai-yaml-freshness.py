#!/usr/bin/env python3
"""Check whether each skill's agents/openai.yaml is still in sync with its SKILL.md.

lazynote's openai.yaml files are hand-curated, not generated from SKILL.md —
they restate a skill's purpose in a shorter, Codex-facing form
(display_name/short_description/default_prompt). Nothing mechanically keeps
them in sync, so an edit to SKILL.md can silently leave openai.yaml stale.

This script does not regenerate anything. It records a hash of each skill's
SKILL.md at the moment openai.yaml was last reviewed, and reports any skill
where SKILL.md has changed since — a prompt to re-read openai.yaml and update
it by hand if the skill's purpose actually shifted.

Usage:
  scripts/check-openai-yaml-freshness.py            # report stale skills; exit 1 if any
  scripts/check-openai-yaml-freshness.py --update    # after reviewing, record current hashes
"""
import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
MANIFEST_PATH = REPO_ROOT / "scripts" / "openai-yaml-freshness.json"


def skill_md_hash(skill_dir: Path) -> str:
    content = (skill_dir / "SKILL.md").read_bytes()
    return hashlib.sha256(content).hexdigest()


def skills_with_openai_yaml() -> list[Path]:
    return sorted(
        d for d in SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "agents" / "openai.yaml").exists()
    )


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {}


def save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def main() -> int:
    update = "--update" in sys.argv
    manifest = load_manifest()
    skill_dirs = skills_with_openai_yaml()

    if update:
        for skill_dir in skill_dirs:
            manifest[skill_dir.name] = skill_md_hash(skill_dir)
        save_manifest(manifest)
        print(f"Recorded current SKILL.md hashes for {len(skill_dirs)} skill(s).")
        return 0

    stale = []
    unrecorded = []
    for skill_dir in skill_dirs:
        current = skill_md_hash(skill_dir)
        recorded = manifest.get(skill_dir.name)
        if recorded is None:
            unrecorded.append(skill_dir.name)
        elif recorded != current:
            stale.append(skill_dir.name)

    if not stale and not unrecorded:
        print(f"All {len(skill_dirs)} openai.yaml file(s) are in sync with their SKILL.md.")
        return 0

    if stale:
        print("SKILL.md changed since openai.yaml was last reviewed:")
        for name in stale:
            print(f"  - {name}")
    if unrecorded:
        print("No recorded hash yet (never checked):")
        for name in unrecorded:
            print(f"  - {name}")
    print(
        "\nReview skills/<name>/agents/openai.yaml against the current SKILL.md. "
        "If it still accurately describes the skill, run with --update to record "
        "the current hash. If not, edit openai.yaml first, then --update."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
