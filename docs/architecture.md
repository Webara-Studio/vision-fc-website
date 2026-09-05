# Vision FC static-site architecture

## Runtime ownership

- `index.html` — semantic page structure, metadata, JSON-LD, accessible labels and stable links.
- `styles.css` — design tokens, layout, responsive breakpoints, motion and reduced-motion rules.
- `app.js` — mobile navigation, former-player loading/search, reveal observer and intro-film modal state.
- `assets/players.json` — supplied former-player fixture data only; not a live squad feed.
- `assets/` — approved/generated crest variants, favicon derivatives, venue image and social preview.
- `brand-guide.pdf` — downloadable brand reference.
- `intro-video.mp4` — 12-second silent visual master, user-controlled in the footer modal.
- `tests/test_site.py` — dependency-free source and asset smoke checks.

## Data boundary

The site is intentionally static. `assets/players.json` is fetched with `cache: 'no-store'` and rendered only as an editorial former-player list. It is not authentication, a database, a live fixture feed or a current squad source. The page's club facts remain subject to the editorial disclaimer in the footer.

## Deployment

The repository is deployed as a static Vercel project under `webara1`. The canonical URL is `https://vision-fc-site.vercel.app/`. Local development uses `python3 -m http.server 4173 --directory .`.

## Refactor rules

- Keep the entry point and public asset URLs stable.
- Prefer external files over inline CSS/JavaScript.
- Keep all UI state in `app.js`; do not introduce inline event handlers.
- Preserve `prefers-reduced-motion` behaviour.
- Verify local HTTP serving, mobile screenshots, JavaScript syntax, asset metadata and live deployment independently.
- Replace fixture data with a typed API only as a separate, explicitly scoped project requiring an authoritative source and backend contract.
