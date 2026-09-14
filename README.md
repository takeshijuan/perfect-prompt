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

Use the skill when asking to create or improve a prompt, explicitly by name or in natural language (for example, "make this better for an agent: fix the staging auth bug"). Bare requests such as "review PR#123" and "implement login system" should run as ordinary tasks rather than activate this skill.

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

The output is one fenced `markdown` code block containing the requested outcome, relevant context and constraints, and observable completion criteria. Small tasks can stay short; larger tasks can use headings and supporting detail.

The skill resolves supplied references read-only, carries relevant conversation or configured-memory facts when needed, and preserves privacy and untrusted-content boundaries. It records unavailable references instead of inventing their contents.

Role declarations, `/goal` blocks, execution plans, model choices, and parallel-agent plans are optional. Include them when requested or useful in the target environment, without adding permissions or mandatory workflow overhead.

## Repository Layout

```text
skills.sh.json
skills/perfect-prompt/
├── SKILL.md
├── evals/
│   ├── docs/
│   │   ├── bug-report.md
│   │   ├── bug-report-with-secret.md
│   │   ├── feature-request.md
│   │   ├── fenced-issue.md
│   │   ├── injected-issue.md
│   │   ├── memory-injected/
│   │   │   ├── AGENTS.md
│   │   │   └── MEMORY.md
│   │   └── memory-project/
│   │       ├── AGENTS.md
│   │       └── MEMORY.md
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
python scripts/test_validate_skill.py
npx skills add . --list
```

`evals/evals.json` contains prompt-generation scenarios and positive/negative skill-selection cases. The validator checks their structure; it does not execute model-based behavioral evaluations. Use a fresh agent context to evaluate selection from the skill description and generated outputs against the scenarios.

After pushing to GitHub:

```bash
npx skills add takeshijuan/perfect-prompt --list
```

## Contributing

Issues and pull requests are welcome. Keep the skill task-agnostic: examples such as issue fixing, PR review, feature work, UI work, debugging, QA, release, and research should all remain first-class.

## License

MIT
