# didimacveg.github.io

Personal site of Diego Macías Vega: <https://didimacveg.github.io>

Static HTML, no build step, no tracking, no frameworks.

| Path | What it is |
|---|---|
| `index.html` | The whole site (styles and the hero animation are inline) |
| `assets/raan/` | RAAN screenshots and a copy of its technical report |
| `cv/` | One-page CV: sources (`cv.en.json`, `cv.es.json`), build script and the two PDFs |
| `docs/` | Working notes in Spanish: decisions, steps for Diego, LinkedIn texts, review of public repositories |

```bash
make cv      # rebuild both CV PDFs (first run creates .venv and installs reportlab)
```

```bash
make check   # fail if an em dash or the old orange accent comes back
```

```bash
make serve   # preview at http://localhost:8000
```

The hero animation draws hydrogen orbitals with particles sampled from the exact
wavefunctions, |ψ(n,l,m)|², by rejection sampling. No libraries.

Built with an AI coding assistant (Claude Code); content and claims are Diego's responsibility.
