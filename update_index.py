import os

filepath = "index.html"
with open(filepath, "r") as f:
    content = f.read()

# Replace the Hero text
old_hero_p = "<p>Stop drowning in administrative tasks. We provide premium remote operations, CRM management, research, and marketing support exclusively for US-based real estate and investment businesses.</p>"
new_hero_p = "<p>Stop drowning in administrative tasks. We provide highly trained real estate virtual assistants and operations partners for CRM management, research, and marketing support exclusively for US-based real estate and investment businesses.</p>"
content = content.replace(old_hero_p, new_hero_p)

# Create a new section about Virtual Assistants
va_section = """
        <!-- VIRTUAL ASSISTANTS SECTION -->
        <section class="section-surface text-center" style="border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
            <div class="container reveal fade-in">
                <div class="section-header">
                    <span class="tag">Specialized Talent</span>
                    <h2>Dedicated Real Estate Virtual Assistants.</h2>
                    <p>Not just another generic VA. Our virtual assistants are specifically trained on real estate workflows, CRM systems, and investment terminology.</p>
                </div>
                <div class="grid-3 reveal-group mt-4">
                    <div class="card reveal-item" style="text-align: left;">
                        <h3 class="card-title">Pre-Trained on Real Estate</h3>
                        <div class="card-content">
                            <p>Our VAs understand capitalization rates, syndication structures, pipelines, and the terminology that keeps your deals moving without needing months of hand-holding.</p>
                        </div>
                    </div>
                    <div class="card reveal-item" style="text-align: left;">
                        <h3 class="card-title">Fluent in Your Software</h3>
                        <div class="card-content">
                            <p>Whether you use GoHighLevel, Buildium, AppFolio, Salesforce, or just a sophisticated Google Sheet, our virtual assistants integrate into your exact tech stack.</p>
                        </div>
                    </div>
                    <div class="card reveal-item" style="text-align: left;">
                        <h3 class="card-title">US Timezone Alignment</h3>
                        <div class="card-content">
                            <p>Your dedicated real estate virtual assistant works when you work, ensuring fast communication, live CRM updates, and immediate task execution during your business hours.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# Inject the VA section right after the Logo Strip
logo_strip_end = content.find("<!-- PROBLEM -->")
if logo_strip_end != -1:
    content = content[:logo_strip_end] + va_section + "\n        " + content[logo_strip_end:]

with open(filepath, "w") as f:
    f.write(content)

print("Updated index.html")
