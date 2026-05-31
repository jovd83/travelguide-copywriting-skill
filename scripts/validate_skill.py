#!/usr/bin/env python3
"""Repository-local validation for travelguide-copywriter.

Structural checks for the AgentSkill portfolio standard: required files,
SKILL.md frontmatter, README badges and sections, a Keep-a-Changelog entry,
and eval metadata validity. Unicode is intentionally allowed in text files,
since travel copy legitimately uses international place names (e.g. Tromso)
and emoji section markers.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SKILL_NAME = "travelguide-copywriter"

ROOT_REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "agents/openai.yaml",
    "evals/evals.json",
    ".github/workflows/validate.yml",
]


def fail(message: str) -> str:
    return f"FAIL: {message}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_top_level_frontmatter(content: str) -> tuple[dict[str, str], str | None]:
    """Parse only top-level (unindented) key: value pairs from the frontmatter."""
    if not content.startswith("---\n"):
        return {}, "SKILL.md must start with YAML frontmatter"
    try:
        _, frontmatter, _ = content.split("---\n", 2)
    except ValueError:
        return {}, "SKILL.md frontmatter must be closed with ---"

    values: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values, None


def validate_skill_md(root: Path) -> list[str]:
    errors: list[str] = []
    content = read_text(root / "SKILL.md")
    frontmatter, parse_error = parse_top_level_frontmatter(content)
    if parse_error:
        return [fail(parse_error)]

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if name != SKILL_NAME:
        errors.append(fail(f"SKILL.md frontmatter name must be {SKILL_NAME}"))
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append(fail("SKILL.md frontmatter name must be lowercase hyphen-case"))
    if not description:
        errors.append(fail("SKILL.md frontmatter description is required"))
    if len(description) > 1024:
        errors.append(fail("SKILL.md frontmatter description must be <= 1024 characters"))

    # Portfolio standard: traceability metadata.
    for fragment, message in [
        ("author: jovd83", "SKILL.md must declare metadata.author: jovd83"),
        ('version: "1.0.0"', "SKILL.md must declare metadata.version 1.0.0"),
    ]:
        if fragment not in content:
            errors.append(fail(message))
    return errors


def validate_openai_yaml(root: Path) -> list[str]:
    errors: list[str] = []
    content = read_text(root / "agents/openai.yaml")
    for fragment in ["display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation: true"]:
        if fragment not in content:
            errors.append(fail(f"agents/openai.yaml missing expected fragment: {fragment}"))
    return errors


def validate_release_docs(root: Path) -> list[str]:
    errors: list[str] = []
    readme = read_text(root / "README.md")
    changelog = read_text(root / "CHANGELOG.md")

    for fragment, message in [
        ("version-1.0.0-blue", "README.md must show the 1.0.0 version badge"),
        ("status-stable", "README.md must show the status badge"),
        ("category-", "README.md must show the category badge"),
        ("validation-GitHub%20Actions", "README.md must include the validation badge"),
        ("license-MIT-green", "README.md must include the MIT license badge"),
        ("Buy%20Me%20a%20Coffee", "README.md must include the Buy Me a Coffee badge"),
        ("## What This Skill Does", "README.md must describe what the skill does"),
        ("## When To Use It", "README.md must describe when to use the skill"),
        ("## What This Skill Does Not Do", "README.md must describe what the skill does not do"),
        ("## Install", "README.md must include an Install section"),
        ("## Usage", "README.md must include a Usage section"),
        ("npx skills add jovd83/travelguide-copywriting-skill", "README.md must include npx skills install guidance"),
    ]:
        if fragment not in readme:
            errors.append(fail(message))

    if "## 1.0.0 - 2026-05-31" not in changelog:
        errors.append(fail("CHANGELOG.md must include the 1.0.0 release entry"))
    return errors


def validate_evals(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(read_text(root / "evals/evals.json"))
    except json.JSONDecodeError as exc:
        return [fail(f"evals/evals.json is invalid JSON: {exc}")]

    if payload.get("skill_name") != SKILL_NAME:
        errors.append(fail(f"evals/evals.json skill_name must be {SKILL_NAME}"))

    evals = payload.get("evals")
    if not isinstance(evals, list) or len(evals) < 3:
        return errors + [fail("evals/evals.json must contain at least 3 eval cases")]

    ids = set()
    for index, case in enumerate(evals, start=1):
        if not isinstance(case, dict):
            errors.append(fail(f"eval case {index} must be an object"))
            continue
        case_id = case.get("id")
        if case_id in ids:
            errors.append(fail(f"duplicate eval id: {case_id}"))
        ids.add(case_id)
        for key in ["prompt", "expected_output"]:
            if not case.get(key):
                errors.append(fail(f"eval id {case_id} missing key: {key}"))
    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    for relative_file in ROOT_REQUIRED_FILES:
        if not (root / relative_file).exists():
            errors.append(fail(f"missing required file: {relative_file}"))

    if not errors:
        errors.extend(validate_skill_md(root))
        errors.extend(validate_openai_yaml(root))
        errors.extend(validate_release_docs(root))
        errors.extend(validate_evals(root))

    if errors:
        for error in errors:
            print(error)
        return 1

    print("Skill repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
