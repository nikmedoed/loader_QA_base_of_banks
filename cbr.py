import urllib.request
from lxml import html
import re
from datetime import datetime
import core_of_export
from multiprocessing import Process
# from selenium import webdriver
# from lxml import etree


# получаем общий список разделов из главной страницы
def getListOfthemes():
    result = []
    u = urllib.request.urlopen("http://www.cbr.ru/IReception/?PrtId=answer")
    data = u.read()
    h = html.document_fromstring(data).find_class('inner_menu with_bottom_shadow no_visited cols_2'
                                                  )[0].getchildren()[0].getchildren()
    for topic in h[0].getchildren():
        to = topic.getchildren()[0].getchildren()[0]
        # print(html.tostring(to, method='html', encoding='cp1251').decode("cp1251"))
        result.append([to.text_content().replace("\xa0"," "), "http://www.cbr.ru" + to.get('href')])
    for topic in h[1].getchildren():
        to = topic.getchildren()[0].getchildren()[0]
        result.append([to.text_content().replace("\xa0"," "), "http://www.cbr.ru" + to.get('href')])
    # print(result)
    return result


# из блока вопрос или ответ получаем текс с переносами строк и вписанными ссылками
def superConcat(t):
    result = html.tostring(t, method='html', encoding='cp1251')
    result = (result.decode("cp1251")).replace("<br>", "\n").replace("<p>", "").replace("</p>", "").replace("</a>", "")
    result = re.sub("<div.*>","",re.sub("<a.*href.*\">", "", result.replace("</div>", "")))
    # print(str(len(t)) + " : " + t[0].text)
    # data = html.tostring(t, method='html', encoding='cp1251')
    # print (data.decode("cp1251"))
    return result


# из очередной страницы вопросов выделяем все вопросы с ответами
def getQuestionList(url, idn):
    u = urllib.request.urlopen(url[1])
    print("Обрабатывается страница", url, idn)
    data = u.read()
    h = html.document_fromstring(data).find_class('question')
    result = []
    try:
        for qu in h:
            q = qu.getchildren()
            # print(html.tostring(qu, method='html', encoding='cp1251').decode("cp1251"))
            # print(html.tostring(q[2], method='html', encoding='cp1251').decode("cp1251"))
            question = q[1].text_content()
            answer = superConcat(q[2])
            question_url = url[1] + q[1].get('href')
            user = "недоступно"
            user_url = ""
            user_town = ""
            question_time = "actual"
            expert = "ЦБ РФ"
            expert_url = ""
            expert_info = ""
            answer_time = ""
            idn += 1

            # result.append \
            QA = ({'id': idn, 'category': url[0], 'question': question, 'answer': answer,
                           'question_url': question_url, 'user_name': user, 'user_url':  user_url,
                           'user_town': user_town, 'question_datetime': question_time,
                           'expert_name': expert, 'expert_url': expert_url, 'expert_info': expert_info,
                           'answer_time': answer_time,'acces_date': str(datetime.now()),
                           'site': "http://www.cbr.ru/Reception/Faq/"})

            # Process(target=core_of_export.exportOne, args=(QA,)).start() # ----- параллельная запись, аккуратнее
            core_of_export.exportOne(QA)
    except Exception as ex:
        print("cbr.ru ошибос:", ex)
    return result


# возвращает список словарей - ответов. получает номер сайта для формирвоания ID вопроса-ответа в формате:
# 2 символна на сайт,
# 3 символа на раздел,
# 8 символов на номер вопроса
def getQAcbr(n):
    topicList = getListOfthemes()
    n *= 100000000000
    print(topicList)
    print("ЦБ РФ - получен спискок тем / старт парсинга")
    # topicList = [topicList[0]]
    banki_ru_base = []
    for tL in topicList:
        n += 100000000
        Process(target=getQuestionList, args=(tL, n)).start()
        # banki_ru_base.extend(getQuestionList(tL, n))
    print("ЦБ РФ - пошла параллельная загрузка")
    return banki_ru_base

def main():
    getQAcbr(2)

if __name__ == '__main__':
    # multiprocessing.freeze_support()
    main()