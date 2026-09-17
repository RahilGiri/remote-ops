with open('css/style.css', 'a') as f:
    f.write("""
.fade-up-text {
    animation: fadeUp 1.2s cubic-bezier(0.23, 1, 0.32, 1) forwards;
    opacity: 0;
    transform: translateY(30px);
}
@keyframes fadeUp {
    to { opacity: 1; transform: translateY(0); }
}
""")

with open('index.html', 'r') as f:
    html = f.read()

html = html.replace("<h1>You Focus on the Deals. <br><span class=\"text-gradient\">We Handle the Work.</span></h1>", 
                    "<h1 class=\"fade-up-text\">You Focus on the Deals. <br><span class=\"text-gradient\">We Handle the Work.</span></h1>")

with open('index.html', 'w') as f:
    f.write(html)
