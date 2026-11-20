# Defining the work

::: {.callout-note}
Draft brief, tier A. Bullets and references compiled from source discussions 01–08 (2026-11-16). `[LAB n]`, `[RESEARCH]`, `[PLAN]` and `[VERIFY]` mark what is still open. `vault:` paths point into the Obsidian vault.
:::

**Outcome (draft, #5):** the reader can define a workload as a formal workflow with a stated purpose and a picture of working well vs badly, with work items treated as untrusted input. Check: a non-work item and an injected instruction are both refused before any model call.

## The pattern
- Define work at the lowest level it can be defined: "triage an issue" or "make a code change", not "a software developer" (01).
- The path belongs in code, not the model. A workflow "shouldn't be a vibe". The order is heuristic, then decision model, then LLM (01). OWASP calls the same idea Least-Agency (07).
- Framing line: "Could agents follow a workflow, maybe, would it be repeatable and reliable, maybe. don't build your business on maybes." (01)
- Variable content, prescriptive method: "determining what files to change are variable -- determining HOW to choose those files does not change very much with each issue" (01).
- The steps are decided when the process is defined, not at runtime: "the factory is your stated pattern, how can you build before you know what you are building?" (01)
- Dynamic for exploring, declared for relying: "as you need to rely on that workflow -- vibes wont cut it" (04). Declared structure is what makes runs comparable: "otherwise how can you measure a good pass versus a bad pass?" (04)
- Retry, step back and restart from zero are three different moves, and the workflow definition names each one. A changed assumption is a step back, and "something the human decides if that is allowed or not" (01).
- A ready work item needs at least two fields: what is requested, and acceptance criteria. Coach the reader to add more, saying why each earns its place (05, decision). Candidates: target area, and a reproduction for bugs.
- Untrusted becomes trusted: "initial issues are untrusted -- but they work through workflows to become trusted" (06). Typed fields carry policy; prose is data (interview A4.2).
- Make values explicit, lightly: "if you can't define what makes the process your way, then how do you expect a machine to replicate that?" (01). Value-driven development stays out of the weeds and may become its own book.
- You are not starting from zero. Agentic workflows replace parts of a human process, so prioritise by the failures that process already knows (06).

## How I set it up
- The flow: find open issues → work out where each one is → a complete issue moves on, an incomplete one goes to a scrum-master-like refinement agent → plan → implement → PR (01). Describe refinement as underway, at its stage on the day (05: "assume this work is underway"). `[PLAN]` State its actual stage when you draft.
- The issue tracker is the only record of an issue's state. Only deterministic, trusted steps write state, as a typed block in a status comment, and look-alikes from other identities are ignored. No model-facing step holds a tracker credential (06).
- From inferring state to writing it: state guessed from branch names, PR text and labels hid 31 of 49 ready issues (06, "how I decided"). `[VERIFY]` the 31/49 figure at its record.
- `.forgejo/` and `.github/` are protected paths, so CI can run unattended: a gate on the path, not on the run (08).

## How I decided, and what I gave up
- A deterministic readiness check finds that an acceptance section exists, not that it can be checked (05, Claude).
- An issue edited after it was promoted to trusted is a known gap, deferred past MVP: "valid, and we need to protect against that later" (06). Human teams catch the same failure at sprint demo day.
- The factory has no estimate fields yet (cost, duration). Adding them would turn caps into a forecast that can be graded (05).

## What I use it for
- Opener: Clinejection, taken link by link against the factory: an untrusted title, Bash, an arbitrary npm install, a shared cache, shared nightly and production tokens (07). Teach the chain, not the vendor. GitPublic is the fallback (07). `[VERIFY]` the write-ups first (issue 19). Don't use the "~4,000 machines in 8 hours" figure, which isn't in the primary sources.

## Try it (kind)
- The intake refuses a non-work item and an injected instruction before any model call.

## Placeholders
- `[LAB 1]` Path-departure rates, model-held vs code-held control flow: https://github.com/shannonlowder/agent-fleet-factory/issues/1
- `[LAB 3]` Decomposition, a bare prompt vs refinement with org values: https://github.com/shannonlowder/agent-fleet-factory/issues/3
- `[RESEARCH]` Source 09 (the "spec maturity curve"; issue text as an injection vector), source 10 (MAST spec disobedience, 11.8%), source 11 (METR: keep tasks short).

## References
- Anthropic, *Building effective agents*: https://www.anthropic.com/engineering/building-effective-agents. Cite it as vocabulary from an interested party (01).
- OpenAI, *A practical guide to building agents*: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf. Its code-first stance is the foil.
- HumanLayer, *12-Factor Agents*, factor 5: https://github.com/humanlayer/12-factor-agents. Licence question open on issue 19.
- OWASP Top 10 for Agentic Applications 2026 (ASI01, goal hijack): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- Your notes: `vault: ideas/book-sources/discussions/01-anthropic-building-effective-agents`, `vault: ideas/book-sources/discussions/05-google-agents-companion`, `vault: ideas/book-sources/discussions/06-12-factor-agents`, `vault: ideas/book-sources/discussions/07-owasp-agentic-top10`
