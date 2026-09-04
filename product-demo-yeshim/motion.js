(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const bar = document.querySelector(".progress i");
  const captions = window.MG_STAGE_CAPTIONS || {};

  const stage = document.querySelector(".stage");
  const frame = stage?.querySelector(".stage__frame");
  const stageImgs = [...document.querySelectorAll(".stage__img")];
  const dots = [...document.querySelectorAll(".stage__dots [data-dot]")];
  const line = document.querySelector("[data-stage-line]");
  const chapters = [...document.querySelectorAll("[data-chapter]")];
  const keys = stageImgs.map((img) => img.dataset.stage).filter(Boolean);

  let active = keys[0] || "intro";
  let manualUntil = 0;

  const setStage = (key, { scrollStory = false } = {}) => {
    if (!key || !keys.includes(key)) return;
    if (key !== active) {
      active = key;
      stageImgs.forEach((img) => {
        img.classList.toggle("is-active", img.dataset.stage === key);
      });
      dots.forEach((dot) => {
        const on = dot.dataset.dot === key;
        dot.classList.toggle("is-on", on);
        if (dot.tagName === "BUTTON") {
          if (on) dot.setAttribute("aria-current", "true");
          else dot.removeAttribute("aria-current");
        }
      });
      if (line && captions[key]) {
        line.classList.add("is-swap");
        window.setTimeout(() => {
          line.textContent = captions[key];
          line.classList.remove("is-swap");
        }, 180);
      }
    }
    if (scrollStory) {
      const chapter = chapters.find((c) => c.dataset.chapter === key);
      chapter?.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    }
  };

  const stepStage = (dir) => {
    const i = Math.max(0, keys.indexOf(active));
    const next = keys[(i + dir + keys.length) % keys.length];
    manualUntil = performance.now() + 1200;
    setStage(next, { scrollStory: true });
  };

  const onScroll = () => {
    if (bar) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const p = max > 0 ? (window.scrollY / max) * 100 : 0;
      bar.style.width = `${p}%`;
    }

    if (performance.now() < manualUntil) return;

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

  stage?.querySelector("[data-stage-prev]")?.addEventListener("click", () => stepStage(-1));
  stage?.querySelector("[data-stage-next]")?.addEventListener("click", () => stepStage(1));
  dots.forEach((dot) => {
    dot.addEventListener("click", () => {
      manualUntil = performance.now() + 1200;
      setStage(dot.dataset.dot, { scrollStory: true });
    });
  });

  if (frame) {
    let startX = 0;
    let tracking = false;
    frame.addEventListener(
      "pointerdown",
      (event) => {
        if (event.pointerType === "mouse" && event.button !== 0) return;
        if (event.target.closest(".stage__btn")) return;
        tracking = true;
        startX = event.clientX;
      },
      { passive: true }
    );
    frame.addEventListener("pointerup", (event) => {
      if (!tracking) return;
      tracking = false;
      const dx = event.clientX - startX;
      if (Math.abs(dx) < 42) return;
      stepStage(dx < 0 ? 1 : -1);
    });
    frame.addEventListener("pointercancel", () => {
      tracking = false;
    });
  }

  const form = document.querySelector(".block--ask form");
  if (form) form.addEventListener("submit", (e) => e.preventDefault());

  const reveal = (root) => {
    root.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
  };

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
        reveal(entry.target);
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.2, rootMargin: "0px 0px -8% 0px" }
  );

  document.querySelectorAll("[data-scene]").forEach((scene) => io.observe(scene));
})();
