TEST RUN for iac/argo-workflows issue 212; written by Claude, not Shannon. Close this PR without merging.
- A book section draft now opens its review on GitHub through the github adapter.
- The adapter never pushes main and never writes under book/.assists.
- Scope is declared per source (book = shannon/personal), not inferred from a path.
