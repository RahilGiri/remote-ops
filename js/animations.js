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

  revealOnScroll();
  window.addEventListener('scroll', revealOnScroll, { passive: true });

  // ---------------------------------------------------
  // Premium 3D Mouse Tracking Tilt Effect for Cards
  // ---------------------------------------------------
  const cards = document.querySelectorAll('.card');
  
  cards.forEach(card => {
    // Add glare element if it doesn't exist
    let glare = card.querySelector('.glare');
    if (!glare) {
      glare = document.createElement('div');
      glare.className = 'glare';
      glare.style.position = 'absolute';
      glare.style.top = '0';
      glare.style.left = '0';
      glare.style.width = '100%';
      glare.style.height = '100%';
      glare.style.pointerEvents = 'none';
      glare.style.opacity = '0';
      glare.style.zIndex = '10';
      glare.style.borderRadius = 'inherit';
      card.appendChild(glare);
    }

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left; 
      const y = e.clientY - rect.top;  
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      // Calculate rotation amount (max 6 degrees for subtle premium feel)
      const rotateX = ((y - centerY) / centerY) * -6; 
      const rotateY = ((x - centerX) / centerX) * 6;
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
      
      card.style.transform = `perspective(1000px) scale(1.02) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
      card.style.transition = 'none'; // remove transition for smooth tracking
      
      const px = (x / rect.width) * 100;
      const py = (y / rect.height) * 100;
      glare.style.background = `radial-gradient(circle at ${px}% ${py}%, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0) 50%)`;
      glare.style.opacity = '1';
    });
    
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) scale(1) rotateX(0deg) rotateY(0deg)';
      card.style.transition = 'transform 0.5s cubic-bezier(0.23, 1, 0.32, 1)';
      glare.style.opacity = '0';
      glare.style.transition = 'opacity 0.5s ease';
    });
    
    card.addEventListener('mouseenter', () => {
      card.style.transition = 'transform 0.1s cubic-bezier(0.23, 1, 0.32, 1)';
    });
  });
});
