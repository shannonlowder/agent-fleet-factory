# 0001. One repo for the book and its kind examples

- **Status:** Accepted, 2026-11-15 ([#10](https://github.com/shannonlowder/agent-fleet-factory/issues/10))

## Context

The book and its kind examples could live in two repos or one. The question
was decided by Shannon: *"Let's go with a single repo, until we have a good reason to split them."*

## Decision

One repo for the book and its kind examples, until a split trigger fires.

Why:

- Text and code change in one commit and one PR, so they can't drift.
- One tag is one edition including its demos.
- One CI and one tracker.
- Listings are included straight from `examples/` paths, so no `listings.lock`
  pinning step is needed.

## Consequences (costs accepted)

- Readers who want only code clone everything. Mitigated: build outputs are
  release assets, never committed; sparse checkout of `examples/` works.
- A demo fix ships as a book patch release.
- CI uses path filters so prose-only changes skip kind tests.
- `LICENSING.md` covers `examples/` as Apache-2.0.

Setup work is tracked in the "Single-repo scaffold" milestone, released as
`v0.0.1`.

## Split triggers

Any one of these triggers a split. Split with `git filter-repo`, keeping history.

- A demo needs its own versioned releases because readers depend on it like a library.
- Clone size passes 200 MB or a PR's CI passes 15 minutes.
- A demo needs a different licence.
- A demo gets outside contributors who don't care about the book.
