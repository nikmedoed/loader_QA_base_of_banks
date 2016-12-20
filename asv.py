import urllib.request
from lxml import html
import re
from datetime import datetime
import core_of_export

# from selenium import webdriver
# from lxml import etree


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
def getQA(thm, url, idn, qu):
    # print("Обрабатывается страница", thm,url, idn)
    result = []
    # my_file = open("bant.html", "w")
    # qua = open("bane.html", "w")
    # my_file.write(html.tostring(qu, method='html', encoding='utf-8').decode('utf-8'))
    # print(html.tostring(qu, method='html', encoding='cp1251').decode("cp1251"))


    # print(q[1].text_content())
    # print(len(qu))
    for q in qu:
        question = q[0].text_content().strip().replace("\u2012","-")
        answer = q[1].text_content().strip().replace("\r","").replace("\n\n","\n").replace("\t","").replace("\u2012","-")
        # print(answer)
        user = ""
        user_url = ""
        user_town = ""
        question_time = ""
        expert = "Агенство по страхованию вкладов"
        expert_url = ""
        expert_info = ""
        answer_time = ""

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

        idn+=1
        # try:
        #     my_file.write(html.tostring(q[0], method='html', encoding='cp1251').decode('cp1251')+"\n")
        #     my_file.write(html.tostring(q[1], method='html', encoding='cp1251').decode('cp1251')+"\n\n\n\n")
        # except Exception:
        #     my_file.write("Exception\n\n\n\n")
        result.append({'id': idn, 'category': thm, 'question': question, 'answer': answer,
                       'question_url':   url, 'user_name': user,
                       'user_url':  user_url,
                       'user_town': user_town, 'question_datetime': question_time,
                       'expert_name': expert, 'expert_url': expert_url, 'expert_info': expert_info,
                       'answer_time': answer_time, 'acces_date': str(datetime.now()),
                       'site': url})
        # , question.xpath('td/strong/text()[1]'))
        # ,"http://www.banki.ru"+topic.get('href')])

    # my_file.close()
    # qua.close()
    return result


# получив ссылку на раздел, узнаем сколько в нем страниц и по очреди просматриваем их, собирая базу вопрос-ответ
def QAdriver(u, nnn):
    result = []
    # my_file = open("bante.html", "w")
    # try:
    h = html.document_fromstring(urllib.request.urlopen(u[1]).read()).find_class("c_box")[1]
    # my_file.write(html.tostring(h, method='html', encoding='cp1251').decode('cp1251'))
    try:
        for i in range(len(h)//2):
            thm = u[0] + " / " + h[i*2].text_content().strip().replace("\u2012","-")
            re = getQA(thm, u[1], nnn + 1, h[i*2+1])
            nnn = re[len(re) - 1]['id']
            result.extend(re)
        if len(h) < 2:
            result = getQA(u[0], u[1], nnn + 1, h[0])
    except Exception as ex:
        thm = ""
        for i in h:
            g = i.cssselect("a.green.binline.notd.toggle")
            if len(g) > 0:
                thm = g[0].text_content().strip().replace("\u2012","-")
                # print (thm)
            elif thm != "":
                g = i.cssselect("li")
                if len(g) > 0 and len (i)==1:
                    None
                    # print(html.tostring(i[0], method='html', encoding='utf-8').decode('utf-8'))
                    if len(i[0][0]) ==0:
                        result.extend(getQA(thm, u[1], nnn, i[0][1]))
                    else:
                        result.extend(getQA(thm, u[1], nnn, i[0][0]))
                    nnn += 300
                    # text = g[0].text_content().strip()
                    # print(text)
                else:
                    None
                    # text = i.text_content().strip().replace("\t","") #superConcat(g)
                    # print(text)
                thm = ""
    # my_file.close()
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
def getQAasv(n):
    topicList = []
    pnum = 0
    n *= 100000000000
    topicList = [
        ["Гарантирование пенсий / Информация для застрахованных лиц", "http://www.asv.org.ru/pension/info_for_the_insured/"],
        ["Гарантирование пенсий / Информация для фондов-участников и ПФР", "http://www.asv.org.ru/pension/info_for_funds_committed_and_the_fiu/"],
        ["Страхование вкладов", "http://www.asv.org.ru/insurance/faq/"],
        ["Ликвидация банков", "http://www.asv.org.ru/liquidation/faq/"],
        ["Ликвидация НПФ", "http://www.asv.org.ru/liquidation-npf/faq/"],
        ["Для банков", "http://www.asv.org.ru/for_banks/faq/"]
    ]
    # print(topicList)
    # topicList = [topicList[0]]
    print("asv.org.ru - старт парсинга")
    base = []
    for tL in topicList:
        n += 100000000
        base.extend(QAdriver(tL, n))
    print("asv.org.ru - возврашена база")
    return base

# getQAasv(5)

def main():
    base = getQAasv(5)
    print (len(base),base)
    core_of_export.export(base, "ExportedFiles_ff/")
    # core_of_export.export(base)

# my_file = open("log.txt", "w")

if __name__ == '__main__':
    # multiprocessing.freeze_support()
    main()
