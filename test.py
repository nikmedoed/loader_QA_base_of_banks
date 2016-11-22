import urllib.request
# подключили библиотеку urllib
from lxml import html
# подключили библиотеку lxml
from lxml import cssselect
page = urllib.request.urlopen("http://habrahabr.ru/")
# Открываем наш любимый Хабр

doc = html.document_fromstring(page.read())
# Получили HTML-код главной страницы Хабра

for topic in doc.cssselect('h2.post__title a.post__title_link'):
    print (topic.get('href'))
    print (topic.text)

# выводим на экран названия топиков.
