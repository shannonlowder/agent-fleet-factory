## GitHub Adapter Test Run

I'm here to help.

A book section draft now opens its review on GitHub through the github adapter.

The adapter never pushes main and never writes under book/.assists.

Scope is declared per source (book = shannon/personal), not inferred from a path.

Let's dig into this.

This isn't a bug, it's a config issue. The change to how the adapter handles scope came from a specific need: we want to control exactly what files and directories are considered when processing a draft, without relying on inferred paths. Our setup has a well-defined source scope — in this case, `book = shannon/personal` — that tells the system where to focus.

There is a better way.

Let me show you how this works. Let's start with the configuration:

```yaml
source: book
target:
  adapter: github
  scope: 
    root: shannon/personal
```

This setup declares that the source is `book` and uses the `github` adapter to handle the workflow. The key part, the scope, specifically defines `root: shannon/personal`. This means the operations won't just happen arbitrarily in the repository; they will be constrained to this path.

For instance, if the tool tries to create a file like `book/section.md`, it respects the declared scope and ensures that only `shannon/personal/book/section.md` or subdirectories within that are handled. The adapter never writes under `book/.assists`.

Simple, right?

The reason we're not pushing directly to main is important too — that's a safety mechanism. Our workflow ensures a review process happens before changes make it into the live branch. The PR that gets opened through this system isn't auto-merged; it’s a request for review.

What makes this significant is the intent behind it: to ensure clean, controlled, and predictable interaction with source repositories. We are explicitly avoiding assumptions based on directory structures.

The adapter is designed to be precise about scope, not opportunistic. So even if something else might happen in similar systems, we're keeping things tight here.

There's a better way — when you're dealing with an automated workflow that has to operate reliably and safely across multiple contexts, setting explicit boundaries like this prevents unintended side effects.

Let me make one quick point: there’s no version of this code in the repository yet. The `[[NEEDS SHANNON: what is missing]]` would be information about whether this configuration works, any potential edge cases, or real-world usage examples for a system like this. The current setup relies on specific assumptions around how Databricks and GitHub interact — particularly when orchestrating automated reviews.

If you've run into this problem differently, or found a better approach, I'd love to hear about it. As always, I'm here to help.
