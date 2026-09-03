(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const bar = document.querySelector(".progress i");
  const captions = {
    intro: "Battery-free tremor stabilization",
    how: "A damper that answers tremor",
    facts: "Light, adjustable, Class I",
    evidence: "Measured quiet - clinical proof",
    stories: "Independence you can wear",
    contact: "Ask MedGlobe about Steadi-3 Plus",
  };

  const stageImgs = [...document.querySelectorAll(".stage__img")];
  const dots = [...document.querySelectorAll(".stage__dots [data-dot]")];
  const line = document.querySelector("[data-stage-line]");
  const chapters = [...document.querySelectorAll("[data-chapter]")];

  let active = "intro";
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

  const wavePath = (midY, amp, cycles, phase) => {
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

  // Count-up stats
  const animateCount = (el) => {
    const target = Number(el.dataset.count || 0);
    if (!target) return;
    if (reduce) {
      el.textContent = `${target}%`;
      return;
    }
    const start = performance.now();
    const dur = 1100;
    const tick = (now) => {
      const t = Math.min(1, (now - start) / dur);
      const eased = 1 - Math.pow(1 - t, 3);
      el.textContent = `${Math.round(target * eased)}%`;
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
        reveal(entry.target);
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.2, rootMargin: "0px 0px -8% 0px" }
  );

  document.querySelectorAll("[data-scene]").forEach((scene) => io.observe(scene));
})();
