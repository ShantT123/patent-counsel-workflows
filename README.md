# Patent Counsel Workflows

**Open-source AI workflows for developing invention disclosures and preparing patent filing reviews.**

Created by **Shant Tchakerian**. Version **0.1.0 — preview**.

The first skill, **Invention Intake**, helps patent counsel turn incomplete inventor materials into a source-linked disclosure, prioritized follow-up questions, technical diagrams, and a filing-review packet. It preserves unresolved questions instead of filling them with invented technical facts.

## Try it in five minutes

1. Download and extract this repository.
2. Open an AI assistant that supports reading local Markdown files. Give it `skills/invention-intake/SKILL.md` and the referenced files in that skill's `references/` folder. Tool support and installation methods vary by assistant.
3. Attach `examples/synthetic-invention/inputs.md` and use this prompt:

> Follow the Invention Intake skill. Use only the attached fictional sources. Prepare a disclosure, prioritized follow-up questions, proposed diagrams, and a filing-review packet. Preserve source references, contradictions, and unknowns. Do not search externally. Produce Markdown in this chat.

4. Compare the response with `examples/synthetic-invention/worked-example.md` and score it using `evaluations/rubric.md`.

For Codex, copy the **entire** `skills/invention-intake` folder into your configured skills directory (commonly `~/.codex/skills/`), make it available in your session, and invoke `$invention-intake`. If it is not discovered, use the file-based prompt above. This preview has been structurally checked; cross-assistant installation and model behavior have not been independently validated.

## What you get

- A reusable skill with evidence and uncertainty rules.
- Templates for disclosures and filing-review packets.
- A complete fictional input/output example with a review commentary.
- Five challenge cases and a human evaluation rubric.
- A standard-library package checker; no API key or paid service is required to inspect the project.

## Scope

This release supports **pre-filing invention development and counsel review**. It can use supplied strategy, glossary, portfolio, rubric, and cost information; those inputs are optional. Missing inputs limit the corresponding analysis.

It does not conduct an exhaustive prior-art search, determine inventorship, give a legal clearance opinion, manage deadlines, draft a complete patent application, or file anything. It does not supply a confidentiality or privilege guarantee. Outputs need review by appropriately qualified counsel before professional reliance.

## Core design choices

**Evidence stays visible.** Technical assertions use stable source locators. Facts, inventor statements, inferences, proposed alternatives, and unknowns remain distinguishable.

**Technical depth precedes scoring.** The workflow asks what changes in the system, how the mechanism works, which steps are essential, and what supports the claimed advantage.

**Business assessment stays separate from legal judgment.** A strategic score is not a patentability determination. An unknown is not a zero. Similar abstracts identify review candidates, not established claim coverage.

**No hidden integrations.** The skill has no bundled external connectors, telemetry, or network code. The AI assistant hosting it may process data remotely; its privacy, retention, tools, and sharing settings still matter.

## Repository map

| Path | Purpose |
| --- | --- |
| `skills/invention-intake/` | Installable skill, supporting references, and Codex UI metadata |
| `templates/` | Optional editable Markdown output forms |
| `examples/synthetic-invention/` | Fictional source materials, worked output, and reviewer commentary |
| `evaluations/` | Challenge cases, scoring rubric, and evaluation status |
| `scripts/check_package.py` | Checks package integrity and worked-example source references |

The installable skill is self-contained. Repository-level templates and evaluations are optional companions.

## Validation

Run `python3 scripts/check_package.py` from the repository root. This checks packaging and example references, **not legal correctness or model performance**. See [evaluation status](evaluations/STATUS.md) for what has and has not been measured.

## Contributing and roadmap

See [publishing instructions](PUBLISHING.md) to upload this package. See [CONTRIBUTING.md](CONTRIBUTING.md) for useful contributions and [ROADMAP.md](ROADMAP.md) for proposed next steps. Synthetic edge cases, documented model failures, and improvements grounded in patent practice are particularly welcome.

## License and attribution

MIT licensed; see [LICENSE](LICENSE). Attribution does not imply endorsement. The fictional examples are intentionally created for this project and do not represent an actual company, invention, patentability conclusion, or client matter.
