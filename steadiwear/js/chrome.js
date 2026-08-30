(() => {
  const header = document.getElementById("sw-header");
  const rail = document.getElementById("sw-rail");
  const drawer = document.getElementById("sw-drawer");
  const menuBtn = document.querySelector(".sw-header__menu-btn");
  const closeBtn = document.querySelector(".sw-drawer__close");

  if (!header) return;

  const prefersReduce = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const freezeHeight = () => {
    const bar = header.querySelector(".sw-header__bar");
    const height = bar ? bar.getBoundingClientRect().height : header.offsetHeight;
    document.documentElement.style.setProperty("--sw-header-height", `${height.toFixed(2)}px`);
  };

  const syncCompact = () => {
    const compact = window.scrollY > 72;
    header.classList.toggle("sw-header--compact", compact);

    if (!rail) return;

    rail.classList.toggle("sw-rail--visible", compact);

    const links = [...rail.querySelectorAll('a[href^="#"]')];
    const line = Math.max(160, window.innerHeight * 0.28);
    let active = null;

    links.forEach((link) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (target && target.getBoundingClientRect().top <= line) active = link;
    });

    links.forEach((link) => {
      if (link === active) link.setAttribute("aria-current", "true");
      else link.removeAttribute("aria-current");
    });
  };

  const closeDrawer = () => {
    if (drawer?.open) drawer.close();
  };

  const openDrawer = () => {
    drawer?.showModal();
  };

  menuBtn?.addEventListener("click", openDrawer);
  closeBtn?.addEventListener("click", closeDrawer);

  drawer?.addEventListener("click", (event) => {
    if (event.target === drawer) closeDrawer();
  });

  drawer?.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", closeDrawer);
  });

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    const id = link.getAttribute("href");
    if (!id || id === "#") return;

    link.addEventListener("click", (event) => {
      const target = id === "#top" ? document.body : document.querySelector(id);
      if (!target) return;

      event.preventDefault();

      if (id === "#top") {
        window.scrollTo({ top: 0, behavior: prefersReduce() ? "auto" : "smooth" });
      } else {
        target.scrollIntoView({ behavior: prefersReduce() ? "auto" : "smooth", block: "start" });
      }

      if (location.hash !== id) history.pushState(null, "", id);
      closeDrawer();
    });
  });

  window.addEventListener("resize", () => {
    freezeHeight();
    syncCompact();
  });

  window.addEventListener("scroll", syncCompact, { passive: true });
  window.addEventListener("load", () => {
    freezeHeight();
    syncCompact();
  });

  freezeHeight();
  syncCompact();
  requestAnimationFrame(freezeHeight);
})();
