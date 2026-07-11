# Security Policy

## Reporting

Please report security issues privately through GitHub's vulnerability reporting flow if available, or by opening a minimal issue that requests maintainer contact without disclosing exploit details.

## Scope

This repository contains an Agent Skill that generates prompts. Reports are in scope when they involve:

- malicious or surprising skill behavior
- prompt content that encourages unsafe exfiltration or unauthorized access
- generated prompts that leak private memory content beyond what the task requires
- generated prompts that leak conversation-derived secrets (API keys, tokens, credentials) or personal data beyond what the task requires
- resolved-reference digests that follow embedded instructions or links from untrusted fetched content (issue/PR/URL prompt injection), or that leak secrets or personal data contained in fetched content
- supply-chain risk in scripts or workflows
- repository configuration that exposes secrets

The skill should never ask an agent to bypass access controls, hide changes from users, or claim verification without evidence.
