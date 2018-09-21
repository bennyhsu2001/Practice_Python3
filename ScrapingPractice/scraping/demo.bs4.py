from bs4 import BeautifulSoup
html_doc = """

<div id="div1">
  <h2 id="myH" class="s1" title="hello">Hello BeautifulSoup1</h2>
  <h2 id="myH" class="s1" title="hello">Hello BeautifulSoup2</h2>
  <h2 id="myH" class="s1" title="hello">Hello BeautifulSoup3</h2>
</div>
<div id="div2">
  <h2 id="myH" class="s1" title="hello">Hello BeautifulSoup4</h2>
  <h2 id="myH" class="s1" title="hello">Hello BeautifulSoup5</h2>
</div>
"""

soup = BeautifulSoup(html_doc,"lxml")
# print(soup)
# tag = soup.h2
# print(tag["id"])
# print(tag["class"])
# print(tag.attrs)
# print(tag.string)
hs = soup.find_all("h2","title=True")
print(hs)
# for h in hs:
#     print(h.string)

# hs = soup.select("#div2 h2")
# for h in hs:
#     print(h.string)