---
name: perfect-prompt
description: Use this skill whenever the user wants a terse request, slash command, vague task, issue or PR instruction, feature idea, UI/dashboard request, debugging task, QA request, release task, research request, planning prompt, or existing prompt rewritten into a stronger ready-to-paste agent prompt. Trigger even when the user only writes shorthand like "review PR#123", "implement login system", "add a dashboard view", "address issue #123", "debug staging auth", or "/perfect-prompt: ...". This skill generates the prompt only; it does not execute the task.
license: MIT
---

# Perfect Prompt

Turn the user's short instruction into one complete agent prompt. The output is the generated prompt itself, not commentary about prompt engineering and not execution of the requested work.

## Core workflow

1. Strip an optional `/perfect-prompt:` prefix and preserve the user's original intent.
2. Classify the task:
   - PR review
   - issue fixing
   - feature implementation
   - UI or dashboard work
   - debugging or incident investigation
   - refactoring
   - test or QA
   - release or deploy
   - research
   - general planning or execution
3. Infer only what is safe. If a value is discoverable by the receiving agent, instruct that agent to discover it instead of inserting a placeholder.
4. Read references only as needed:
   - Use `references/prompt-structure.md` for the baseline prompt contract.
   - Use `references/task-patterns.md` for task-specific sections.
   - Use `references/agent-orchestration.md` whenever the generated prompt should include parallel subagents, `/goal` blocks, or model/cost policy.
5. Write a ready-to-paste prompt that the user can give to another agent.
6. Self-check the generated prompt against the rubric below. Revise before answering if any item fails.

## Generated prompt requirements

The generated prompt must include:

- A main `/goal` block.
- A clear role line, usually starting with `You are ...`.
- Objective, context discovery, source-of-truth rules, constraints, success criteria, execution policy, verification gates, and final response format.
- A bounded parallel-agent strategy when parallel work is useful.
- Dedicated `/goal` text for each subagent lane when subagents are recommended.
- Model/cost policy: cheaper/faster models for narrow discovery and checks; stronger models for architecture, risky edits, synthesis, and final review.
- Explicit instruction to synthesize subagent results rather than blindly concatenate them.
- A final reporting contract that separates completed work, verification, residual risk, and blockers.

## Output format

Return exactly this shape:

```markdown
You are ...

/goal
[one concrete objective for the main agent]

## Context
...

## Operating Rules
...

## Parallel Agent Plan
...

## Execution Plan
...

## Verification
...

## Final Response
...
```

If subagents are not useful, keep `## Parallel Agent Plan` and explain that the task should stay single-threaded because the work is too small, sequential, or context-coupled.

## Rubric

Before responding, verify:

- The prompt is directly usable without additional explanation.
- The task scope is inferred without overfitting to GitHub issues.
- The generated prompt does not execute the task.
- Subagent fanout is useful, bounded, and cost-aware.
- Each recommended subagent has its own dedicated `/goal`.
- The prompt tells the main agent how to synthesize returned results.
- Verification gates are concrete and relevant to the task class.
- The final response contract is explicit.

## Example

Input:

```text
/perfect-prompt: review PR#123
```

Output:

```markdown
You are a senior code review agent...

/goal
Review PR #123 end to end...
```
