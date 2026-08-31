(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const form = document.querySelector(".request form");
  if (form) form.addEventListener("submit", (e) => e.preventDefault());

  if (reduce) {
    document.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
    return;
  }

  requestAnimationFrame(() => {
    document.querySelectorAll(".sheet [data-in]").forEach((el) => el.classList.add("is-on"));
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.18, rootMargin: "0px 0px -8% 0px" }
  );

  document.querySelectorAll("[data-scene]").forEach((scene) => io.observe(scene));
})();
