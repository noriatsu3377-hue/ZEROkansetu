import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract header from index.html
header_match = re.search(r'(.*?<main>)', index_html, re.DOTALL)
header = header_match.group(1) if header_match else ""

with open('pricing.html', 'r', encoding='utf-8') as f:
    pricing_html = f.read()

# Current pricing.html starts with <!-- Subpage Header -->
# But it has the footer at the bottom.
# Let's extract just the content between Subpage Header and the footer.
content_match = re.search(r'(    <!-- Subpage Header -->.*?</section>)', pricing_html, re.DOTALL)
content = content_match.group(1) if content_match else ""

footer_match = re.search(r'(<footer class="site-footer">.*)', index_html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

final_html = f"""{header}
{content}
    </main>
{footer}
"""

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

