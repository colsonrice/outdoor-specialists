# Outdoor Specialists — Squatchcraft demo

A responsive website concept for Outdoor Specialists, LLC, Zionsville, Indiana.

Demo: https://www.squatchcraft.com/outdoor-specialists/

## Run locally

```sh
python3 -m http.server 4182 --directory site
python3 scripts/qa.py
```

The finished static website is in `site/`. Edit `site/index.html`, `site/assets/site.css`, and `site/assets/site.js` directly. Fonts and photos are self-hosted. The gallery supports category filters, native modal focus management, Escape, and arrow-key navigation. Reduced-motion preferences are respected.

## Original assets

`scripts/collect_assets.py` records assets from all five original pages, seven attachment pages, and the original theme stylesheet. `source/asset-manifest.json` records source URLs, dimensions, checksums, and failed legacy assets. The local `assets/originals/` directory preserves recovered originals. There are 14 full-size photographs/banners: 11 project photos and three old promotional banners. The photo gallery includes all 11 project photographs; the three banners with embedded promotional text are archived and have optimized copies in the assets folder. Original logo and thumbnail/theme assets are archived locally. Seven broken original references (five theme decorations and two dynamic sidebar thumbnail endpoints) are recorded in the manifest; the corresponding full-size sidebar photos were recovered successfully.

Photos were optimized to WebP with EXIF orientation corrected; original content was not synthesized. The new OS typographic mark is a demo identity treatment, with the original logo preserved locally.

## Demo boundaries

This concept is marked `noindex, nofollow`. Consultation buttons explicitly open the business's existing contact page. There is no new form backend, no invented contact information or testimonials, and no submissions are made during QA. The existing outdoorspecialists.net website remains untouched.

## Publishing

GitHub Pages publishes `site/` using `.github/workflows/deploy.yml`. The account's existing Squatchcraft custom domain supplies the demo's project URL.
