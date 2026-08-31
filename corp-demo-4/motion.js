(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const bar = document.querySelector(".progress i");
  const spineLinks = [...document.querySelectorAll(".spine a")];
  const scenes = [...document.querySelectorAll(".pair[id]")];

  const onScroll = () => {
    if (bar) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const p = max > 0 ? (window.scrollY / max) * 100 : 0;
      bar.style.width = `${p}%`;
    }

    let active = null;
    const mid = window.innerHeight * 0.4;
    scenes.forEach((scene) => {
      const r = scene.getBoundingClientRect();
      if (r.top <= mid && r.bottom >= mid) active = scene.id;
    });
    spineLinks.forEach((link) => {
      link.classList.toggle("is-active", active && link.getAttribute("href") === `#${active}`);
    });
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const form = document.querySelector(".turn form");
  if (form) form.addEventListener("submit", (e) => e.preventDefault());

  if (reduce) {
    document.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
    return;
  }

  requestAnimationFrame(() => {
    document.querySelectorAll(".cover [data-in]").forEach((el) => el.classList.add("is-on"));
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.22, rootMargin: "0px 0px -8% 0px" }
  );

  document.querySelectorAll("[data-scene]").forEach((scene) => io.observe(scene));
})();
