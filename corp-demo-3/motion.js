(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fill = document.querySelector(".rail__fill");

  const onScroll = () => {
    if (!fill) return;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const p = max > 0 ? (window.scrollY / max) * 100 : 0;
    fill.style.width = `${p}%`;
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const form = document.querySelector(".desk form");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
    });
  }

  if (reduce) {
    document.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
    return;
  }

  requestAnimationFrame(() => {
    document.querySelectorAll(".gate [data-in]").forEach((el) => el.classList.add("is-on"));
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.24, rootMargin: "0px 0px -8% 0px" }
  );

  document.querySelectorAll("[data-scene]").forEach((scene) => io.observe(scene));
})();
