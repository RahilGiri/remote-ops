import os

with open('pricing.html', 'r') as f:
    content = f.read()

faq_html = """
    <section class="section-surface" style="padding-bottom: 5rem;">
    <div class="container reveal fade-in" style="max-width: 800px;">
      <h2 class="text-center" style="margin-bottom: 3rem;">Frequently Asked Questions</h2>
      
      <div class="accordion">
        <div class="accordion-item" style="border-bottom: 1px solid var(--border); padding: 1.5rem 0;">
          <button class="accordion-header" style="width: 100%; display: flex; justify-content: space-between; align-items: center; background: none; border: none; cursor: pointer; text-align: left; font-size: 1.25rem; font-weight: 600; color: var(--primary);">
            Do I have to sign a long term contract?
            <span class="icon" style="font-size: 1.5rem; color: var(--accent); transition: transform 0.3s ease;">+</span>
          </button>
          <div class="accordion-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="color: var(--secondary); padding-top: 1rem; line-height: 1.7;">No! We believe in earning your business every single month. All of our standard virtual assistant plans are month to month. If we aren't saving you time, you can cancel anytime.</p>
          </div>
        </div>

        <div class="accordion-item" style="border-bottom: 1px solid var(--border); padding: 1.5rem 0;">
          <button class="accordion-header" style="width: 100%; display: flex; justify-content: space-between; align-items: center; background: none; border: none; cursor: pointer; text-align: left; font-size: 1.25rem; font-weight: 600; color: var(--primary);">
            What if my VA goes on vacation or gets sick?
            <span class="icon" style="font-size: 1.5rem; color: var(--accent); transition: transform 0.3s ease;">+</span>
          </button>
          <div class="accordion-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="color: var(--secondary); padding-top: 1rem; line-height: 1.7;">When you hire RemoteOps, you hire our entire infrastructure. If your dedicated VA takes paid time off or is out sick, our operations managers immediately step in to ensure your daily workflows continue uninterrupted.</p>
          </div>
        </div>

        <div class="accordion-item" style="border-bottom: 1px solid var(--border); padding: 1.5rem 0;">
          <button class="accordion-header" style="width: 100%; display: flex; justify-content: space-between; align-items: center; background: none; border: none; cursor: pointer; text-align: left; font-size: 1.25rem; font-weight: 600; color: var(--primary);">
            Are your VAs trained in my specific software?
            <span class="icon" style="font-size: 1.5rem; color: var(--accent); transition: transform 0.3s ease;">+</span>
          </button>
          <div class="accordion-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
            <p style="color: var(--secondary); padding-top: 1rem; line-height: 1.7;">Yes. Our virtual assistants undergo rigorous training in standard real estate tech stacks including GoHighLevel, Follow Up Boss, Salesforce, AppFolio, Canva, and Mailchimp before they ever touch your account.</p>
          </div>
        </div>
      </div>
    </div>
    </section>
"""

# Insert FAQ above the final section-light
content = content.replace('<section class="section-light">', faq_html + '\n    <section class="section-light">')

# Add JS for accordion
accordion_js = """
      const accordions = document.querySelectorAll('.accordion-header');
      accordions.forEach(acc => {
        acc.addEventListener('click', function() {
          const content = this.nextElementSibling;
          const icon = this.querySelector('.icon');
          
          if(content.style.maxHeight && content.style.maxHeight !== '0px') {
            content.style.maxHeight = '0px';
            icon.style.transform = 'rotate(0deg)';
            icon.textContent = '+';
          } else {
            content.style.maxHeight = content.scrollHeight + 'px';
            icon.style.transform = 'rotate(45deg)';
          }
        });
      });
"""
content = content.replace("function animatePrice(element, newPrice) {", accordion_js + "\n      function animatePrice(element, newPrice) {")

with open('pricing.html', 'w') as f:
    f.write(content)

print("FAQ accordion added!")
