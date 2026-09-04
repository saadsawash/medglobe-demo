# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parent
catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))

EN = {
    "roll-on": {
        "lead": "A natural underarm roll-on that helps delay odor-causing bacteria without blocking pores or stopping sweat. Nourishes skin and supports comfort during sensitive periods.",
        "points": ["No aluminum or parabens", "No synthetic fragrance", "Pure botanical oils", "Does not clog pores"],
    },
    "brow-oil": {
        "lead": "A supportive brow oil for hair that sheds during treatment — formulated to help brows return healthier with pure botanical oils and no chemical additives.",
        "points": ["Supports regrowth", "Pure plant oils", "No synthetic additives", "Gentle daily use"],
    },
    "nail-oil": {
        "lead": "A nail care serum for cuticles and nails that dry, crack, or yellow during chemotherapy. Pure botanical oils — no heavy chemical additives.",
        "points": ["Cuticle comfort", "Brittle nail support", "Pure botanical oils", "No synthetic fragrance"],
    },
    "castile": {
        "lead": "A traditional olive-oil castile soap for face and body when skin becomes sensitive during treatment. Non-toxic, biodegradable, free of fragrance and essence.",
        "points": ["Face & body safe", "Olive-oil tradition", "Biodegradable", "No fragrance or essence"],
    },
    "spray": {
        "lead": "A refreshing body mist for sensitive skin during and after treatment. Can stand in for deodorant while calming skin and helping limit bacterial buildup.",
        "points": ["Sensitive-skin mist", "Deodorant alternative", "Calming feel", "No synthetic fragrance"],
    },
    "protective-balm": {
        "lead": "A protective balm prepared for skin that is more open to fungal issues during radiotherapy, when immunity is strained. Pure botanical oils — no chemical additives.",
        "points": ["Radiotherapy-period care", "Protective barrier story", "Pure botanical oils", "No synthetic additives"],
    },
    "scalp-oil": {
        "lead": "A scalp oil that feeds hair roots during shedding so new growth has a calmer place to begin. Helps with scalp discomfort using only pure botanical oils.",
        "points": ["Root nourishment", "Supports new growth", "Scalp comfort", "Pure plant oils"],
    },
    "lotion": {
        "lead": "A moisturizing body lotion for skin that becomes sensitive and dry during or after treatment. Pure botanical oils with a gentle protective feel.",
        "points": ["Daily moisture", "Sensitive & dry skin", "Pure botanical oils", "No synthetic additives"],
    },
    "repair-balm": {
        "lead": "An intensive balm to support skin that is wounded, burned, or damaged during radiotherapy. Cell-renewing botanical oils — no chemical additives.",
        "points": ["Repair-focused", "Radiotherapy support", "Cell-renewing story", "Pure botanical oils"],
    },
    "body-oil": {
        "lead": "A rich botanical oil blend to nourish and moisturize skin that dries and sensitizes during or after treatment.",
        "points": ["Deep nourishment", "Dry, sensitive skin", "Pure plant oils", "No synthetic fragrance"],
    },
    "hair-serum": {
        "lead": "A strengthening hair serum for strands returning after treatment — clarifies the scalp, balances sebum, and supports stronger, healthier growth.",
        "points": ["Strength & growth support", "Scalp balance", "Pure botanical oils", "No chemical additives"],
    },
}

CAT_LABEL = {"body": "Body care", "hair": "Hair, brow & nail", "balm": "Balms"}

for p in catalog:
    p.update(EN[p["id"]])
    p["category_label"] = CAT_LABEL[p["category"]]

(root / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")

css_extra = """

/* Yeshim line: catalog grid + product accent (deep green, MedGlobe chrome stays) */
:root {
  --yeshim-green: 20 84 68;
}

.top__logo--radika {
  height: 2.35rem;
  width: auto;
}
@media (min-width: 480px) {
  .top__logo--radika { height: 2.55rem; }
}

.stage__frame--product {
  aspect-ratio: 1 / 1;
  background: rgb(var(--mg-muted));
}
.stage__frame--product .stage__img {
  object-fit: contain;
  object-position: center;
  padding: 8%;
  transform: none;
}
.stage__frame--product .stage__img.is-active {
  transform: none;
}

.catalog {
  display: grid;
  gap: 0.75rem;
  margin: 0;
  padding: 0;
  list-style: none;
}
@media (min-width: 560px) {
  .catalog { grid-template-columns: 1fr 1fr; }
}
.catalog a {
  display: grid;
  grid-template-rows: auto 1fr;
  text-decoration: none;
  border: 1px solid var(--line);
  border-radius: 0.65rem;
  overflow: hidden;
  background: rgb(var(--mg-muted));
  transition: border-color 0.3s var(--ease), transform 0.3s var(--ease), background 0.3s var(--ease);
}
.catalog a:hover {
  border-color: rgb(var(--mg-navy) / 22%);
  background: rgb(var(--mg-paper));
  transform: translateY(-2px);
}
.catalog__img {
  aspect-ratio: 1;
  background: #fff;
  display: grid;
  place-items: center;
}
.catalog__img img {
  width: 78%;
  height: 78%;
  object-fit: contain;
}
.catalog__meta {
  padding: 0.85rem 0.9rem 1rem;
}
.catalog__cat {
  display: block;
  margin-bottom: 0.3rem;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgb(var(--yeshim-green));
}
.catalog__name {
  display: block;
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: -0.015em;
  color: rgb(var(--mg-navy));
  margin-bottom: 0.25rem;
}
.catalog__focus {
  font-size: 0.8rem;
  color: var(--mute);
}

.pillars {
  display: grid;
  gap: 0.65rem;
  margin: 0 0 0.25rem;
  padding: 0;
  list-style: none;
}
.pillars li {
  padding: 0.95rem 1rem;
  border-radius: 0.65rem;
  background: rgb(var(--mg-muted));
  border: 1px solid var(--line);
}
.pillars strong {
  display: block;
  margin-bottom: 0.25rem;
  color: rgb(var(--mg-navy));
  font-size: 0.95rem;
}
.pillars span { color: var(--mute); font-size: 0.9rem; }

.points {
  display: grid;
  gap: 0.45rem;
  margin: 0 0 1.25rem;
  padding: 0;
  list-style: none;
}
.points li {
  display: flex;
  gap: 0.65rem;
  align-items: baseline;
  padding: 0.55rem 0;
  border-bottom: 1px solid var(--line);
  color: rgb(var(--mg-navy));
  font-size: 0.92rem;
  font-weight: 500;
}
.points li::before {
  content: "";
  flex: none;
  width: 0.4rem;
  height: 0.4rem;
  margin-top: 0.35rem;
  border-radius: 999px;
  background: rgb(var(--yeshim-green));
}

.back-line {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: 1rem;
  font-size: 0.78rem;
  font-weight: 600;
  color: rgb(var(--mg-navy) / 62%);
  text-decoration: none;
}
.back-line:hover { color: rgb(var(--mg-navy)); }

.related {
  display: grid;
  gap: 0.55rem;
  margin: 0;
  padding: 0;
  list-style: none;
}
.related a {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.55rem;
  border-radius: 0.55rem;
  border: 1px solid var(--line);
  text-decoration: none;
  background: rgb(var(--mg-muted));
  transition: background 0.25s var(--ease), border-color 0.25s var(--ease);
}
.related a:hover {
  background: #fff;
  border-color: rgb(var(--mg-navy) / 22%);
}
.related img {
  width: 3.2rem;
  height: 3.2rem;
  object-fit: contain;
  background: #fff;
  border-radius: 0.4rem;
}
.related strong {
  display: block;
  font-size: 0.88rem;
  color: rgb(var(--mg-navy));
}
.related span {
  font-size: 0.74rem;
  color: var(--mute);
}

.source-note {
  margin-top: 0.85rem;
  font-size: 0.68rem;
  color: var(--mute);
}
.source-note a { color: rgb(var(--mg-sky)); }
"""

css_path = root / "styles.css"
css = css_path.read_text(encoding="utf-8")
if "/* Yeshim line:" not in css:
    css_path.write_text(css + css_extra, encoding="utf-8")

(root / "motion.js").write_text(
    """(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const bar = document.querySelector(".progress i");
  const captions = window.MG_STAGE_CAPTIONS || {};
  const stageImgs = [...document.querySelectorAll(".stage__img")];
  const dots = [...document.querySelectorAll(".stage__dots [data-dot]")];
  const line = document.querySelector("[data-stage-line]");
  const chapters = [...document.querySelectorAll("[data-chapter]")];

  let active = chapters[0]?.dataset.chapter || "intro";
  const setStage = (key) => {
    if (!key || key === active) return;
    active = key;
    stageImgs.forEach((img) => {
      img.classList.toggle("is-active", img.dataset.stage === key);
    });
    dots.forEach((dot) => {
      dot.classList.toggle("is-on", dot.dataset.dot === key);
    });
    if (line && captions[key]) {
      line.classList.add("is-swap");
      window.setTimeout(() => {
        line.textContent = captions[key];
        line.classList.remove("is-swap");
      }, 180);
    }
  };

  const onScroll = () => {
    if (bar) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const p = max > 0 ? (window.scrollY / max) * 100 : 0;
      bar.style.width = `${p}%`;
    }
    const mid = window.innerHeight * 0.42;
    let current = active;
    chapters.forEach((chapter) => {
      const r = chapter.getBoundingClientRect();
      if (r.top <= mid && r.bottom >= mid) current = chapter.dataset.chapter;
    });
    setStage(current);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const form = document.querySelector(".block--ask form");
  if (form) form.addEventListener("submit", (e) => e.preventDefault());

  const animateCount = (el) => {
    const target = Number(el.dataset.count || 0);
    if (!target) return;
    if (reduce) {
      el.textContent = String(target);
      return;
    }
    const start = performance.now();
    const dur = 1100;
    const tick = (now) => {
      const t = Math.min(1, (now - start) / dur);
      const eased = 1 - Math.pow(1 - t, 3);
      el.textContent = String(Math.round(target * eased));
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  if (reduce) {
    document.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
    document.querySelectorAll("[data-count]").forEach(animateCount);
    return;
  }

  requestAnimationFrame(() => {
    document.querySelectorAll(".block--hero [data-in]").forEach((el) => el.classList.add("is-on"));
    document.querySelectorAll(".block--hero [data-count]").forEach(animateCount);
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.2, rootMargin: "0px 0px -8% 0px" }
  );
  document.querySelectorAll("[data-scene]").forEach((scene) => io.observe(scene));
})();
""",
    encoding="utf-8",
)


def header(active_label, nav_html, brand_href="#top", logo_prefix=""):
    return f"""  <header class="top">
    <a class="top__brand" href="{brand_href}" aria-label="MedGlobe product library — {active_label}">
      <img class="top__logo top__logo--mg" src="{logo_prefix}images/medglobe/logo.webp" width="148" height="68" alt="MedGlobe">
      <span class="top__rule" aria-hidden="true"></span>
      <img class="top__logo top__logo--radika" src="{logo_prefix}images/brand/radika-logo.svg" width="160" height="42" alt="Radika Aromatherapy">
    </a>
    <nav class="top__nav" aria-label="Page">
{nav_html}
    </nav>
  </header>"""


featured = ["scalp-oil", "protective-balm", "brow-oil", "lotion", "repair-balm", "hair-serum"]
by_id = {p["id"]: p for p in catalog}

line_nav = """      <a href="#story">Story</a>
      <a href="#care">Care areas</a>
      <a href="#range">The range</a>
      <a href="#contact">Ask MedGlobe</a>"""

catalog_items = []
for p in catalog:
    catalog_items.append(
        f"""          <li data-in>
            <a href="products/{p['id']}.html">
              <div class="catalog__img"><img src="{p['image']}" width="400" height="400" alt="{p['title_en']}" loading="lazy"></div>
              <div class="catalog__meta">
                <span class="catalog__cat">{p['category_label']}</span>
                <span class="catalog__name">{p['title_en']}</span>
                <span class="catalog__focus">{p['focus']}</span>
              </div>
            </a>
          </li>"""
    )

stage_imgs = []
dots = []
keys = ["intro", "story", "care", "range", "contact"]
for i, key in enumerate(keys):
    img_key = featured[min(i, len(featured) - 1)]
    p = by_id[img_key]
    active = " is-active" if i == 0 else ""
    on = ' class="is-on"' if i == 0 else ""
    extra = ' fetchpriority="high"' if i == 0 else ' loading="lazy"'
    stage_imgs.append(
        f'        <img class="stage__img{active}" data-stage="{key}" src="{p["image"]}" width="1080" height="1080" alt="{p["title_en"]}"{extra}>'
    )
    dots.append(f'        <span data-dot="{key}"{on}></span>')

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MedGlobe — Yeshim Serisi | Radika Aromatherapy</title>
  <meta name="description" content="Yeshim Serisi in the MedGlobe product library — natural care for skin that becomes sensitive during intensive treatment. Story first, not a checkout.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

{header("Yeshim Serisi", line_nav)}

  <div class="progress" aria-hidden="true"><i></i></div>

  <main id="top" class="layout">
    <aside class="stage-pin" aria-label="Product stage">
    <div class="stage">
      <div class="stage__glow" aria-hidden="true"></div>
      <div class="stage__frame stage__frame--product">
{chr(10).join(stage_imgs)}
      </div>
      <div class="stage__caption">
        <p class="stage__model">Yeshim Serisi</p>
        <p class="stage__line" data-stage-line>Care for sensitive treatment periods</p>
      </div>
      <div class="stage__dots" aria-hidden="true">
{chr(10).join(dots)}
      </div>
    </div>
    </aside>

    <div class="story">
      <section class="block block--hero" data-chapter="intro">
        <p class="eyebrow" data-in>MedGlobe product library</p>
        <h1 data-in data-delay="1">Care when skin<br>becomes the story.</h1>
        <p class="lead" data-in data-delay="2">Yeshim Serisi is Radika Aromatherapy—s natural line for skin that becomes sensitive during intensive care — scalp, brows, nails, and dryness-prone body. Selected by MedGlobe for careful market entry. Not a checkout.</p>
        <div class="hero__actions" data-in data-delay="3">
          <a class="btn btn--fill" href="#range">See the range</a>
          <a class="btn btn--ghost" href="#story">Read the story</a>
        </div>
        <ul class="hero__stats" data-in data-delay="4">
          <li><strong data-count="11">0</strong><span>products in this library</span></li>
          <li><strong>3</strong><span>care areas</span></li>
          <li><strong>100%</strong><span>botanical oils — no synthetic perfume</span></li>
        </ul>
      </section>

      <section class="block" id="story" data-chapter="story" data-scene>
        <p class="eyebrow" data-in>The line</p>
        <h2 data-in data-delay="1">Named for a person. Built for a period of care.</h2>
        <p data-in data-delay="2">Yeshim is not a lifestyle fragrance line. It is a focused collection for skin that has become fragile during intensive treatment — formulated with pure plant oils, without synthetic perfume, parabens, or heavy chemical additives.</p>
        <p data-in data-delay="3">MedGlobe brings this story to markets where clinical trust and human care matter more than a shop grid. The <a href="https://radikaaromaterapi.com/onkoloji" rel="noopener">Radika oncology collection</a> is the source catalog; this library is how we present it.</p>
        <ul class="pillars" data-in data-delay="4">
          <li><strong>Hospital-period care</strong><span>Formulated for scalp, brows, nails, and body when treatment changes the skin.</span></li>
          <li><strong>Pure botanicals</strong><span>Plant oils only — no synthetic perfume, parabens, or heavy additives.</span></li>
          <li><strong>One MedGlobe shell</strong><span>Same product-page skeleton as Steadi-3 Plus. Content and accent change; the institution does not.</span></li>
        </ul>
      </section>

      <section class="block" id="care" data-chapter="care" data-scene>
        <p class="eyebrow" data-in>Care areas</p>
        <h2 data-in data-delay="1">Where the line works</h2>
        <p data-in data-delay="2">Grouped the way clinicians and caregivers ask — not as a perfume aisle.</p>
        <div class="chips">
          <article data-in data-delay="0"><strong>Hair, brow &amp; nail</strong><p>Scalp oil, brow oil, nail oil, strengthening hair serum.</p></article>
          <article data-in data-delay="1"><strong>Balms</strong><p>Protective balm and intensive repair balm for strained skin.</p></article>
          <article data-in data-delay="2"><strong>Body care</strong><p>Castile soap, lotion, body oil, spray, and underarm roll-on.</p></article>
          <article data-in data-delay="3"><strong>~12 SKUs max</strong><p>MedGlobe will not import the full Radika catalog — this library stays selective.</p></article>
        </div>
      </section>

      <section class="block" id="range" data-chapter="range" data-scene>
        <p class="eyebrow" data-in>The range</p>
        <h2 data-in data-delay="1">Eleven products. One story.</h2>
        <p data-in data-delay="2">Open any SKU for the same left-stage / right-story layout — product first, ask MedGlobe at the end.</p>
        <ul class="catalog">
{chr(10).join(catalog_items)}
        </ul>
        <p class="source-note" data-in>Source catalog: <a href="https://radikaaromaterapi.com/onkoloji" rel="noopener">radikaaromaterapi.com/onkoloji</a>. Packaging photography from Radika; MedGlobe label direction TBD.</p>
      </section>

      <section class="block block--ask" id="contact" data-chapter="contact" data-scene>
        <p class="eyebrow" data-in>Inquire</p>
        <h2 data-in data-delay="1">Ask MedGlobe about Yeshim</h2>
        <p data-in data-delay="2">For clinicians, clinics, and partners. Tell us your market and whether you need the full selective range or a starter set.</p>
        <form action="#" method="post" data-in data-delay="3">
          <label>
            <span>Name</span>
            <input type="text" name="name" autocomplete="name" required>
          </label>
          <label>
            <span>Email</span>
            <input type="email" name="email" autocomplete="email" required>
          </label>
          <label>
            <span>Message</span>
            <textarea name="message" required></textarea>
          </label>
          <button type="submit">Send inquiry</button>
        </form>
        <p class="fine" data-in data-delay="4">Distributed by MedGlobe. Manufactured by Radika Aromatherapy. Cart and checkout are off in this library preview.</p>
      </section>
    </div>
  </main>

  <footer class="end">MedGlobe product library — Yeshim Serisi — Radika Aromatherapy</footer>

  <script>
    window.MG_STAGE_CAPTIONS = {{
      intro: "Care for sensitive treatment periods",
      story: "Named for a person. Built for care.",
      care: "Scalp, brows, nails, body",
      range: "Eleven products in one shell",
      contact: "Ask MedGlobe about Yeshim",
    }};
  </script>
  <script src="motion.js" defer></script>
</body>
</html>
"""
(root / "index.html").write_text(index_html, encoding="utf-8")

prod_dir = root / "products"
prod_dir.mkdir(exist_ok=True)

for p in catalog:
    others = [o for o in catalog if o["id"] != p["id"] and o["category"] == p["category"]][:3]
    if len(others) < 3:
        others = [o for o in catalog if o["id"] != p["id"]][:3]
    related = []
    for o in others:
        related.append(
            f"""            <li data-in>
              <a href="{o['id']}.html">
                <img src="../{o['image']}" width="80" height="80" alt="" loading="lazy">
                <span><strong>{o['title_en']}</strong><span>{o['focus']}</span></span>
              </a>
            </li>"""
        )
    points = "\n".join(
        f'          <li data-in data-delay="{i}">{pt}</li>' for i, pt in enumerate(p["points"])
    )
    nav = """      <a href="#about">About</a>
      <a href="#formula">Formula</a>
      <a href="#range">In the line</a>
      <a href="#contact">Ask MedGlobe</a>"""
    stage = f"""      <div class="stage__frame stage__frame--product">
        <img class="stage__img is-active" data-stage="intro" src="../{p['image']}" width="1080" height="1080" alt="{p['title_en']}" fetchpriority="high">
        <img class="stage__img" data-stage="about" src="../{p['image']}" width="1080" height="1080" alt="{p['title_en']}" loading="lazy">
        <img class="stage__img" data-stage="formula" src="../{p['image']}" width="1080" height="1080" alt="{p['title_en']}" loading="lazy">
        <img class="stage__img" data-stage="range" src="../{p['image']}" width="1080" height="1080" alt="{p['title_en']}" loading="lazy">
        <img class="stage__img" data-stage="contact" src="../{p['image']}" width="1080" height="1080" alt="{p['title_en']}" loading="lazy">
      </div>"""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>MedGlobe — {p['title_en']} | Yeshim Serisi</title>
  <meta name="description" content="{p['lead']}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>

{header(p['title_en'], nav, brand_href="../index.html", logo_prefix="../")}

  <div class="progress" aria-hidden="true"><i></i></div>

  <main id="top" class="layout">
    <aside class="stage-pin" aria-label="Product stage">
    <div class="stage">
      <div class="stage__glow" aria-hidden="true"></div>
{stage}
      <div class="stage__caption">
        <p class="stage__model">{p['title_en']}</p>
        <p class="stage__line" data-stage-line>{p['focus']}</p>
      </div>
      <div class="stage__dots" aria-hidden="true">
        <span data-dot="intro" class="is-on"></span>
        <span data-dot="about"></span>
        <span data-dot="formula"></span>
        <span data-dot="range"></span>
        <span data-dot="contact"></span>
      </div>
    </div>
    </aside>

    <div class="story">
      <section class="block block--hero" data-chapter="intro">
        <a class="back-line" href="../index.html">? Yeshim Serisi</a>
        <p class="eyebrow" data-in>{p['category_label']} — Yeshim Serisi</p>
        <h1 data-in data-delay="1">{p['title_en']}</h1>
        <p class="lead" data-in data-delay="2">{p['lead']}</p>
        <div class="hero__actions" data-in data-delay="3">
          <a class="btn btn--fill" href="#about">About this product</a>
          <a class="btn btn--ghost" href="#contact">Ask MedGlobe</a>
        </div>
      </section>

      <section class="block" id="about" data-chapter="about" data-scene>
        <p class="eyebrow" data-in>About</p>
        <h2 data-in data-delay="1">What it is for</h2>
        <p data-in data-delay="2">{p['lead']}</p>
        <p data-in data-delay="3">Turkish name: <strong>{p['title_tr']}</strong>. Part of Radika—s Yeshim Serisi for oncology-adjacent skin care — presented here in MedGlobe—s product library.</p>
      </section>

      <section class="block" id="formula" data-chapter="formula" data-scene>
        <p class="eyebrow" data-in>Formula stance</p>
        <h2 data-in data-delay="1">Pure oils. No perfume aisle.</h2>
        <ul class="points">
{points}
        </ul>
        <p data-in>Source description (TR): {p['desc_tr']}</p>
        <p class="source-note" data-in>Source: <a href="{p['source']}" rel="noopener">radikaaromaterapi.com</a></p>
      </section>

      <section class="block" id="range" data-chapter="range" data-scene>
        <p class="eyebrow" data-in>In the line</p>
        <h2 data-in data-delay="1">Related in Yeshim</h2>
        <ul class="related">
{chr(10).join(related)}
        </ul>
        <p class="source-note" data-in><a href="../index.html">View full Yeshim range</a></p>
      </section>

      <section class="block block--ask" id="contact" data-chapter="contact" data-scene>
        <p class="eyebrow" data-in>Inquire</p>
        <h2 data-in data-delay="1">Ask MedGlobe about {p['title_en']}</h2>
        <p data-in data-delay="2">Tell us your role and market. This is a library preview — cart is off.</p>
        <form action="#" method="post" data-in data-delay="3">
          <label>
            <span>Name</span>
            <input type="text" name="name" autocomplete="name" required>
          </label>
          <label>
            <span>Email</span>
            <input type="email" name="email" autocomplete="email" required>
          </label>
          <label>
            <span>Message</span>
            <textarea name="message" required></textarea>
          </label>
          <button type="submit">Send inquiry</button>
        </form>
        <p class="fine" data-in data-delay="4">Distributed by MedGlobe. Manufactured by Radika Aromatherapy.</p>
      </section>
    </div>
  </main>

  <footer class="end">MedGlobe — Yeshim — {p['title_en']}</footer>

  <script>
    window.MG_STAGE_CAPTIONS = {{
      intro: "{p['focus']}",
      about: "What it is for",
      formula: "Pure botanical oils",
      range: "Related in the line",
      contact: "Ask MedGlobe",
    }};
  </script>
  <script src="../motion.js" defer></script>
</body>
</html>
"""
    (prod_dir / f"{p['id']}.html").write_text(html, encoding="utf-8")

print(f"Wrote index + {len(catalog)} PDPs")
