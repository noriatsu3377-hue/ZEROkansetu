with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Change threshold from 0.1 to 0
js = js.replace("threshold: 0.1", "threshold: 0.02")
js = js.replace("rootMargin: '0px 0px -10% 0px'", "rootMargin: '0px 0px -50px 0px'")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)
