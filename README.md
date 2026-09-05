# Vision FC website

A mobile-first static website for Vision Football Club, built from the supplied brand guide and club information.

## Run locally

```bash
python3 -m http.server 4173 --directory .
```

Then open `http://localhost:4173`.

## Included

- Matchday-led homepage
- Responsive navigation with mobile menu
- Club story and timeline
- First-team, Validus FC and U-17/U-15 pathway
- Club leadership cards
- Former-player search interaction
- Accessible reduced-motion fallback
- Authenticated crest asset integrated as a transparent PNG
- External official website CTA pointing to `https://myvisionfc.com`

## Editorial status

The visible facts were prepared from the information supplied by the client from the Vision F.C. Wikipedia article. Before publication, verify the league position, current management, stadium capacity, historical wording, official website and any fixture information directly with the club. No fixtures, ticket prices, testimonials, player statistics or live squad details have been invented.

## Asset note

`assets/crest-transparent.png` was generated from the supplied low-resolution crest reference using GPT Image 2 through the authenticated OpenAI OAuth connection. It is suitable for this prototype presentation, but the club should supply or approve an official vector master before kit, embroidery or formal print production.
