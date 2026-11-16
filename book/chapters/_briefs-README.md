# Chapter briefs — what can be drafted now (2026-11-16)

2026-11-16 — One brief per chapter of the ToC v2 (`vault: ideas/book-repo-plan-2026-11` §6b; `docs/toc.md` in `vault: ideas/book-proposal-draft/docs/toc`). Built from the 192 chapter-tagged ideas and decisions in source discussions 01–08 (`vault: ideas/book-sources/discussions/01-anthropic-building-effective-agents` … `vault: ideas/book-sources/discussions/08-github-copilot-coding-agent`), plus `vault: ideas/book-evidence-2026-11`. #book #plan (claude)

**What these are.** Outlines, not prose. Each one follows the chapter template from interview A5.1: *the pattern → how I set it up → how I decided, and what I gave up → what I use it for → try it (kind)*. Text in quotes is Shannon's own words, with the discussion it came from. Anything marked *(Claude)* is Claude's framing: keep it or cut it. Nothing here is book text, and nothing here counts as evidence until it's checked.

**Drafts may be incomplete (Shannon, 2026-11-16).** Leave the gaps in as tagged placeholders:
- `[LAB n]`: waits on a lab result. The book repo issue is n.
- `[RESEARCH]`: needs reading, or a source discussion (09–15b) that hasn't happened yet.
- `[PLAN]`: needs a decision or design from Shannon.
- `[VERIFY]`: a fleet claim that must be checked before the book states it (mostly items on https://github.com/shannonlowder/agent-fleet-factory/issues/22), or a quote that must be checked at its primary source (https://github.com/shannonlowder/agent-fleet-factory/issues/19).

## Readiness

| Tier | Chapters | Meaning |
|---|---|---|
| **A: draft now** | [7](07-defining-the-work/index.qmd), [8](08-knowing-its-done/index.qmd), [10](10-humans-where-they-add-value/index.qmd), [9](09-dividing-the-work/index.qmd), [6](06-identity-credentials-grants/index.qmd), [1](01-from-prompting-to-a-factory/index.qmd) | The argument is settled in Shannon's words. Only the numbers wait on labs or checks. |
| **B: draft with many placeholders** | [3](03-the-model-is-not-the-agent/index.qmd), [12](12-changing-a-running-factory/index.qmd), [11](11-measuring-the-factory/index.qmd) | Rich material, but the key figures are held (the October token data, issue 22) or the story isn't finished yet (the Argo migration). |
| **C: skeleton only** | [4](04-the-harness-beats-the-model/index.qmd), [5](05-the-environment-agents-work-in/index.qmd), [2](02-your-first-fleet-on-kind/index.qmd) | Too little from sources 01–08 (5), or it depends on research not in the vault (4: "Shannon's harness research") or on demo code that doesn't exist yet (2). |

Tagged ideas per chapter: ch7 42, ch11 39, ch8 33, ch10 28, ch9 28, ch12 28, ch6 27, ch3 22, ch4 20, ch1 13, ch5 13, ch2 5. Volume isn't readiness: ch11's ideas are rich, but its numbers are held.

## Inconsistencies found while building these

1. ~~**The bad-guidance lab has no issue.**~~ Filed 2026-11-16 as https://github.com/shannonlowder/agent-fleet-factory/issues/50 (chapters 4 and 11).
2. **Evidence identity rule vs the Forgejo numbers.** The 2026-11-13 decision (discussion 03) says evidence comes only from the Argo factory and its identities: *"stop referring to lthorn or claude when citing evidence for this book"*. `vault: ideas/book-evidence-2026-11` §2 counts "four agent identities" (1,309 / 616 / 558 / 141 merges) without saying whether one of them is `lthorn`. If it is, the agent-share table breaks the rule. `[VERIFY]` before chapters 1 and 11 use it.
3. **Three chapters have no outcome.** Issue 21 says every chapter carries one checkable outcome, but `docs/outcomes.md` covers only chapters 3–11. Chapters 1, 2 and 12 have none. Chapter 2's is implied by the ToC ("one issue in, one reviewed PR out"). `[PLAN]` for 1 and 12.
