// Scroll Animations
document.addEventListener('DOMContentLoaded', () => {
  const revealElements = document.querySelectorAll('.reveal');
  const revealGroups = document.querySelectorAll('.reveal-group');

  const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    const elementVisible = 100;

    revealElements.forEach(element => {
      const elementTop = element.getBoundingClientRect().top;
      if (elementTop < windowHeight - elementVisible) {
        element.classList.add('active');
      }
    });

    revealGroups.forEach(group => {
      const elementTop = group.getBoundingClientRect().top;
      if (elementTop < windowHeight - elementVisible) {
        group.classList.add('active');
      }
    });
  };

  // Initial check
  revealOnScroll();

  // Add scroll listener
  window.addEventListener('scroll', revealOnScroll, { passive: true });

  // ---------------------------------------------------
  // 3D Tilt Effect for Cards
  // ---------------------------------------------------
  const cards = document.querySelectorAll('.card');
  
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left; // x position within the element
      const y = e.clientY - rect.top;  // y position within the element
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = ((y - centerY) / centerY) * -5; // max rotation degrees
      const rotateY = ((x - centerX) / centerX) * 5;
      
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px) scale(1.02)`;
      card.style.transition = 'none'; // remove transition for smooth tracking
      
      // Add a subtle glare effect
      let glare = card.querySelector('.glare');
      if (!glare) {
        glare = document.createElement('div');
        glare.className = 'glare';
        card.appendChild(glare);
      }
      
      const px = (x / rect.width) * 100;
      const py = (y / rect.height) * 100;
      glare.style.background = `radial-gradient(circle at ${px}% ${py}%, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 40%)`;
      glare.style.opacity = '1';
    });
    
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0) scale(1)';
      card.style.transition = 'transform 0.5s cubic-bezier(0.23, 1, 0.32, 1)';
      
      const glare = card.querySelector('.glare');
      if (glare) {
        glare.style.opacity = '0';
        glare.style.transition = 'opacity 0.5s ease';
      }
    });
    
    card.addEventListener('mouseenter', () => {
      card.style.transition = 'transform 0.1s cubic-bezier(0.23, 1, 0.32, 1)';
    });
  });
});
