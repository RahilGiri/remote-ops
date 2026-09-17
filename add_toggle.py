import os

with open('pricing.html', 'r') as f:
    content = f.read()

toggle_html = """
      <div class="pricing-toggle-wrapper" style="margin-top: 3rem; display: flex; align-items: center; justify-content: center; gap: 1rem;">
        <span id="label-monthly" style="font-weight: 700; color: white;">Monthly</span>
        <label class="toggle-switch" style="position: relative; display: inline-block; width: 60px; height: 34px;">
          <input type="checkbox" id="pricing-toggle" style="opacity: 0; width: 0; height: 0;">
          <span class="slider round" style="position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: rgba(255,255,255,0.3); transition: .4s; border-radius: 34px;">
             <span style="position: absolute; content: ''; height: 26px; width: 26px; left: 4px; bottom: 4px; background-color: white; transition: .4s; border-radius: 50%;"></span>
          </span>
        </label>
        <span id="label-annually" style="font-weight: 600; color: rgba(255,255,255,0.6);">Annually <span style="background: var(--accent); color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; margin-left: 5px;">Save 15%</span></span>
      </div>
"""

# Insert toggle under the p tag in hero
content = content.replace('<p>Hire elite, highly trained real estate virtual assistants without the massive overhead of in house employees.</p>', 
                          '<p>Hire elite, highly trained real estate virtual assistants without the massive overhead of in house employees.</p>' + toggle_html)

# Add IDs and transition to prices
content = content.replace(
    '<div style="font-size: 3rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">\n          $350',
    '<div id="price-part-time" style="font-size: 3rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem; transition: all 0.3s ease;">\n          $350'
)

content = content.replace(
    '<div style="font-size: 3rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem;">\n          $600',
    '<div id="price-full-time" style="font-size: 3rem; font-weight: 800; color: var(--primary); margin-bottom: 0.5rem; transition: all 0.3s ease;">\n          $600'
)

# Add the script at the end
script = """
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const toggle = document.getElementById('pricing-toggle');
      if(!toggle) return;
      const labelMonthly = document.getElementById('label-monthly');
      const labelAnnually = document.getElementById('label-annually');
      
      const partTimePrice = document.getElementById('price-part-time');
      const fullTimePrice = document.getElementById('price-full-time');
      
      toggle.addEventListener('change', function() {
        const isAnnual = this.checked;
        const sliderInner = document.querySelector('.slider span');
        const sliderBg = document.querySelector('.slider');
        
        if(isAnnual) {
          sliderInner.style.transform = 'translateX(26px)';
          sliderBg.style.backgroundColor = 'var(--accent)';
          labelAnnually.style.fontWeight = '700';
          labelAnnually.style.color = 'white';
          labelMonthly.style.fontWeight = '600';
          labelMonthly.style.color = 'rgba(255,255,255,0.6)';
          
          animatePrice(partTimePrice, 295);
          animatePrice(fullTimePrice, 510);
        } else {
          sliderInner.style.transform = 'translateX(0)';
          sliderBg.style.backgroundColor = 'rgba(255,255,255,0.3)';
          labelMonthly.style.fontWeight = '700';
          labelMonthly.style.color = 'white';
          labelAnnually.style.fontWeight = '600';
          labelAnnually.style.color = 'rgba(255,255,255,0.6)';
          
          animatePrice(partTimePrice, 350);
          animatePrice(fullTimePrice, 600);
        }
      });
      
      function animatePrice(element, newPrice) {
        if(!element) return;
        element.style.opacity = '0';
        element.style.transform = 'translateY(-10px)';
        
        setTimeout(() => {
          element.innerHTML = '\\n          $' + newPrice + '<span style="font-size: 1rem; color: var(--secondary); font-weight: 500;">/mo</span>';
          element.style.opacity = '1';
          element.style.transform = 'translateY(0)';
        }, 300);
      }
    });
  </script>
</body>
"""
content = content.replace('</body>', script)

with open('pricing.html', 'w') as f:
    f.write(content)

print("Toggle added!")
