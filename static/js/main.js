(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canHover = window.matchMedia('(hover: hover)').matches;

  /* ---------- mobile menu ---------- */
  const menu = document.getElementById('nav-links');
  const burger = document.querySelector('.hamburger');

  function setMenu(open) {
    if (!menu || !burger) return;
    menu.classList.toggle('show', open);
    burger.setAttribute('aria-expanded', String(open));
  }

  if (burger) {
    burger.addEventListener('click', (e) => {
      e.stopPropagation();
      setMenu(!menu.classList.contains('show'));
    });
  }
  document.addEventListener('click', (e) => {
    if (!menu) return;
    if (!menu.contains(e.target) || e.target.tagName === 'A') setMenu(false);
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });

  /* ---------- nav gets a solid background once you scroll ---------- */
  const nav = document.querySelector('.nav-bar');
  const onScroll = () => nav && nav.classList.toggle('is-solid', window.scrollY > 40);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- video helpers ---------- */
  function play(video) {
    if (reduceMotion || !video) return;
    const p = video.play();
    if (p && p.catch) p.catch(() => {});
  }
  function pause(video) { if (video) video.pause(); }

  // Hero video: respect reduced motion.
  document.querySelectorAll('.hero-video, .page-hero-media video').forEach((v) => {
    if (reduceMotion) { v.removeAttribute('autoplay'); v.pause(); }
  });

  // Hero magpie: the clip doesn't loop seamlessly, so it fades to black for its
  // last 0.3s, holds 2s of darkness, then fades back in from the first frame.
  const heroVideo = document.querySelector('.hero-video');
  if (heroVideo && !reduceMotion) {
    const FADE = 0.3, HOLD = 2000;
    heroVideo.loop = false;
    const watch = () => {
      if (heroVideo.duration && heroVideo.currentTime >= heroVideo.duration - FADE) {
        heroVideo.classList.add('is-dark');
      }
      requestAnimationFrame(watch);
    };
    requestAnimationFrame(watch);
    heroVideo.addEventListener('ended', () => {
      heroVideo.classList.add('is-dark');
      setTimeout(() => {
        heroVideo.currentTime = 0;
        play(heroVideo);
        heroVideo.classList.remove('is-dark');
      }, HOLD);
    });
  }

  // Background loops only play while on screen.
  const bgVideos = document.querySelectorAll('video[data-autoplay]');

  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => { if (entry.isIntersecting) play(entry.target); else pause(entry.target); });
    }, { threshold: 0.35 });
    bgVideos.forEach((v) => io.observe(v));
  } else {
    bgVideos.forEach(play);
  }

  /* ---------- Lab: crossfading AI loops behind the copy ---------- */
  const lab = document.querySelector('.lab');
  if (lab) {
    const scenes = Array.from(lab.querySelectorAll('.lab-scene'));
    const tabs = Array.from(lab.querySelectorAll('.lab-tab'));
    const nameEl = lab.querySelector('.lab-now-name');
    const modelEl = lab.querySelector('.lab-now-model');
    const promptBox = lab.querySelector('.lab-prompt');
    const promptEl = promptBox ? promptBox.querySelector('p') : null;
    const DURATION = 8000;
    lab.style.setProperty('--lab-duration', DURATION + 'ms');

    let current = 0;
    let timer = null;
    let inView = false;

    function show(i) {
      current = (i + scenes.length) % scenes.length;
      scenes.forEach((v, n) => {
        const active = n === current;
        v.classList.toggle('is-active', active);
        if (active) { v.preload = 'auto'; if (inView) play(v); }
        else { setTimeout(() => { if (!v.classList.contains('is-active')) pause(v); }, 1500); }
      });
      tabs.forEach((t, n) => {
        t.classList.toggle('is-active', n === current);
        t.classList.toggle('is-done', n < current);
        t.setAttribute('aria-pressed', String(n === current));
        // restart the progress bar animation
        const bar = t.querySelector('.lab-tab-bar');
        if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
      });
      const t = tabs[current];
      if (t) {
        if (nameEl) nameEl.textContent = t.dataset.title;
        if (modelEl) modelEl.textContent = t.dataset.model;
        if (promptEl) promptEl.textContent = t.dataset.prompt;
      }
      // warm up the next clip so the crossfade has frames to show
      const next = scenes[(current + 1) % scenes.length];
      if (next) next.preload = 'auto';
    }

    function shouldRun() {
      return inView && !reduceMotion && !(promptBox && promptBox.open) && !document.hidden;
    }

    function schedule() {
      clearTimeout(timer);
      lab.classList.toggle('is-paused', !shouldRun());
      if (!shouldRun()) return;
      const bar = tabs[current] && tabs[current].querySelector('.lab-tab-bar');
      if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
      timer = setTimeout(() => { show(current + 1); schedule(); }, DURATION);
    }

    tabs.forEach((t, n) => t.addEventListener('click', () => { show(n); schedule(); }));
    if (promptBox) promptBox.addEventListener('toggle', schedule);
    document.addEventListener('visibilitychange', schedule);

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([entry]) => {
        inView = entry.isIntersecting;
        const v = scenes[current];
        if (inView) play(v); else pause(v);
        schedule();
      }, { threshold: 0.25 }).observe(lab);
    }
  }

  /* ---------- YouTube facade: load the player only when asked ---------- */
  document.querySelectorAll('.yt[data-yt]').forEach((box) => {
    const btn = box.querySelector('.yt-play');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + box.dataset.yt + '?autoplay=1&rel=0';
      iframe.title = btn.textContent.trim();
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      iframe.referrerPolicy = 'strict-origin-when-cross-origin';
      iframe.allowFullscreen = true;
      box.replaceChildren(iframe);
      iframe.focus();
    });
  });
})();
