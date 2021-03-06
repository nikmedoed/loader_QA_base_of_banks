import urllib.request
from lxml import html
import re
from datetime import datetime
import core_of_export
from multiprocessing import Process

# from selenium import webdriver
# from lxml import etree


# получаем общий список разделов из главной страницы
def getListOfthemes(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    h = html.document_fromstring(data)
    result = []
    for topic in h.cssselect('h3.widget__title a'):
        if topic.get('href') != "/":
            result.append([topic.text, "http://www.banki.ru" + topic.get('href')])
    return result


# из блока вопрос или ответ получаем текс с переносами строк и вписанными ссылками
def superConcat(t):
    # print(str(len(t)) + " : " + t[0].text)
    # data = html.tostring(t, method='html', encoding='cp1251').decode("cp1251")
    # print(html.tostring(t, method='html', encoding='cp1251').decode("cp1251"))
    result = ""
    l = 0
    for s in t:
        # Заменяем <br> на  \n
        # print(s.text_content())
        text = html.tostring(s, method='html', encoding='cp1251')
        text = (text.decode("cp1251")).replace("<br>", "\n").replace("<p>", "").replace("</p>", "").replace("</a>", "")
        text = re.sub("<a.*href.*\">", "", text)
        # print(text)
        # print("\n")
        # s = html.document_fromstring(text).text_content()
        # print(s)
        # print(s[0].text)
        # # выдергиваем ссылки
        # text = html.tostring(s, method='html', encoding='cp1251')
        # #получаем итоговый текст
        # text = text.text
        if l > 0:
            result += "\n\n" + text
        else:
            result += text
            l += 1
    # print (result+"\n---------------------------------------\n")
    return result

def test(s):
    if s is None:
        return "???"
    else:
        return s


# из очередной страницы вопросов выделяем все вопросы с ответами
def getQuestionList(url, idn):
    u = urllib.request.urlopen(url[1])
    # print("Обрабатывается страница", url, idn)
    data = u.read()
    h = html.document_fromstring(data)
    result = []
    # my_file = open("bant.html", "w")
    # qua = open("bane.html", "a")

    for qu in h.find_class('qaBlock'):
        try:
            q = qu.getchildren()
            # print(html.tostring(qu.getchildren()[0], method='html', encoding='cp1251').decode("cp1251"))
            if len(q) > 1:  # если есть ответы
                question = superConcat(q[0].getchildren()[1].getchildren()[0]).replace("\xa0"," ")
                answer = superConcat(q[1].getchildren()[1].getchildren()[0]).replace("\xa0"," ")
                question_url = q[0].getchildren()[1].getchildren()[1].getchildren()[0].get('href')
                user =' '.join( q[0].getchildren()[1].getchildren()[2].text.strip().split())
                user_url = q[0].getchildren()[1].getchildren()[2].getchildren()[0].get('href')
                user_town = re.sub("\n.*", "", re.sub(".*\n.*\n.*\n", "", q[0].getchildren()[1].getchildren()[
                    2].text_content()).replace("(","").replace(")","").strip()).strip()
                question_time = re.sub("\n.*", "", re.sub(".*\n.*\n.*\n.*", "", q[0].getchildren()[1].getchildren()[
                    2].text_content()).lstrip()).rstrip()
                try:
                    expert = q[1].getchildren()[1].getchildren()[1].text_content().strip()
                except:
                    expert = ""
                expert_url = ""
                expert_info = ""
                answer_time = ""
                idn += 1
                # qua.write("\tВопрос:\n"+question+"\n\n")
                # qua.write("\tОтвет:\n"+answer+"\n\n")
                # qua.write("\tПользователь:\n"+user+"\n\n")
                # qua.write("\tСсылка на пользователя:\n"+user_url+"\n\n")
                # qua.write("\tГород пользователя:\n"+user_town+"\n\n")
                # qua.write("\tПостоянный адрес:\n"+question_url+"\n\n")
                # qua.write("\tВремя вопроса:\n"+question_time+"\n\n")
                # qua.write("\tЭксперт:\n"+expert+"\n\n")
                # qua.write("\tСсылка на эксперта:\n"+expert_url+"\n\n")
                # qua.write("\tИнфо об эксперте:\n"+expert_info+"\n\n")
                # qua.write("\tВремя ответа:\n"+answer_time+"\n\n")
                # qua.write("\n------------------------------\n")

                # try:
                #     my_file.write(html.tostring(q[0], method='html', encoding='cp1251').decode('cp1251')+"\n")
                #     my_file.write(html.tostring(q[1], method='html', encoding='cp1251').decode('cp1251')+"\n\n\n\n")
                # except Exception:
                #     my_file.write("Exception\n\n\n\n")
                # result.append \
                QA = {'id': idn, 'category': url[0], 'question': question, 'answer': answer,
                               'question_url': "http://www.banki.ru" + question_url, 'user_name': user,
                               'user_url': "http://www.banki.ru" + test(user_url),
                               'user_town': user_town, 'question_datetime': question_time,
                               'expert_name': expert, 'expert_url': expert_url, 'expert_info': expert_info,
                               'answer_time': answer_time, 'acces_date': str(datetime.now()),
                               'site': "http://www.banki.ru/services/questions-answers/"}
                # Process(target=core_of_export.exportOne, args=(QA,ourway)).start() -------------для параллельной записи. Тормозит--------------
                core_of_export.exportOne(QA,ourway)
                # , question.xpath('td/strong/text()[1]'))
                # ,"http://www.banki.ru"+topic.get('href')])
        except Exception as ex:
            print("банки ру ошибос:", ex, url , user_url)

        # print("банки ру - страница обработана:", url, idn)
    # my_file.close()
    # qua.close()
    return idn


# получив ссылку на раздел, узнаем сколько в нем страниц и по очреди просматриваем их, собирая базу вопрос-ответ
def QAdriver(u, nnn):
    # print(u)
    result = []
    # browser = webdriver.Chrome()
    try:
        # browser.get("http://www.banki.ru/services/questions-answers/?id=4826772&p=1")
        # l = browser.find_element_by_class_name('v-margins').get_attribute("data-options")
        # print(eval(l))
        # #print (browser.page_source)
        # h = html.document_fromstring(browser.page_source)
        # browser.close()
        # k = 0
        # print(html.tostring(h, method='html', encoding='cp1251').decode("cp1251"))

        h = html.document_fromstring(urllib.request.urlopen(u[1]).read())
        l = h.find_class('v-margins')[0].get('data-options')
        if l is None:
            l = 1
        else:
            l = l.split('; ')
            l = round(float(l[2].split(': ')[1]) / float(l[1].split(': ')[1]) + 0.5)
        print(u[0], u[1], "Страниц:", l)
        # print(l)
        # print(html.tostring(l, method='html', encoding='cp1251').decode("cp1251"))
        # l = l[len(l)-2].getchildren()[0].text
        # print (l)

        for n in range(l):
            re = getQuestionList([u[0], u[1] + "?p=" + str(n)], nnn)
            nnn = re #[len(re) - 1]['id']
            # result.extend(re)
    except Exception as ex:
        print("банки ру ошибос:", ex)
        # if k:
        #     browser.close()
    print("банки ру - обработано:", u, nnn)
    return result


'''
print(topicList)
print(len(topicList))
my_file = open("ban.html","w")
my_file.write(data.decode('cp1251'))
my_file.close()
topicList = [["БАНКРОТСТВО БАНКОВ", "http://www.banki.ru/services/questions-answers/?id=4826772"]]
'''


# возвращает список словарей - ответов. получает номер сайта для формирвоания ID вопроса-ответа в формате:
# 2 символна на сайт,
# 3 символа на раздел,
# 8 символов на номер вопроса
def getQAbankiru(n):
    topicList = []
    pnum = 0
    n *= 100000000000
    while True:  # ! может затупить
        pnum += 1
        r = getListOfthemes("http://www.banki.ru/services/questions-answers/?p=" + str(pnum))
        if r == []:
            break
        else:
            topicList.extend(r)
    # print(topicList)
    # topicList = [topicList[0]]
    print("банки.ру - получен спискок тем / старт парсинга")
    banki_ru_base = []
    for tL in topicList:
        n += 100000000
        # QAdriver(tL, n)
        Process(target=QAdriver, args=(tL, n)).start()
    print("банки.ру - паралельная выгрузка пошла")
    return banki_ru_base


ourway = "E:/clouds/MailCloud/ExportedFiles_banki/"


def main():
    getQAbankiru(1)

if __name__ == '__main__':
    # multiprocessing.freeze_support()
    main()