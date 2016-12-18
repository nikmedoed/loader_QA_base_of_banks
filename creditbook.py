import urllib.request
from lxml import html
import re
from datetime import datetime

# from selenium import webdriver
# from lxml import etree


# получаем общий список разделов из главной страницы
def getListOfthemes():
    start = [
        [0, "Кредиты", "http://creditbook.ru/otvety/kredity"],
        [1, "Кредитные карты", "http://creditbook.ru/otvety/banki"],
        [2, "Ипотека", "http://creditbook.ru/otvety/avtokredit"],
        [3, "Автокредит", "http://creditbook.ru/otvety/ipoteka"],
        [5, "Банки", "http://creditbook.ru/otvety/kreditnye-karty"]
    ]
    result = []
    u = urllib.request.urlopen(start[0][2])
    data = u.read()
    h = html.document_fromstring(data).get_element_by_id('swrCatsContent')[0]

    # my_file = open("bant.html", "w")

    # my_file.write(html.tostring(h, method='html', encoding='utf-8').decode('utf-8'))
    for topic in start:
        # my_file.write(html.tostring(h[topic[0]], method='html', encoding='utf-8').decode('utf-8') + "\n\n")
        for s in h[topic[0]]:
            result.append([topic[1] + " / " + ' '.join(s.text_content().split()), "http://creditbook.ru" + s[0].get('href')])

    print(result)
    # my_file.close()
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
        text = (text.decode("cp1251")).replace("<br>", "\n").replace("</a>", "") \
            .replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "")\

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
            result += "\n" + text
        else:
            result += text
            l += 1
    # print (result+"\n---------------------------------------\n")
    return result


# из очередной страницы вопросов выделяем все вопросы с ответами
def getQA(thm, url, idn):
    print("Обрабатывается страница", thm,url, idn)
    q = html.document_fromstring(urllib.request.urlopen(url).read()).find_class("answer_all")[0]
    result = []

    # my_file = open("bant.html", "w")
    # qua = open("bane.html", "w")
    # my_file.write(html.tostring(q, method='html', encoding='utf-8').decode('utf-8'))
    # print(html.tostring(qu.getchildren()[0], method='html', encoding='cp1251').decode("cp1251"))

    question = q[1].text_content().strip()
    # print(q[1].text_content())
    answer = superConcat(q[2][1][1]).replace("\xa0"," ")
    user = ""
    user_url = ""
    user_town = ""
    question_time = q[0][1].text_content().strip()
    expert = q[2][1][0][0][0].text_content().strip()
    expert_url = ""
    expert_info = q[2][1][0][0][1].text_content().strip()
    answer_time =  q[2][4].text_content().strip()

    # qua.write("\tВопрос:\n"+question+"\n\n")
    # qua.write("\tОтвет:\n"+answer+"\n\n")
    # qua.write("\tПользователь:\n"+user+"\n\n")
    # qua.write("\tСсылка на пользователя:\n"+user_url+"\n\n")
    # qua.write("\tГород пользователя:\n"+user_town+"\n\n")
    # qua.write("\tПостоянный адрес:\n"+url+"\n\n")
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
    result.append({'id': idn, 'category': thm, 'question': question, 'answer': answer,
                   'question_url': "http://creditbook.ru/" + url, 'user_name': user,
                   'user_url': "http://www.banki.ru" + user_url,
                   'user_town': user_town, 'question_datetime': question_time,
                   'expert_name': expert, 'expert_url': expert_url, 'expert_info': expert_info,
                   'answer_time': answer_time, 'acces_date': str(datetime.now()),
                   'site': "http://creditbook.ru/otvety/"})
    # , question.xpath('td/strong/text()[1]'))
    # ,"http://www.banki.ru"+topic.get('href')])

    # my_file.close()
    # qua.close()
    return result


# получив ссылку на раздел, узнаем сколько в нем страниц и по очреди просматриваем их, собирая базу вопрос-ответ
def QAdriver(u, nnn):
    result = []
    try:
        h = html.document_fromstring(urllib.request.urlopen(u[1]).read()).find_class('filter_number')
        if len(h) > 1:
            l = len(h[1][1])
        else:
            l = 1
        for i in range(l):
            h = html.document_fromstring(urllib.request.urlopen(u[1] + "/start/" + str(i+1)).read()).cssselect("div.question")
            for htm in h:
                nnn += 1
                result.append(getQA(u[0] + " / "+ ' '.join(htm.text_content().split()),
                      "http://creditbook.ru" + htm[0].get('href'), nnn))
    except Exception as ex:
        print("creditbook.ru ошибос:", ex)
    return result


'''
print(topicList)
print(len(topicList))
my_file = open("ban.html","w")
my_file.write(data.decode('cp1251'))
my_file.close()
topicList = [["БАНКРОТСТВО БАНКОВ", "http://www.banki.ru/services/questions-answers/?id=4826772"]]
'''

#TODO параллельная загрузка
# возвращает список словарей - ответов. получает номер сайта для формирвоания ID вопроса-ответа в формате:
# 2 символна на сайт,
# 3 символа на раздел,
# 8 символов на номер вопроса
def getQAcreditbook(n):
    topicList = []
    pnum = 0
    n *= 100000000000
    topicList = getListOfthemes()
    # print(topicList)
    # topicList = [topicList[0]]
    print("creditbook.ru - получен спискок тем / старт парсинга")
    base = []
    for tL in topicList:
        n += 100000000
        base.extend(QAdriver(tL, n))
    print("creditbook.ru - возврашена база")
    return base