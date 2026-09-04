# -*- coding: utf-8 -*-
from pathlib import Path
import re

yeshim_css = Path("product-demo-yeshim/styles.css")
css = yeshim_css.read_text(encoding="utf-8")
if ".stage__btn" not in css:
    nav = """
.stage__nav {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 0.55rem;
  pointer-events: none;
}
.stage__btn {
  pointer-events: auto;
  width: 2.2rem;
  height: 2.2rem;
  border: 0;
  border-radius: 999px;
  background: rgb(var(--mg-paper) / 88%);
  color: rgb(var(--mg-navy));
  font-size: 1.45rem;
  line-height: 1;
  cursor: pointer;
  box-shadow: 0 6px 18px rgb(var(--mg-navy) / 12%);
  transition: background 0.2s var(--ease), transform 0.2s var(--ease);
}
.stage__btn:hover,
.stage__btn:focus-visible {
  background: #fff;
  outline: none;
  transform: scale(1.05);
}
"""
    css = css.replace(
        "box-shadow: inset 0 0 0 1px rgb(var(--mg-navy) / 6%);\n}",
        "box-shadow: inset 0 0 0 1px rgb(var(--mg-navy) / 6%);\n  touch-action: pan-y;\n}\n" + nav,
        1,
    )
    css = re.sub(
        r"\.stage__dots \{.*?\n\.stage__dots span\.is-on \{[^}]+\}",
        """\.stage__dots {
  display: flex;
  gap: 0.4rem;
  margin-top: 0.95rem;
  padding: 0 0.15rem;
}
.stage__dots button,
.stage__dots span {
  width: 0.4rem;
  height: 0.4rem;
  padding: 0;
  border: 0;
  border-radius: 999px;
  background: rgb(var(--mg-navy) / 16%);
  cursor: pointer;
  transition: width 0.35s var(--ease), background 0.35s var(--ease);
}
.stage__dots button:hover,
.stage__dots button:focus-visible {
  background: rgb(var(--mg-navy) / 42%);
  outline: none;
}
.stage__dots button.is-on,
.stage__dots span.is-on {
  width: 1.25rem;
  background: rgb(var(--mg-sky));
}""".replace("\\.", "."),
        css,
        count=1,
        flags=re.S,
    )
    # fix accidental escape in replacement - I used wrong approach
    yeshim_css.write_text(css, encoding="utf-8")
    print("css updated")
else:
    print("css already has btn")

nav_html = """        <div class="stage__nav" role="group" aria-label="Product images">
          <button type="button" class="stage__btn" data-stage-prev aria-label="Previous image">‹</button>
          <button type="button" class="stage__btn" data-stage-next aria-label="Next image">›</button>
        </div>
"""

files = [Path("product-demo-yeshim/index.html"), *Path("product-demo-yeshim/products").glob("*.html")]


def span_to_button(match: re.Match) -> str:
    key = match.group(1)
    on = match.group(2) or ""
    current = ' aria-current="true"' if on else ""
    return f'<button type="button" data-dot="{key}"{on} aria-label="{key}"{current}></button>'


for path in files:
    html = path.read_text(encoding="utf-8")
    if "data-stage-prev" not in html:
        html = html.replace(
            '      </div>\n      <div class="stage__caption">',
            nav_html + '      </div>\n      <div class="stage__caption">',
            1,
        )

    def repl_dots(m: re.Match) -> str:
        block = m.group(0)
        block = block.replace('aria-hidden="true"', 'role="tablist" aria-label="Stage slides"')
        block = re.sub(
            r'<span data-dot="([^"]+)"( class="is-on")?></span>',
            span_to_button,
            block,
        )
        return block

    html = re.sub(r'<div class="stage__dots"[^>]*>.*?</div>', repl_dots, html, count=1, flags=re.S)
    path.write_text(html, encoding="utf-8")
    print("patched", path.name)

Path("product-demo-yeshim/motion.js").write_text(
    Path("product-demo/motion.js").read_text(encoding="utf-8")
    .replace(
        """  const captions = {
    intro: "Battery-free tremor stabilization",
    how: "A damper that answers tremor",
    facts: "Light, adjustable, Class I",
    evidence: "Measured quiet - clinical proof",
    stories: "Independence you can wear",
    contact: "Ask MedGlobe about Steadi-3 Plus",
  };
""",
        "  const captions = window.MG_STAGE_CAPTIONS || {};\n",
    )
    .replace(
        """  const wavePath = (midY, amp, cycles, phase) => {
    let d = "";
    for (let x = 0; x <= 400; x += 4) {
      const y = midY + Math.sin((x / 400) * cycles * Math.PI * 2 + phase) * amp;
      d += (x === 0 ? "M" : " L") + `${x} ${y.toFixed(2)}`;
    }
    return d;
  };

  const startPlot = (plot) => {
    if (reduce || plot.dataset.plotLive) return;
    plot.dataset.plotLive = "1";
    const raw = plot.querySelector(".plot-wave--raw");
    const steady = plot.querySelector(".plot-wave--steady");
    if (!raw || !steady) return;

    const cycles = 5.2;
    raw.setAttribute("d", wavePath(52, 14, cycles, 0));
    steady.setAttribute("d", wavePath(128, 3.5, cycles, 0));

    window.setTimeout(() => {
      plot.classList.add("is-live");
      const origin = performance.now();
      const tick = (now) => {
        if (!plot.isConnected) return;
        const phase = ((now - origin) / 1000) * 1.55;
        raw.setAttribute("d", wavePath(52, 14, cycles, phase));
        steady.setAttribute("d", wavePath(128, 3.5, cycles, phase));
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }, 1150);
  };

  const reveal = (root) => {
    root.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
    root.querySelectorAll("[data-plot]").forEach(startPlot);
  };

  const animateCount = (el) => {
    const target = Number(el.dataset.count || 0);
    if (!target) return;
    if (reduce) {
      el.textContent = `${target}%`;
      return;
    }
""",
        """  const reveal = (root) => {
    root.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
  };

  const animateCount = (el) => {
    const target = Number(el.dataset.count || 0);
    if (!target) return;
    if (reduce) {
      el.textContent = String(target);
      return;
    }
""",
    )
    .replace(
        "      el.textContent = `${Math.round(target * eased)}%`;",
        "      el.textContent = String(Math.round(target * eased));",
    ),
    encoding="utf-8",
)
print("motion ok")
