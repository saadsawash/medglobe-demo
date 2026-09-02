# MedGlobe brand guide — extracted from `medglobe presentation.ai`

Source: client presentation file (Adobe Illustrator 30.7, Aug 2026).  
Artboard: A3 landscape (420 x 297 mm).  
Thumbnail reference: `medglobe-presentation-thumb.jpg` (same folder).

---

## Logo

| Element | Spec |
|---------|------|
| Mark | Globe grid in **sky blue** with an **orange** curved swoosh |
| Wordmark | **MED** in burnt orange + **GLOBE** in navy blue |
| Lockup | Icon left, wordmark right (horizontal) |
| Clear space | Generous padding around mark; no crowding |

**Usage in deck:** white/light backgrounds; business cards use mark + wordmark top-left, contact block lower area, navy footer bar.

---

## Brand colors (official swatches from presentation)

| Name | HEX | RGB | CMYK | Role |
|------|-----|-----|------|------|
| **Burnt Orange** | `#EC7B25` | 236, 123, 37 | 0, 60, 100, 0 | Accent, "MED", map dots, taglines, CTAs |
| **Sky Blue** | `#3EA9E3` | 62, 169, 227 | 67, 18, 0, 0 | Globe lines, secondary accent, icons |
| **Navy Blue** | `#1E3F8F` | 30, 63, 143 | 100, 85, 0, 20 | "GLOBE", headings, borders, map fill |
| **White** | `#FFFFFF` | 255, 255, 255 | — | Primary background |
| **Black / text** | `#000000` | 0, 0, 0 | — | Body on light surfaces |

Supporting neutrals in file: CMYK gray ramp (K=5 through K=100), plus Turkish-named bases (`Beyaz`, `Siyah`).

---

## Typography

**Primary family: Montserrat** (Medium, SemiBold, Bold embedded in file).

| Level | Weight | Style notes |
|-------|--------|-------------|
| **Main headings** | Bold (700) | Uppercase or title case; navy on light backgrounds |
| **Sub-headings** | SemiBold (600) | Title case; section labels |
| **Body / details** | Medium (400–500) | Sentence case; black or dark gray |

Also embedded: **Social Media Circled** (icon font for contact icons on stationery).

**Tone:** geometric sans, corporate healthcare, high legibility — not decorative or serif.

---

## Layout and composition

- **White space:** airy, minimal; content grouped in clear blocks
- **Stationery:** white card, thin rules, navy **footer band** (~15–20% height) with white type
- **Map motif:** flat navy world map, orange location dots — supports "global presence" messaging
- **Tagline shown:** *"CONNECTING THE WORLD FOR YOUR HEALTH"* (orange, uppercase)
- **Icons:** simple line icons (phone, email, web, location) in brand colors

---

## Imagery direction

- Flat / vector map graphics (not photographic hero clutter)
- Orange pins = markets / offices
- Professional, clinical-corporate — not retail or promotional

---

## Implications for `corp-demo-1` (current demo)

The live corporate demo uses **Athora plum** (`rgb(86 60 73)`) and **cyan accent** (`rgb(42 168 200)`) from the Shopify export — **not** the presentation's orange / navy / sky blue triad.

| Presentation brand | corp-demo-1 today |
|--------------------|-------------------|
| Orange `#EC7B25` | Not used |
| Navy `#1E3F8F` | Not used (plum instead) |
| Sky blue `#3EA9E3` | Partial overlap with cyan accent |
| Montserrat | Inter (Aptos-like substitute) |

**Before recoloring the demo:** confirm with Esra whether the **presentation palette** or the **current plum Athora direction** is the Friday deliverable. Meeting 3 also asked for "more blue" on product pages — navy/sky from this deck may be the intended MedGlobe chrome.

---

## Suggested CSS tokens (if aligning demo to presentation)

```css
:root {
  --mg-orange: #ec7b25;
  --mg-sky: #3ea9e3;
  --mg-navy: #1e3f8f;
  --mg-ink: #000000;
  --mg-paper: #ffffff;
  --mg-font: "Montserrat", "Inter", system-ui, sans-serif;
}
```

---

## File handling

- `medglobe presentation.ai` is **gitignored** (large binary; keep locally or in client asset store).
- Do not embed Montserrat from the `.ai` file on web without a license — use Google Fonts or a purchased webfont.
