# Sourcing and citation rules

These rules cover every quote, figure and claim the book takes from someone else's work. They exist because sources move: pages are edited, PDFs are re-exported, and vendor tools change every few months.

## 1. Cite only what was read at the primary source

- A quote or figure goes into a chapter only after it has been read on the original page or in the original PDF. A summary, a search snippet or a model-written digest is not enough.
- Quotes are exact. A paraphrase never goes inside quotation marks.
- Where the book could read only part of a source (a sample, a preview, a table of contents), the citation says so. It makes no claim about the rest of the work.

## 2. Date every claim, and mark how it is known

Each claim taken from a source carries:

- **the date it was read** (YYYY-MM-DD);
- **how it is known:**
  - *official*: the source states it;
  - *observed*: we saw it ourselves, in our fleet or by running the tool;
  - *inferred*: our reading of the evidence, labelled as such.

Our own numbers are dated in the same way. A later edition can then show whether a number improved or got worse, and by how much. We don't assume progress is linear.

## 3. Pin the version of living documents

- **For a PDF,** record the SHA-256 of the file that was read (`shasum -a 256 file.pdf`), along with its URL and the date the file says it was created. A re-export with a new date or hash is a new version, and the citation is re-checked against it.
- **For a web page,** record the URL and the date read. If the page shows a "last updated" date, record that too.

## 4. Vendor posts the vendor itself calls outdated

Some vendor posts carry a later note saying their tooling has changed. One example is Anthropic's *Building effective agents* (2024-12-19), which now points readers to a newer post.

- Cite these posts for their **concepts and vocabulary**, with their publication date and a mention of the vendor's own note.
- Never cite their tool names, APIs or settings as current practice. Where the book needs the current mechanism, it cites the newer primary source, or our own observed behaviour.

## 5. Third-party licences

The book's prose is CC BY 4.0 (see [LICENSING.md](../LICENSING.md)). Material under a ShareAlike licence cannot be adapted into it without the result inheriting that licence.

- **Short quotation with attribution** is allowed from any source: the author, title, link and licence, kept to what the argument needs.
- **CC BY-SA content is quoted, never adapted.** We don't copy its images or diagrams, rewrite its passages into our prose, or reuse its structure as our own. For example, *12-Factor Agents* (HumanLayer) is CC BY-SA 4.0 for its content and images and Apache-2.0 for its code, per its README's License section.
- The same rule applies to the *OWASP Top 10 for Agentic Applications 2026* (CC BY-SA 4.0, stated on p. 1). The book uses its ASI numbers as references ("OWASP ASI03") in its own words, and quotes only short passages.
- **Apache-2.0 or MIT code** from another project can appear in a listing only with its copyright notice and licence named beside it.
- **Paid books** are quoted briefly for commentary and never reproduced. Until we have bought a book, we cite only what its sample or preview shows.

## 6. Re-check before each release

- Re-run the landscape search ([landscape.md](landscape.md)) before each release, because the field moves monthly. Update the page's "last searched" date.
- Re-check any cited figure whose source has a newer edition (for example a yearly survey).
