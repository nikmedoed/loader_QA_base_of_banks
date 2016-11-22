import lxml.html
import urllib.request
# подключили библиотеку

page = urllib.request.urlopen("file:///E:/Downloads/bank.html")
p = page.read()
doc = lxml.html.document_fromstring(p)
# Получили HTML-документ со строки

txt1 = doc.xpath('/html/body/span[@class="simple_text"]/text()[1]')
# Находим тег «span», у которого аттрибут «class» равен значению «simple_text» и с помощью функции text() получаем текст элемента
txt2 = doc.xpath('/html/body/span[@class="cyrillic_text"]/following-sibling::text()[1]')
# Находим тег «span», у которого аттрибут «class» равен значению «cyrillic_text» и получаем следующий за ним текст с помощью following-sibling (получаем следующий в ветке элемент) и text()
# Для получение значений использовался XPath

print(txt2)