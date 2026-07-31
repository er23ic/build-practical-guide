# Optional Math SVG Adapter

This internal adapter converts formal math source into one standalone SVG
fragment. It is optional: ordinary `build-practical-guide` execution must work
without Node, MathJax, this adapter, or network access.

## Capability probe

```bash
npm run capability
```

Exit status `0` means MathJax is available. Exit status `3` means the optional
capability is unavailable. An unavailable result does not install anything.

## Render

After the user separately approves installing this optional dependency:

```bash
npm ci
npm run render -- \
  --source '\mathbf{v}=\mathbf{v}_x+\mathbf{v}_y' \
  --id-prefix vector-sum \
  --output /approved/package/images/vector-equation.svg
```

Add `--display` only for display-style layout. Exit statuses:

| Status | Meaning |
|---|---|
| `0` | One standalone SVG with a `viewBox` was written atomically |
| `1` | Invalid formal source, invalid renderer output, or write failure |
| `2` | Invalid command arguments |
| `3` | Optional renderer unavailable |

The adapter rejects MathJax SVG error boxes and output containing anything
other than one SVG root before writing. When several fragments will be composed
into one figure, the caller supplies a unique XML-safe `--id-prefix` for each
fragment; the adapter owns rewriting definition IDs and every internal
`href`, `xlink:href`, and `url(#...)` reference.

The caller owns placement, unique semantic prefix selection, figure-level
accessibility metadata, formula-to-mark mapping, and actual-size Human QA.

Do not commit `node_modules`. Do not run `npm ci` without separate authorization.
