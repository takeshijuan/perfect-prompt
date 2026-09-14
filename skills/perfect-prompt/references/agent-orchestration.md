# Agent Orchestration Reference

Use only when the user requests parallel work or independent subtasks would materially help and the receiving environment permits delegation. Prompt generation itself does not authorize spawning agents or changing model settings.

## Independent work

Describe each useful lane's objective, scope, expected result, and edit authority. Choose a small bound based on the actual independent work and available runtime capacity; do not prescribe agent counts by task size alone. Keep coupled or sequential work together and avoid overlapping ownership of the same edits.

A lane can be a sentence, for example: "Review the API changes for authorization regressions; return actionable findings and evidence without editing files."

Use `/goal` syntax only when requested or known to be supported and helpful. Do not require a separate goal block for every lane.

## Models and stopping

Preserve the user's model and budget choices. Include model-routing advice only when requested or useful for a known multi-model runtime; use only models actually available there. Otherwise let the receiving environment keep its defaults.

Bound repeated review or repair by the task's scope and evidence needs. Stop duplicate work and stop another pass when it cannot add useful evidence. A suggested parallel plan must not expand permission to send messages, publish, deploy, or modify external state.

## Synthesis

The main agent resolves conflicting evidence, deduplicates findings, and integrates authorized changes. Ask it for a coherent result, not concatenated subagent reports.
