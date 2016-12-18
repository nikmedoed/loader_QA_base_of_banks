import banki
import cbr
import ff
import creditbook
import asv
from multiprocessing import Process
from threading import Thread

def hdr_write (place, f, qa):
    file = open("ExportedFiles/qa"+ f + ".hdr", "w")
    file.write('MRM_id' + " = " + str(qa['id'] % 100000000*2 + qa['id']) + "\n")
    file.write('MRM_QA_id' + " = " + str(qa['id']) + "\n")
    file.write('MRM_doc' + " = qa" + str(qa['id']) + "\n")
    file.write('MRM_type' + " = QA\n")
    file.write('MRM_site' + " = " + str(qa['site']) + "\n")
    file.write('MRM_category' + " = " + str(qa['category']) + "\n")
    file.write('MRM_question_url' + " = " + str(qa['question_url']) + "\n")
    file.write('MRM_user_name' + " = " + str(qa['user_name']) + "\n")
    file.write('MRM_user_url' + " = " + str(qa['user_url']) + "\n")
    file.write('MRM_user_town' + " = " + str(qa['user_town']) + "\n")
    file.write('MRM_question_datetime' + " = " + str(qa['question_datetime']) + "\n")
    file.write('MRM_expert_name' + " = " + str(qa['expert_name']) + "\n")
    file.write('MRM_expert_url' + " = " + str(qa['expert_url']) + "\n")
    file.write('MRM_expert_info' + " = " + str(qa['expert_info']) + "\n")
    file.write('MRM_answer_time' + " = " + str(qa['answer_time']) + "\n")
    file.write('MRM_acces_date' + " = " + str(qa['acces_date']) + "\n")
    file.write('MRM_snippet' + " = Question: " + str(qa['question']).replace("\n", "\t") +
               ' <NOMORPH><FONT="GREY">Answer: ' +
               str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "\t") + '</FONT></NOMORPH>')
    file.close()


def hdr_write_q (f, qa):
    file = open("ExportedFiles/questions/q" + f + ".hdr", "w")
    file.write('MRM_id' + " = " + str(qa['id'] % 100000000*2 - 1 + qa['id']) + "\n")
    file.write('MRM_QA_id' + " = " + str(qa['id']) + "\n")
    file.write('MRM_doc' + " = q" + str(qa['id']) + "\n")
    file.write('MRM_type' + " = Q\n")
    file.write('MRM_site' + " = " + str(qa['site']) + "\n")
    file.write('MRM_category' + " = " + str(qa['category']) + "\n")
    file.write('MRM_question_url' + " = " + str(qa['question_url']) + "\n")
    file.write('MRM_user_name' + " = " + str(qa['user_name']) + "\n")
    file.write('MRM_user_url' + " = " + str(qa['user_url']) + "\n")
    file.write('MRM_user_town' + " = " + str(qa['user_town']) + "\n")
    file.write('MRM_question_datetime' + " = " + str(qa['question_datetime']) + "\n")
    file.write('MRM_acces_date' + " = " + str(qa['acces_date']) + "\n")
    file.write('MRM_snippet' + " = Question: " + str(qa['question']).replace("\n", "\t") +
               ' <NOMORPH><FONT="GREY">Answer: ' +
               str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "\t") + '</FONT></NOMORPH>')
    file.close()


def hdr_write_a (f, qa):
    file = open("ExportedFiles/answers/a"+ f + ".hdr", "w")
    file.write('MRM_id' + " = " + str(qa['id'] % 100000000*2 - 2 + qa['id']) + "\n")
    file.write('MRM_QA_id' + " = " + str(qa['id']) + "\n")
    file.write('MRM_doc' + " = a" + str(qa['id']) + "\n")
    file.write('MRM_type' + " = A\n")
    file.write('MRM_site' + " = " + str(qa['site']) + "\n")
    file.write('MRM_category' + " = " + str(qa['category']) + "\n")
    file.write('MRM_user_name' + " = " + str(qa['user_name']) + "\n")
    file.write('MRM_user_url' + " = " + str(qa['user_url']) + "\n")
    file.write('MRM_user_town' + " = " + str(qa['user_town']) + "\n")
    file.write('MRM_question_url' + " = " + str(qa['question_url']) + "\n")
    file.write('MRM_expert_name' + " = " + str(qa['expert_name']) + "\n")
    file.write('MRM_expert_url' + " = " + str(qa['expert_url']) + "\n")
    file.write('MRM_expert_info' + " = " + str(qa['expert_info']) + "\n")
    file.write('MRM_answer_time' + " = " + str(qa['answer_time']) + "\n")
    file.write('MRM_acces_date' + " = " + str(qa['acces_date']) + "\n")
    file.write('MRM_snippet' + ' = <NOMORPH><FONT="GREY">Question: ' + str(qa['question']).replace("\n", "\t") +
               '</FONT></NOMORPH> Answer: ' + str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "\t"))
    file.close()


def htm_write (f, qa):
    file = open("ExportedFiles/qa" + f + ".htm", "w")
    style1column = "style=\"text-align: right;font-weight: bold\""
    style2column = ""
    styletable = "border=\"1\" style=\"color:gray\""
    file.write("<NOMORPH>\n<FONT COLOR=\"GRAY\"><I>\n<table " + styletable + ">\n")
    file.write("<tr><td " + style1column + " >id</td><td " + style2column + " >" + str(qa['id']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >site</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['site']) + "\">" + str(qa['site']) + "</a></td></tr>\n")
    file.write(
        "<tr><td " + style1column + " >category</td><td " + style2column + " >" + str(qa['category']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >question_url</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['question_url']) + "\">" + str(qa['question_url']) + "</a></td></tr>\n")
    file.write("<tr><td " + style1column + " >user_name</td><td " + style2column + " >" + str(
        qa['user_name']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >user_url</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['user_url']) + "\">" + str(qa['user_url']) + "</a></td></tr>\n")
    file.write("<tr><td " + style1column + " >user_town</td><td " + style2column + " >" + str(
        qa['user_town']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >question_datetime</td><td " + style2column + " >" + str(
        qa['question_datetime']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >expert_name</td><td " + style2column + " >" + str(
        qa['expert_name']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >expert_url</td><td " + style2column + " >" + str(
        qa['expert_url']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >expert_info</td><td " + style2column + " >" + str(
        qa['expert_info']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >answer_time</td><td " + style2column + " >" + str(
        qa['answer_time']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >acces_date</td><td " + style2column + " >" + str(
        qa['acces_date']) + "</td></tr>\n")
    file.write("</table></I></FONT>\n</NOMORPH>\n&nbsp\n<div>")
    file.write("<b>Вопрос:</b><p>" + str(qa['question']).replace("\n", "<br>") + "</p>\n")
    file.write("<b>Ответ:</b><p>" + str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "<br>")
               + "</p>")
    file.write("</div>")
    file.close()


def htm_write_a (f, qa):
    file = open("ExportedFiles/answers/a" + f + ".htm", "w")
    style1column = "style=\"text-align: right;font-weight: bold\""
    style2column = ""
    styletable = "border=\"1\" style=\"color:gray\""
    file.write("<NOMORPH>\n<FONT COLOR=\"GRAY\"><I>\n<table " + styletable + ">\n")
    file.write("<tr><td " + style1column + " >id</td><td " + style2column + " >" + str(qa['id']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >site</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['site']) + "\">" + str(qa['site']) + "</a></td></tr>\n")
    file.write(
        "<tr><td " + style1column + " >category</td><td " + style2column + " >" + str(qa['category']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >question_url</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['question_url']) + "\">" + str(qa['question_url']) + "</a></td></tr>\n")
    file.write("<tr><td " + style1column + " >expert_name</td><td " + style2column + " >" + str(
        qa['expert_name']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >expert_url</td><td " + style2column + " >" + str(
        qa['expert_url']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >expert_info</td><td " + style2column + " >" + str(
        qa['expert_info']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >answer_time</td><td " + style2column + " >" + str(
        qa['answer_time']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >acces_date</td><td " + style2column + " >" + str(
        qa['acces_date']) + "</td></tr>\n")
    file.write("</table></I></FONT>\n</NOMORPH>\n&nbsp\n")
    file.write("<NOMORPH><FONT COLOR=\"GRAY\"><i><b>Вопрос:</b><p>" + str(qa['question']).replace("\n", "<br>") +
               "</p></i></FONT></NOMORPH>\n")
    file.write("<div><b>Ответ:</b><p>" + str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "<br>")
               + "</p>")
    file.write("</div>")# + "\n")
    file.close()


def htm_write_q (f, qa):
    file = open("ExportedFiles/questions/q" + f + ".htm", "w")
    style1column = "style=\"text-align: right;font-weight: bold\""
    style2column = ""
    styletable = "border=\"1\" style=\"color:gray\""
    file.write("<NOMORPH>\n<FONT COLOR=\"GRAY\"><I>\n<table " + styletable + ">\n")
    file.write("<tr><td " + style1column + " >id</td><td " + style2column + " >" + str(qa['id']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >site</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['site']) + "\">" + str(qa['site']) + "</a></td></tr>\n")
    file.write(
        "<tr><td " + style1column + " >category</td><td " + style2column + " >" + str(qa['category']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >question_url</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['question_url']) + "\">" + str(qa['question_url']) + "</a></td></tr>\n")
    file.write("<tr><td " + style1column + " >user_name</td><td " + style2column + " >" + str(
        qa['user_name']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >user_url</td><td " + style2column + " >" + "<a href=\"" + str(
        qa['user_url']) + "\">" + str(qa['user_url']) + "</a></td></tr>\n")
    file.write("<tr><td " + style1column + " >user_town</td><td " + style2column + " >" + str(
        qa['user_town']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >question_datetime</td><td " + style2column + " >" + str(
        qa['question_datetime']) + "</td></tr>\n")
    file.write("<tr><td " + style1column + " >acces_date</td><td " + style2column + " >" + str(
        qa['acces_date']) + "</td></tr>\n")
    file.write("</table></I></FONT>\n</NOMORPH>\n&nbsp\n<div>")
    file.write("<div><b>Вопрос:</b><p>" + str(qa['question']).replace("\n", "<br>") + "</p>")
    file.write("</div>")
    file.write("<br><NOMORPH><FONT COLOR=\"GRAY\"><i><b>Ответ:</b><p>" +
               str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "<br>") +
               "</p></i></FONT></NOMORPH>\n")
    file.close()

placeq = ""
placea = ""
placeqa = ""


def export(t):
    print("export:", t)
    for QA in t:
        file = str(QA['id'])
        file = ("0"*(13-len(file))) + file
        hdr_write(placeqa, file, list(QA))
        hdr_write_a(placea, file, list(QA))
        hdr_write_q(placeq, file, list(QA))
        htm_write(placeqa, file, list(QA))
        htm_write_a(placea, file, list(QA))
        htm_write_q(placeq, file, list(QA))

# t = []

# t = banki.getQuestionList (['Банкротство банков', 'http://www.banki.ru/services/questions-answers/?id=4826772?p=0'], 100100000000)
# export(banki.getQAbankiru(1))
# export(cbr.getQAcbr(2))
# export(getQAff(3))
# export(t)


# t_file = open("ban.html", "w")
# t_file.write(json.dumps(t))
# t_file.close()
# print(t)

# Thread(target=export(banki.getQAbankiru(1))).start()
# Thread(target=export(cbr.getQAcbr(2))).start()
Thread(target=export(ff.getQAff(3))).start()

# p1.start()
# p2.start()
# p3.start()
#
# p1.join()
# p2.join()
# p3.join()


