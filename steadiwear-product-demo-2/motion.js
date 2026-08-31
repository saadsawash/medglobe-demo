(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const form = document.querySelector(".close form");
  if (form) form.addEventListener("submit", (e) => e.preventDefault());

  // Product turntable
  const tabs = [...document.querySelectorAll(".turn__controls [data-view]")];
  const shots = [...document.querySelectorAll(".turn__shot")];
  const show = (index) => {
    const i = Number(index);
    tabs.forEach((tab) => {
      const on = Number(tab.dataset.view) === i;
      tab.setAttribute("aria-selected", on ? "true" : "false");
    });
    shots.forEach((shot) => {
      shot.classList.toggle("is-active", Number(shot.dataset.shot) === i);
    });
  };
  tabs.forEach((tab) => {
    tab.addEventListener("click", () => show(tab.dataset.view));
  });

  if (reduce) {
    document.querySelectorAll("[data-in]").forEach((el) => el.classList.add("is-on"));
    return;
  }

  requestAnimationFrame(() => {
    document.querySelectorAll(".plinth [data-in]").forEach((el) => el.classList.add("is-on"));
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
