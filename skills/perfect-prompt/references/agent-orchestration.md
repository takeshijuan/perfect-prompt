# Agent Orchestration Reference

Use this reference when the generated prompt should tell the receiving agent how to spawn and manage subagents.

## When To Parallelize

Recommend subagents when the task has independent lanes that can proceed without waiting on each other, such as:

- reading separate parts of a large codebase
- comparing implementation against docs or issues
- reviewing API, UI, data, and test impact separately
- investigating logs, config, recent commits, and reproduction paths
- checking security, accessibility, performance, or migration risk

Keep the task single-threaded when:

- it is small enough for one pass
- every step depends on the previous step
- the required context is too intertwined to split cleanly
- subagent overhead would exceed likely benefit

## Fanout Budget

Tell the main agent to spawn only lanes with clear marginal value. A useful default:

- 0 subagents for trivial or highly sequential tasks
- 2-3 subagents for medium tasks with distinct discovery/review lanes
- 4-6 subagents for broad PRs, incidents, or multi-surface features
- More only when each lane has a bounded scope and a clear merge point

## Model And Cost Policy

Include this policy in generated prompts:

- Use cheaper/faster models for narrow searches, file inventory, log scanning, documentation lookup, and straightforward test checks.
- Use stronger models for architecture decisions, security-sensitive analysis, complex debugging, cross-lane synthesis, and final review.
- Stop a subagent early if its lane becomes duplicative or low-signal.
- Prefer one strong synthesis pass over many expensive overlapping agents.

## Subagent Goal Template

Each recommended subagent must receive its own `/goal` block.

```markdown
### Subagent: [lane name]
Recommended model: [cheap/fast or strong, with reason]

/goal
[One independent objective for this subagent.]

Scope:
- Inspect: [files/docs/issues/logs/etc.]
- Produce: [short report, findings, patch recommendation, test list, risk notes]
- Do not: [avoid edits, avoid duplicate lane, avoid speculation]
```

## Synthesis Rule

The main agent should merge returned results by resolving conflicts, deduplicating findings, and choosing the smallest complete execution path. It should not paste subagent reports directly into the final answer unless the user asked for raw reports.
