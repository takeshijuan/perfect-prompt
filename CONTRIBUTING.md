# Contributing

Thanks for improving Perfect Prompt.

## Guidelines

- Keep the skill task-agnostic. Do not overfit it to GitHub issues or a single coding agent.
- Keep `SKILL.md` compact and move reusable detail into `references/`.
- Add or update eval cases when changing behavior.
- Run validation before opening a PR:

```bash
python scripts/validate_skill.py
npx skills add . --list
```

## Pull Requests

Include:

- what changed
- why it improves generated prompts
- validation run and result
- any remaining limitations
