// Main JS file
document.addEventListener('DOMContentLoaded', () => {
  // Update copyright year in footer
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const headerOffset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')) || 80;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // FAQ Accordion
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentNode;
      const content = item.querySelector('.accordion-content');
      
      // Close other open items
      const currentActive = document.querySelector('.accordion-item.active');
      if (currentActive && currentActive !== item) {
        currentActive.classList.remove('active');
        currentActive.querySelector('.accordion-content').style.maxHeight = null;
      }
      
      // Toggle current item
      item.classList.toggle('active');
      if (item.classList.contains('active')) {
        content.style.maxHeight = content.scrollHeight + "px";
      } else {
        content.style.maxHeight = null;
      }
    });
  });
});
