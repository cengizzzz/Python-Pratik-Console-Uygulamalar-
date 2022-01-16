from bs4 import BeautifulSoup
html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Sayfa</title>
</head>
<body>
    <h1>Python Kursu</h1>
    <div class="1">
        <h1>Programlama</h1>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </div>
    <div class="2">
        <h1>Modüller</h1>
        <li>Menü 1</li>
        <li>Menü 2</li>
        <li>Menü 3</li>
    </div>
</body>
</html>
"""

from bs4.builder import HTMLTreeBuilder

soup=BeautifulSoup(html_doc,"html.parser")

result=soup.prettify()
result=soup.title
result=soup.head
result=soup.find_all("li")[2]
result=soup.findChild("div")
print(result)