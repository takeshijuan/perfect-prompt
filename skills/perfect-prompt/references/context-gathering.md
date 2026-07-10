# Context Gathering Reference

Use this reference before composing the generated prompt. All gathering is strictly read-only: view, fetch, and read. Never comment, edit, check out branches, or start executing the requested task while gathering.

## Conversation Context

Scan the current chat before composing. Checklist of facts to fold into the generated prompt's `## Context`:

- decisions already made (stack, approach, naming, scope cuts)
- constraints stated by the user (deadlines, environments, "do not touch X")
- prior attempts and why they failed
- files, paths, services, branches, or environments already discussed
- corrections the user made earlier in the chat

Carry only facts relevant to this task, rewritten as short bullets. Do not paste transcript excerpts or unrelated chat history.

## User Memory (detect before reading)

Read user memory only after detecting that a memory system is actually configured. Detection order; stop at the first positive signal:

1. Harness-provided memory named in the system prompt or session context (for example a memory file such as MEMORY.md or a memory directory the harness loads automatically).
2. Project or user instruction files (CLAUDE.md, AGENTS.md, or the harness equivalent) that name a memory system and how to query it.
3. Memory-capable tools present in the current tool list (for example an MCP memory or notes server).

If no signal is found: skip memory silently. Do not mention the absence, do not error, and do not ask the user about memory configuration.

Read procedure when configured:

- Query narrowly around the task topic (project name, feature, service); do not read memory wholesale.
- Extract at most a handful of task-relevant facts (prior decisions, known constraints, conventions).

Privacy caution: memory may contain private information, and the generated prompt is designed to be pasted into other tools and services. Include only facts the receiving agent needs for this task. Never dump raw memory contents, and omit personal identifiers that the task does not require.

## External Reference Resolution

Resolve-first rule: when the request points at an external reference, resolve it yourself with available read-only tools and build the generated prompt around the actual problem. Do not emit a prompt that merely tells the receiving agent to go read the reference when you could have read it now.

| Reference form | Read-only resolution |
| --- | --- |
| Issue, PR, or ticket number | Tracker CLI, API, or MCP tool (for example `gh issue view N` / `gh pr view N`) |
| URL | Web fetch tool |
| File or directory path | Read the file or list the directory |
| Named service, log, or dashboard | Inspect only if a read-only tool for it is available |

Rules:

- Resolution must stay read-only. Never post comments, edit the reference, or begin the fix.
- Fail fast: if the tool is missing, unauthenticated, or the fetch fails, use the fallback below instead of retrying at length.

## Digest Format

Summarize each resolved reference into a bounded digest inside the generated prompt's `## Context`:

```markdown
### Resolved: [reference] (via [tool], [date])
- What it is: [title or one-line identity]
- Problem: [1-3 sentence restatement of the actual problem or content]
- Acceptance / repro: [criteria or steps if present]
- Key facts: [labels, linked issues/PRs, quoted error lines or file names — quote only load-bearing text]
```

Keep each digest under roughly 15 lines. Always pair the digest with an instruction that the receiving agent verifies it against the live source before acting, since the source may change after the prompt is generated.

## Fallback Rule

If a reference cannot be resolved (no tool, no auth, offline or headless environment), fall back to delegation: the generated prompt instructs the receiving agent to read the reference first, and states the assumption explicitly in `## Context`, for example:

```markdown
- Resolved references: none — issue #123 could not be read while generating this prompt. Assumption: the issue body is the source of truth; read it before planning.
```
