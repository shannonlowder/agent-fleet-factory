# Landscape

**Last searched: 2026-11-27.** The search covered web pages, primary pages where they could be read, and arXiv. Items marked † could not be read at the primary page. A claim that something is "not found" means a limited search turned up nothing; it doesn't prove nothing exists. The field moves monthly, so this page is re-searched before each release ([sourcing.md](sourcing.md), rule 6).

## The gap

Today I share a link to one or more articles, sometimes my own posts, but each only ever answers one question. None covers the whole topic, or lets a reader move easily from the first question to the second.

## What's out there

**Foundations: cite them, don't re-teach them**
- *AI Engineering*, Chip Huyen (O'Reilly, 2025). Evals, RAG, agents and inference cost: the general text. One chapter covers agents, including agent failure modes; the book isn't about fleets or delivery.
- *Building effective agents*, Anthropic (2024-12-19), and *How we built our multi-agent research system* (June 2025). The first distinguishes workflows from agents. The second reports large token costs as the price of multi-agent gains. Anthropic's own later note says much of the tooling in the first post has changed ([sourcing.md](sourcing.md), rule 4).
- *A practical guide to building agents*, OpenAI (2025), and *Agents Companion*, Google (February 2025). Orchestration, guardrails and evaluation.
- *12-Factor Agents*, HumanLayer (GitHub, free; content CC BY-SA 4.0, code Apache-2.0). Principles for reliable LLM software. It's the closest to this book in spirit and format (free, written in public), but it isn't a fleet implementation.
- *OWASP Top 10 for Agentic Applications 2026* (December 2025, CC BY-SA 4.0). A risk taxonomy (ASI01–ASI10), not a build guide. Its "Least-Agency" principle and its agent-identity entry (ASI03) are the nearest published statement of our identity chapter's premise.
- DeepLearning.AI *Agentic AI* (Andrew Ng). Patterns: reflection, tools, planning, multi-agent.

**Software delivery with agents: the nearest neighbours**
- ***Building the Agentic Software Factory***, Alex Merced and Benedikt Stemmildt (Packt, 2026-10-29, 338 pp.)†. **The closest match by name and scope.** It takes one developer's AI coding practice to a team-wide "software factory", through context engineering, AI-TDD, "The Complete Harness", "The Autonomy Spectrum", security and team operating models. Read from a retailer's listing and its table of contents only. The listing doesn't mention the authors' production data, agent identity, separation of duties, faked-work detection or reproducible environments.
- *Agentic Engineering: Loops, Harnesses, and the Software Factory*, Addy Osmani (O'Reilly Early Release)†. The harness, multi-agent and long-running workflows, verification and review, and the costs of automation. Read from a retailer page only.
- *Orchestrating AI Agents*, Yohan J. Rodríguez (Leanpub, 286 pp.). Claude Code, Codex, local models and MCP run as one system, through a control plane. Its worked example is Hermes (NousResearch hermes-agent), the same runtime our fleet ran before it moved to Argo workflows. Its contents cover:
  - budgets: per-task-class envelopes, cloud-versus-local break-even, showback;
  - a lease-based work queue;
  - auth isolation (5.6);
  - a worked factory (ch. 13);
  - failure modes and chaos testing (ch. 15).

  The full table of contents and the 14-page sample were read. The sample has no production data.
- *Vibe Coding*, Gene Kim and Steve Yegge (IT Revolution, 2025-10-21, 320 pp.). Working with coding agents, from one developer up to the enterprise. Its chapter on hijacking the reward function names forms of faked work. Its inner, middle and outer developer loops are each organised as Prevent / Detect / Correct. Its "10x" claim is hedged ("at times") and supported by one anecdote. Read: the free excerpt, which includes the full contents.
- *AI-Native Software Delivery*, Durkin, Minick and Gaikwad (O'Reilly with Harness, July 2025). AI added to each stage of an existing CI/CD pipeline, written by staff of a CI/CD vendor. It argues against change-approval boards, with evidence, and gates on SLOs, error budgets and resilience scores. It has no agent identity and no agent approving its own work. The full text was read (free PDF from Harness).
- *Agentic AI for DevOps Engineers*, Trevoir Williams (Packt, July 2026, 270 pp.)†.
  - Its eight chapters cover GenAI in pipelines, governance and enterprise readiness, agentic CI/CD failure triage and PR quality assessment, memory and MCP, and multi-agent incident response with agent observability.
  - A companion repo has C# agents for GitHub Actions.
  - The chapter titles show no agent identity, separation of duties, faked-work detection, token budgets or reproducible environments. Read from a bookseller listing and the code repo, not Packt's page.
- *Agentic Software Development*, Caio Incau (Leanpub). The Claude ecosystem end to end, including chapters on multi-agent orchestration, agentic CI/CD, and security and governance. Single-vendor by design.
- *AI Agents in Action*, 2nd ed., Micheal Lanham (Manning, June 2026, 392 pp.). Agents built as Python application code, on a five-layer model, including a new chapter on "metacognition harnesses". It uses "harness" in a different sense from ours.
- *Agentic Continuous Delivery*, Michael Küsters (Leanpub, unpublished). Continuous-delivery discipline at agent speed, written so a coding agent can use it to review a repo.
- GitHub Copilot coding agent docs. One vendor's version of "the requester can't approve the PR", branch protection and sandboxing.

**Research that bears on our claims**
- *What Does a Harness Buy? Tokens, Mostly*, Liu and Han (arXiv 2610.04433, v2 2026-11-18).
  - **Design:** seven models in three coding-agent scaffolds (Claude Code, mini-SWE-agent, OpenCode), on SWE-bench Verified plus two other benchmarks, with reruns.
  - **Findings:** no scaffold leads across models. Swapping the scaffold changes about as many task outcomes as rerunning the same one, and where the difference can be bounded it is 2–5 points. Cost differences depend on the model.
  - **The paper's "harness":** the scaffold only (system prompt, tools, context handling). It doesn't test CI gates, review or policy around the agent.
  - **How it bears on our chapter 4:** our "harness" means the workflow, gates and controls the agent runs inside. Chapter 4 has to say so, and to report rerun variance next to any harness difference we claim.
- METR, *Time Horizon 1.1* (2026-01-29). The infrastructure change accounts for "a relatively small share" of its trend.
- Reward hacking in code generation: *HackTrace* (arXiv 2610.03055)† and *SpecBench* (arXiv 2605.21384)†. These are detection methods for training, not practitioner guidance.
- Cloud Security Alliance, non-human identity governance for agentic AI (whitepaper, May 2026)†.
- DORA: the latest report is *State of AI-assisted Software Development 2025*. DORA announced on 2026-09-03 that it will not publish a 2026 report, and is moving to qualitative research. We know this from LeadDev's report of the announcement (2026-10-26); the original LinkedIn post wasn't read.

## Where this book is different

| Topic | Elsewhere |
|---|---|
| Patterns that hold across platforms, not one vendor's tools | Merced and Stemmildt claim a tool-independent approach; most other delivery titles are tied to a vendor or one ecosystem |
| Token and cost budgets across many providers, avoiding lock-in | Rodríguez (envelopes, break-even, showback); OWASP ASI02 (tool budgeting) |
| Harness beats model, with a controlled comparison | Liu and Han run a controlled comparison of agent *scaffolds*, and find scaffolds matter about as much as a rerun. No one found has compared the workflow-and-gates harness this book means |
| Reproducible agent runtime environments | Blog posts and tools (sandboxed execution); no book found |
| Per-agent identity and least-privilege credentials, as a build guide | OWASP ASI03 names the risk; Rodríguez covers auth isolation; CSA has a governance whitepaper. No build guide found |
| Catching faked work and tests | *Vibe Coding* names the forms; research papers detect them in training. No measured practice in a working fleet found |
| Formal workflow definitions and measuring interventions | Not found |
| Moving controls from human to machine, measured step by step | *AI-Native Software Delivery* argues against approval boards; Merced and Stemmildt have an "autonomy spectrum". No measured progression found |
| Migrating a running fleet, including one that declined | Not found |
| The author's own production data, good and bad | Not found, apart from Anthropic's research-system numbers |
| Free, open, written in public, runnable on a laptop | *12-Factor Agents* is free and public, but isn't a running fleet |

The honest version: the patterns are known in pieces, and two books published in the last month now use the "software factory" framing. What nobody else appears to offer is the whole path, in one fleet, with the numbers, including the weeks it went wrong.

## What I'd point someone to today

Before this book, I'd suggest:
- Huyen for foundations;
- Anthropic's *Building effective agents* for the difference between workflows and agents;
- *12-Factor Agents* for principles;
- the OWASP agentic top 10 for threats;
- *Vibe Coding* for working alongside a coding agent.

After that, readers are on their own for everything in the table above.
