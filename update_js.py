with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("const revealElements = document.querySelectorAll('.reveal');", "const revealElements = document.querySelectorAll('.reveal, .mask-reveal, .fade-up-text');")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
