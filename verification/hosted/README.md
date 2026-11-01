# Hosted mathematics verification

The [hosted review workflow](../../.github/workflows/hosted-review.yml) compares the mathematics in every tracked Markdown page with the actual, commit-pinned GitHub rendering at widths of 1440 and 760 pixels. It saves source inventories, rendered MathML comparisons, page HTML, screenshots and a bound `hosted-report.json`.

The [text contract](math-contract.json) adds exact accessible-text checks for the README's headline threshold and two finite guarantees, tied to their source-expression hashes. These source-derived expectations supplement the structural checks for every formula; they are not captured host evidence and introduce no renderer exceptions.

The browser uses a fresh anonymous context and normal certificate verification. Dependencies, browser binaries and capture output live in the runner's temporary directory, outside the source checkout. The job grants `contents: read`, disables checkout credential persistence, uses no repository secrets and does not modify the repository. Failed comparisons fail the job; the artifact step also preserves available evidence from failed captures.

## Revisions and evidence

The workflow runs when a pull request targeting `main` opens or its head changes. Runs for the same head SHA share a concurrency group, which cancels overlapping attempts. The checkout and capture both use `github.event.pull_request.head.sha`. GitHub documents that a pull-request event's default SHA represents its merge branch, which is why the explicit head SHA is necessary here: [workflow event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request).

There is no page filter: the collector inventories every tracked `.md`, `.markdown`, `.mdown`, `.mkdn` and `.mkd` file, case insensitively, from that exact Git commit. The output directory must be empty at the start of each capture. The workflow bounds dependency installation to eight minutes, capture to fifteen minutes and the complete job to twenty-five minutes.

The report records both its observed commit and Git tree. A pull-request report can describe the integrated content only when the complete checked tree equals the observed merged tree and the actual merge relationship is recorded. A different tree requires a new capture. Do not substitute a moving branch URL or a synthetic pull-request merge SHA for the recorded source pin.

Download the complete artifact directory before its retention period expires. Preserve `hosted-report.json` together with its referenced files and verify their recorded hashes. The artifact archive digest and the report file's SHA-256 are different identifiers. Inspect the screenshots separately: an automated structure pass does not establish visual correctness, mathematical correctness, originality or future rendering behavior.

## Verifier provenance

The two utilities are unchanged copies of the canonical hosted-math verifier, version **0.10.0**. Their recorded SHA-256 values are:

```text
49182eaf354e86f685a4976814d672de5d7329a2d9e42f62a5227e2bc07c2d18  capture_hosted_math.cjs
edbc2d72af94e96b78166d74b66fcea150134f2f3ebaaea121e9057768e1dbfe  check_rendered_math.py
```

The collector's only adjacent runtime dependency is `check_rendered_math.py`, which uses the Python standard library. Its external runtime dependencies are Node.js, Git, Python, Playwright **1.56.1** and MathJax **3.2.1**. This provenance record adds no license terms and does not change the repository's existing license.

The workflow pins each official action to the full commit identified by its release:

| Action | Verified release |
| --- | --- |
| `actions/checkout` | [v6.0.2](https://github.com/actions/checkout/releases/tag/v6.0.2) |
| `actions/setup-node` | [v6.5.0](https://github.com/actions/setup-node/releases/tag/v6.5.0) |
| `actions/setup-python` | [v6.3.0](https://github.com/actions/setup-python/releases/tag/v6.3.0) |
| `actions/upload-artifact` | [v7.0.2](https://github.com/actions/upload-artifact/releases/tag/v7.0.2) |

Chromium and its operating-system dependencies are installed with Playwright's documented [`install --with-deps chromium` CI command](https://playwright.dev/docs/ci).

## Local invocation

Use an approved environment with Node.js 18 or newer, Python 3.10 or newer, Git and the pinned dependencies above. Set `NODE_PATH` to the temporary dependency directory's `node_modules`, and set `PLAYWRIGHT_BROWSERS_PATH` to the corresponding temporary browser cache. Run:

```bash
node verification/hosted/capture_hosted_math.cjs \
  --root /absolute/path/to/checkout \
  --repository owner/name \
  --revision FULL_40_CHARACTER_COMMIT \
  --contract verification/hosted/math-contract.json \
  --output /absolute/path/to/new-empty-evidence-directory
```

Exit code 0 means the automated checks passed for the recorded source and page scope. Exit code 1 records failed or blocked verification; exit code 2 indicates invalid invocation or setup. Retain failed evidence and investigate its reported cause before attempting a new capture in a different empty directory.
