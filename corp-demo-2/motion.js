(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const bar = document.querySelector(".progress__bar");
  const back = document.querySelector(".back");

  const onScroll = () => {
    if (bar) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const p = max > 0 ? (window.scrollY / max) * 100 : 0;
      bar.style.width = `${p}%`;
    }
    if (back) {
      const y = window.scrollY;
      const heroH = window.innerHeight * 0.85;
      back.style.background =
        y > heroH ? "rgb(18 17 15 / 72%)" : "rgb(18 17 15 / 55%)";
    }
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const form = document.querySelector(".whisper form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      const thanks = form.querySelector(".whisper__thanks");
      if (thanks) thanks.hidden = false;
      form.classList.add("is-sent");
    });
  }

  if (reduce) {
    document.querySelectorAll("[data-reveal]").forEach((el) => el.classList.add("is-in"));
    document.querySelector(".folio")?.classList.add("is-seen");
    return;
  }

  // Hero brand + hint after first paint
  requestAnimationFrame(() => {
    document.querySelectorAll(".arrive [data-reveal]").forEach((el) => {
      el.classList.add("is-in");
    });
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const root = entry.target;
        root.querySelectorAll("[data-reveal]").forEach((el) => el.classList.add("is-in"));
        if (root.hasAttribute("data-reveal")) root.classList.add("is-in");
        if (root.classList.contains("folio")) root.classList.add("is-seen");
        io.unobserve(root);
      });
    },
    { threshold: 0.22, rootMargin: "0px 0px -10% 0px" }
  );

  document.querySelectorAll("[data-scene]").forEach((scene) => io.observe(scene));

  // Footer reveal
  const end = document.querySelector(".end");
  if (end) {
    const endIo = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          end.classList.add("is-in");
          endIo.unobserve(end);
        });
      },
      { threshold: 0.4 }
    );
    endIo.observe(end);
  }

  // Soft parallax on folio image
  const folio = document.querySelector(".folio");
  const folioImg = document.querySelector(".folio img[data-parallax]");
  if (folio && folioImg) {
    let ticking = false;
    const tick = () => {
      const rect = folio.getBoundingClientRect();
      const view = window.innerHeight || 1;
      const mid = rect.top + rect.height / 2;
      const offset = ((mid - view / 2) / view) * -22;
      folioImg.style.transform = `translate3d(0, ${offset.toFixed(2)}px, 0) scale(1.1)`;
      ticking = false;
    };
    window.addEventListener(
      "scroll",
      () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(tick);
      },
      { passive: true }
    );
    tick();
  }
})();
