# Vision FC Website Refactor Implementation Plan

> **For Hermes:** Execute this plan against the existing static site without replacing verified production behaviour.

**Goal:** Convert the Vision FC single-file static site into a maintainable static frontend while preserving the live brand, content, SEO/GEO foundation, animations, intro-film replay modal, favicon set and footer downloads.

**Architecture:** Keep a dependency-free static deployment suitable for Vercel. `index.html` owns semantic structure and metadata; `styles.css` owns all visual tokens, responsive rules and motion; `app.js` owns navigation, player search, reveal behaviour and intro-film modal state; `assets/players.json` owns the supplied former-player list. A small Python smoke-test suite verifies source references and release-critical assets.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, JSON, Python `unittest`, Vercel static deployment.

---

## Scope

- Extract inline CSS into `styles.css`.
- Extract inline JavaScript into `app.js`.
- Move former-player fixture data into `assets/players.json`.
- Add explicit loading/error handling for player data without changing the user-facing search contract.
- Add deterministic static smoke checks under `tests/`.
- Add architecture and run instructions.
- Preserve current URLs, assets, metadata, structured data, animations and modal behaviour.

## Non-goals

- No framework migration.
- No database, authentication or CMS.
- No new club facts or live match data.
- No replacement of the supplied/generated crest or venue asset.
- No change to the canonical production domain.

## Release gates

1. `python -m unittest discover -s tests -v` passes.
2. `node --check app.js` passes.
3. `git diff --check` passes.
4. Local HTTP serving returns the homepage, assets, brand guide and intro video.
5. 320px and 390px screenshots show no horizontal overflow or clipped primary CTA.
6. Live HTML references external CSS/JS and contains no inline runtime `<style>` or `<script>` blocks.
7. The live footer contains the brand guide and intro-film links; the header does not contain the brand-guide link.
8. GitHub remote head and the Vercel canonical URL are verified after deployment.

## Ordered tasks

### Task 1: Extract presentation layer

Create `styles.css` from the existing inline `<style>` block and replace it with a stylesheet link in `index.html`. Preserve tokens, breakpoints, motion rules and reduced-motion overrides exactly before making any optional cleanup.

### Task 2: Extract behaviour layer

Create `app.js` from the existing inline script. Replace the hard-coded player array with a fetch from `assets/players.json`; render a clear fallback if the request fails. Preserve menu, reveal, search, modal close and focus behaviour.

### Task 3: Add data and architecture documentation

Create `assets/players.json` and `docs/architecture.md` describing ownership boundaries, verified asset routes, editorial caveats and the static deployment model.

### Task 4: Add smoke tests

Create `tests/test_site.py` using Python standard library only. Test required files, HTML references, metadata markers, footer/header placement, JSON validity and asset existence. Do not use a browser or external network in unit tests.

### Task 5: Verify and release

Run all release gates, render narrow mobile screenshots, inspect console/network errors if available, commit the refactor, push `main`, deploy to Vercel and read back the canonical HTML and representative assets.
