import requests
from lxml import html
import re
from datetime import datetime
import urllib.request
# from selenium import webdriver
# from lxml import etree


def getSubListOfthemes(m, n, ou):
    result = []
    requests.packages.urllib3.disable_warnings()
    u = requests.api.request('post', ou, data={'bar': 'baz'}, json=None, verify=False).text
    h = html.document_fromstring(u).find_class('cloud2')[0]
    # print(html.tostring(h, method='html', encoding='cp1251').decode("cp1251"))
    h=h.getchildren()
    if len(h) > 1:
        if h[0].text is None:
            main = m + " - " + n
        else:
            main = m + " - " + h[0].text
        for sub in h[1].getchildren():
            result.append([main + " - " + sub.getchildren()[0].text, sub.getchildren()[0].get('href')])
    # print(result)
    return result


# получаем общий список разделов из главной страницы
def getListOfthemes():
    result = []
    #headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')}
    #u = requests.get("https://ff.ru/ask/", verify=False)
    #print(u)
    #u = urllib.request.urlopen(urllib.request.Request(url="https://ff.ru/ask/", headers=headers))
    #print(u)
    #.read()
    requests.packages.urllib3.disable_warnings()
    u = requests.api.request('post', "https://ff.ru/ask/", data={'bar':'baz'}, json=None, verify=False).text
    h = html.document_fromstring(u).find_class('category') # [0].getchildren()[0].getchildren()
    del (h[0])
    for el in h:
        el = el.getchildren()
        main = el[0].text
        print("ФедФин бюро - список ссылок - категория:", main)
        for sub in el[1].getchildren():
            name = sub.getchildren()[0].text
            url = sub.getchildren()[0].get('href')
            result.append([main + " - " + name + " - Общая", url])
            result.extend(getSubListOfthemes(main, name, url))
    # browser = webdriver.Chrome()
    # browser.get("https://ff.ru/ask/")
    # l = browser.find_elements_by_class_name('category')
    # for k in l:
    #   print(k.text)
    # #print (browser.page_source)
    # browser.close()
    #print(u.text)
    # data = u.read()
    # h = html.document_fromstring(data).find_class('category') #[0].getchildren()[0].getchildren()
    # print(html.tostring(h, method='html', encoding='cp1251').decode("cp1251"))

    # for topic in h[0].getchildren():
    #     to = topic.getchildren()[0].getchildren()[0]
    #     # print(html.tostring(to, method='html', encoding='cp1251').decode("cp1251"))
    #     result.append([to.text_content().replace("\xa0"," "), "http://www.cbr.ru" + to.get('href')])
    # for topic in h[1].getchildren():
    #     to = topic.getchildren()[0].getchildren()[0]
    #     result.append([to.text_content().replace("\xa0"," "), "http://www.cbr.ru" + to.get('href')])
    # print(result)
    return result


def detQL(url, p, n):
    requests.packages.urllib3.disable_warnings()
    print(url, p, n)
    data = requests.api.request('post', url[1]+str(p), data={'bar': 'baz'}, json=None, verify=False).text
    h = html.document_fromstring(data).find_class('no-questions')
    if len(h) > 0:
        return []
    else:
        rk = detQL(url, p+1, n+8)
        t = html.document_fromstring(data).find_class('questions')[0].getchildren()
        temp = map(lambda x: [url[0], "https://ff.ru" + x.getchildren()[1].getchildren()[0].get('href')], t)
        k = list(zip(temp, [i for i in range(n, n+len(t))]))
        k.extend(rk)
        return k


def getQuestionList(url):
    return detQL([url[0][0],url[0][1]+"?page="], 1, url[1]+1)


# из очередной страницы вопросов выделяем все вопросы с ответами
def getQuestion(url):
    idn = url[1]
    url = url[0]
    print("Обрабатывается страница", url, idn)
    requests.packages.urllib3.disable_warnings()
    data = requests.api.request('post', url[1], data={'bar':'baz'}, json=None, verify=False).text
    q = html.document_fromstring(data).find_class('question')[0]
    qs = q.getchildren()
    a = html.document_fromstring(data).find_class('answer')[0].getchildren()
    result = []
    # qua = open("bane.html", "a")

    # print(html.tostring(qu, method='html', encoding='cp1251').decode("cp1251"))
    # print(html.tostring(q[2], method='html', encoding='cp1251').decode("cp1251"))

    question = qs[0].text_content().replace("Вопрос:","") + "\n" + qs[1].text_content()
    answer = a[1].getchildren()[0].getchildren()[1].text_content()
    question_url = url[1]
    user = "недоступно"
    user_url = ""
    ut = q.cssselect('time')[0].text
    if  len(ut) == 10:
        user_town = ""
    else:
        user_town = re.sub(".*\..*\..*\s", "", ut)
    question_time = re.sub("\+.*", "", q.cssselect('meta')[0].get('content').replace("T", " "))
    expert = a[1].getchildren()[0].getchildren()[0].getchildren()[0].text
    expert_url = a[1].getchildren()[0].getchildren()[0].getchildren()[0].get("href")
    expert_info = a[1].getchildren()[0].getchildren()[0].getchildren()[1].text_content()
    answer_time = re.sub("\+.*", "", a[3].getchildren()[1].text)
    # idn += 1

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

    result.append({'id': idn, 'category': url[0], 'question': question, 'answer': answer,
                   'question_url': question_url, 'user_name': user, 'user_url':  user_url,
                   'user_town': user_town, 'question_datetime': question_time,
                   'expert_name': expert, 'expert_url': expert_url, 'expert_info': expert_info,
                   'answer_time': answer_time, 'acces_date': str(datetime.now()), 'site': "https://ff.ru/ask/"})


    # qua.close()
    return result


#TODO удаление повторяющихся вопросов


#TODO параллельная загрузка
# возвращает список словарей - ответов. получает номер сайта для формирвоания ID вопроса-ответа в формате:
# 2 символна на сайт,
# 3 символа на раздел,
# 8 символов на номер вопроса
def getQAff(n):
    print("ФедФин бюро - получен спискок тем / старт парсинга")
    n *= 100000000000
    topicList = []
    for t in getListOfthemes():
        topicList.append([t, n])
        n += 100000000
    banki_ru_base = []
    # for l in map(getQuestionList, topicList):
    #     for el in l:
    #         banki_ru_base.append(getQuestion(el))
    for k in list(map(lambda x: list(map(getQuestion, x)), map(getQuestionList, topicList))):
        banki_ru_base.extend(k)
    print("ФедФин бюро - возврашена база")
    return banki_ru_base

# print(getQuestion([["Супертема","https://ff.ru/ask/26768/"],464564641313]))
# print(getListOfthemes())
#
#
# topicList = [(["Кредиты", "https://ff.ru/asks/202-invalidu/"],1000000000),
#              (["бизнес","https://ff.ru/asks/9-na_biznes/"],2000000000)]
# banki_ru_base = []
# for k in list(map(lambda x: list(map(getQuestion, x)), map(getQuestionList, topicList))):
#     banki_ru_base.extend(k)
# print(banki_ru_base)
#

getQAff(3)