# Perfect Prompt

[![skills.sh](https://skills.sh/b/takeshijuan/perfect-prompt)](https://skills.sh/takeshijuan/perfect-prompt)

`perfect-prompt` is an Agent Skill that turns terse intent into a structured, ready-to-paste prompt for another coding or research agent.

Examples:

```text
/perfect-prompt: review PR#123
/perfect-prompt: implement login system
/perfect-prompt: add a dashboard view
/perfect-prompt: address issue #123
/perfect-prompt: debug staging auth
```

The skill generates the prompt only. It does not execute the requested task.

## Install

From the public repository:

```bash
npx skills add takeshijuan/perfect-prompt
```

Install only this skill if the repository later contains more skills:

```bash
npx skills add takeshijuan/perfect-prompt --skill perfect-prompt
```

Use locally from a clone:

```bash
npx skills add .
```

List discoverable skills:

```bash
npx skills add . --list
```

## skills.sh Listing

The repository is listed on [skills.sh](https://skills.sh/takeshijuan/perfect-prompt) after installs are observed through the `skills` CLI. The root `skills.sh.json` customizes the repo page display and groups this skill under `Prompt Engineering`.

## What It Produces

The generated prompt includes:

- a main `/goal`
- a single fenced `markdown` code block wrapper for easy copying
- role and objective
- context discovery and source-of-truth rules
- context gathered up front by the skill itself: conversation facts, task-relevant user memory (only when a memory system is detected), and resolved external references (issue/PR/URL/file digests embedded in the prompt, with fallback instructions when a reference cannot be resolved)
- constraints and success criteria
- bounded parallel subagent plan with dedicated `/goal` blocks when useful
- model/cost policy
- verification gates
- final reporting format

## Repository Layout

```text
skills.sh.json
skills/perfect-prompt/
├── SKILL.md
├── evals/
│   ├── docs/bug-report.md
│   └── evals.json
└── references/
    ├── agent-orchestration.md
    ├── context-gathering.md
    ├── prompt-structure.md
    └── task-patterns.md
```

## Validate

```bash
python scripts/validate_skill.py
npx skills add . --list
```

After pushing to GitHub:

```bash
npx skills add takeshijuan/perfect-prompt --list
```

## Contributing

Issues and pull requests are welcome. Keep the skill task-agnostic: examples such as issue fixing, PR review, feature work, UI work, debugging, QA, release, and research should all remain first-class.

## License

MIT
