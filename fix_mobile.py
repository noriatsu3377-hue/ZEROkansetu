with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add body overflow-x hidden
if 'overflow-x: hidden;' not in css[:500]:
    css = css.replace('body {\n', 'body {\n    overflow-x: hidden;\n')
    css = css.replace('html {\n', 'html {\n    overflow-x: hidden;\n')

# Fix min-width for diff-table on mobile
fix_css = """
@media (max-width: 768px) {
    .comparison-table.diff-table {
        min-width: 100% !important;
    }
}
"""
css += fix_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

