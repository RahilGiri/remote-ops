import os

def get_shell(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    parts = content.split('<main>')
    head = parts[0]
    tail = parts[1].split('</main>')[1]
    return head, tail

head, tail = get_shell('how-it-works.html')

how_it_works_html = """
    <main>
        <section class="hero section-light">
            <div class="container text-center reveal fade-in">
                <span class="tag" style="margin-bottom: 2rem;">Methodology</span>
                <h1>A Simple Way to Add Remote Support.</h1>
                <p>We built our onboarding process to be completely frictionless. From discovery to daily execution, here is exactly how we integrate into your real estate business.</p>
            </div>
        </section>

        <section class="section-surface" style="padding-top: 0;">
            <div class="container pull-up reveal fade-in">
                <div class="card" style="padding: 4rem;">
                    <div class="grid-2" style="gap: 4rem;">
                        <div>
                            <div style="font-size: 3rem; color: var(--accent); font-weight: 800; line-height: 1; margin-bottom: 1rem;">01</div>
                            <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Discovery & Audit</h3>
                            <p style="color: var(--secondary); font-size: 1.1rem; line-height: 1.7; margin-bottom: 2rem;">We start by auditing your current operations. We identify where you are spending too much time, which CRM workflows are broken, and exactly which tasks should be delegated to a virtual assistant.</p>
                            
                            <div style="font-size: 3rem; color: var(--accent); font-weight: 800; line-height: 1; margin-bottom: 1rem;">02</div>
                            <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Workflow Mapping</h3>
                            <p style="color: var(--secondary); font-size: 1.1rem; line-height: 1.7; margin-bottom: 2rem;">Before we touch your systems, we document the exact process. We build Standard Operating Procedures (SOPs) for how leads should be tagged, how social media should be scheduled, and how investors should be emailed.</p>

                            <div style="font-size: 3rem; color: var(--accent); font-weight: 800; line-height: 1; margin-bottom: 1rem;">03</div>
                            <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Onboarding & Integration</h3>
                            <p style="color: var(--secondary); font-size: 1.1rem; line-height: 1.7;">Your dedicated VA is granted access to your tech stack (GoHighLevel, Mailchimp, Slack, etc.). We ensure all permissions are secure and the communication channels are firmly established.</p>
                        </div>
                        
                        <div>
                            <div style="font-size: 3rem; color: var(--primary); font-weight: 800; line-height: 1; margin-bottom: 1rem;">04</div>
                            <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Daily Execution</h3>
                            <p style="color: var(--secondary); font-size: 1.1rem; line-height: 1.7; margin-bottom: 2rem;">Your VA begins executing the mapped workflows. Whether it is pulling daily lead lists, responding to CRM inquiries, or formatting offering memorandums, the work gets done consistently and on time.</p>
                            
                            <div style="font-size: 3rem; color: var(--primary); font-weight: 800; line-height: 1; margin-bottom: 1rem;">05</div>
                            <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Reporting & Analytics</h3>
                            <p style="color: var(--secondary); font-size: 1.1rem; line-height: 1.7; margin-bottom: 2rem;">You are never left in the dark. At the end of every week, you receive a concise report detailing exactly what was accomplished, how many leads were processed, and what is on the schedule for next week.</p>

                            <div style="font-size: 3rem; color: var(--primary); font-weight: 800; line-height: 1; margin-bottom: 1rem;">06</div>
                            <h3 style="font-size: 1.75rem; margin-bottom: 1rem;">Optimization</h3>
                            <p style="color: var(--secondary); font-size: 1.1rem; line-height: 1.7;">As your business grows, your operational needs will change. We hold regular strategy calls to optimize your workflows, introduce new automation, and ensure your VA is always providing maximum leverage.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="section-light">
            <div class="container text-center">
                <h2>Ready to map your workflows?</h2>
                <a href="book-consultation.html" class="btn btn-primary mt-2">Book a Free Consultation</a>
            </div>
        </section>
    </main>
"""

with open('how-it-works.html', 'w') as f:
    f.write(head + how_it_works_html + tail)

about_html = """
    <main>
        <section class="hero section-light">
            <div class="container text-center reveal fade-in">
                <span class="tag" style="margin-bottom: 2rem;">Our Story</span>
                <h1>Built by Real Estate Operators.</h1>
                <p>We understand the industry because we work in it. We built RemoteOps to solve the exact operational bottlenecks we faced ourselves.</p>
            </div>
        </section>

        <section class="section-surface" style="padding-top: 0;">
            <div class="container pull-up reveal fade-in">
                <div class="card" style="padding: 0; overflow: hidden; border: none; box-shadow: 0 30px 60px rgba(0,0,0,0.08);">
                    <div style="height: 400px; background: url('https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=1600&auto=format&fit=crop') center/cover;"></div>
                    <div style="padding: 4rem;">
                        <div class="grid-2" style="gap: 4rem; align-items: center;">
                            <div>
                                <h2 style="font-size: 2.25rem; margin-bottom: 1.5rem;">Why We Started RemoteOps</h2>
                                <p style="font-size: 1.15rem; color: var(--secondary); line-height: 1.8; margin-bottom: 1.5rem;">The real estate industry is uniquely demanding. Between managing complex CRM pipelines, formatting offering memorandums, and constantly prospecting for deals, top producers are often drowning in administrative work.</p>
                                <p style="font-size: 1.15rem; color: var(--secondary); line-height: 1.8;">We found that generic virtual assistant agencies simply didn't understand the nuance of real estate. They didn't know what a cap rate was, how to navigate GoHighLevel, or how to pull property owner data. We built RemoteOps to provide highly trained, industry specific operational support.</p>
                            </div>
                            <div>
                                <div style="background: var(--surface); padding: 2rem; border-radius: 12px; border: 1px solid var(--border);">
                                    <h3 style="margin-bottom: 1rem; color: var(--primary);">Our Core Mission</h3>
                                    <p style="color: var(--secondary); line-height: 1.6;">To give real estate and investment professionals their time back so they can focus 100% of their energy on underwriting, negotiating, and closing deals.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
"""

head_about, tail_about = get_shell('about.html')
with open('about.html', 'w') as f:
    f.write(head_about + about_html + tail_about)

print("Core pages enhanced!")
