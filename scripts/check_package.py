#!/usr/bin/env python3
"""Offline integrity checks. Does not evaluate model behavior or legal correctness."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "ROADMAP.md",
    "skills/invention-intake/SKILL.md",
    "skills/invention-intake/agents/openai.yaml",
    "skills/invention-intake/references/evidence.md",
    "skills/invention-intake/references/interview.md",
    "skills/invention-intake/references/outputs.md",
    "skills/invention-intake/references/filing-review.md",
    "templates/invention-disclosure.md", "templates/filing-review.md",
    "examples/synthetic-invention/inputs.md",
    "examples/synthetic-invention/worked-example.md",
    "examples/synthetic-invention/reviewer-notes.md",
    "evaluations/cases.json", "evaluations/rubric.md", "evaluations/STATUS.md",
]

def check():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"Missing required file: {name}")
    if errors:
        return errors
    for path in ROOT.rglob("*.md"):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            destination = target.split("#", 1)[0]
            if not (path.parent / destination).exists():
                errors.append(f"Broken local link in {path.relative_to(ROOT)}: {target}")
    inputs = (ROOT / "examples/synthetic-invention/inputs.md").read_text()
    valid = set()
    source = None
    for line in inputs.splitlines():
        match = re.match(r"## (SRC-\d+) ", line)
        if match:
            source = match.group(1)
        match = re.match(r"### §(\d+)$", line)
        if match and source:
            valid.add((source, match.group(1)))
    output = (ROOT / "examples/synthetic-invention/worked-example.md").read_text()
    citations = re.findall(r"\[(SRC-\d+) §(\d+)\]", output)
    if not citations:
        errors.append("Worked example contains no recognized source citations")
    for citation in citations:
        if citation not in valid:
            errors.append(f"Unknown worked-example source locator: {citation}")
    cases = json.loads((ROOT / "evaluations/cases.json").read_text())
    ids = [case["id"] for case in cases]
    if len(set(ids)) != len(ids) or len(ids) != 5:
        errors.append("Expected five uniquely identified challenge cases")
    for case in cases:
        if not case.get("review_for"):
            errors.append(f"No review criteria for {case['id']}")
        if "input" in case and not (ROOT / case["input"]).is_file():
            errors.append(f"Missing case input for {case['id']}")
        if not (case.get("input") or case.get("input_text")):
            errors.append(f"No input for {case['id']}")
    return errors

if __name__ == "__main__":
    failures = check()
    if failures:
        for failure in failures:
            print("FAIL:", failure)
        raise SystemExit(1)
    print("PASS: package files, local links, five case definitions, and example source locators.")
    print("Scope: structural checks only; no model-performance or legal validation.")
