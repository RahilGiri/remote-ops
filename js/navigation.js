// Mobile Navigation
document.addEventListener('DOMContentLoaded', () => {
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');
  const dropdowns = document.querySelectorAll('.dropdown');

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true' || false;
      mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
      mobileMenuBtn.innerHTML = navLinks.classList.contains('active') ? '✕' : '☰';
    });
  }

  // Handle mobile dropdowns
  dropdowns.forEach(dropdown => {
    const link = dropdown.querySelector('a');
    link.addEventListener('click', (e) => {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        dropdown.classList.toggle('active');
      }
    });
  });

  // Header scroll effect
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.style.boxShadow = 'var(--shadow-sm)';
      header.style.padding = '0.5rem 0';
    } else {
      header.style.boxShadow = 'none';
      header.style.padding = '0';
    }
  });
});
