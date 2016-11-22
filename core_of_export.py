import banki


def hdr_write (f, qa):
    file = open("ExportedFiles/qa"+ f + ".hdr", "w")
    file.write('id' + " = " + str(qa['id']) + "\n")
    file.write('site' + " = " + str(qa['site']) + "\n")
    file.write('category' + " = " + str(qa['category']) + "\n")
    file.write('question_url' + " = " + str(qa['question_url']) + "\n")
    file.write('user_name' + " = " + str(qa['user_name']) + "\n")
    file.write('user_url' + " = " + str(qa['user_url']) + "\n")
    file.write('user_town' + " = " + str(qa['user_town']) + "\n")
    file.write('question_datetime' + " = " + str(qa['question_datetime']) + "\n")
    file.write('expert_name' + " = " + str(qa['expert_name']) + "\n")
    file.write('acces_date' + " = " + str(qa['acces_date']) + "\n")
    file.write('question' + " = " + str(qa['question']).replace("\n", "\t") + "\n")
    file.write('answer' + " = " + str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "\t")) # + "\n")
    file.close()


def hdr_write_q (f, qa):
    file = open("ExportedFiles/questions/q"+ f + ".hdr", "w")
    file.write('id' + " = " + str(qa['id']) + "\n")
    file.write('site' + " = " + str(qa['site']) + "\n")
    file.write('category' + " = " + str(qa['category']) + "\n")
    file.write('question_url' + " = " + str(qa['question_url']) + "\n")
    file.write('user_name' + " = " + str(qa['user_name']) + "\n")
    file.write('user_url' + " = " + str(qa['user_url']) + "\n")
    file.write('user_town' + " = " + str(qa['user_town']) + "\n")
    file.write('question_datetime' + " = " + str(qa['question_datetime']) + "\n")
    file.write('acces_date' + " = " + str(qa['acces_date']) + "\n")
    file.write('question' + " = " + str(qa['question']).replace("\n", "\t")) # + "\n")
    file.close()


def hdr_write_a (f, qa):
    file = open("ExportedFiles/answers/a"+ f + ".hdr", "w")
    file.write('id' + " = " + str(qa['id']) + "\n")
    file.write('site' + " = " + str(qa['site']) + "\n")
    file.write('category' + " = " + str(qa['category']) + "\n")
    file.write('question_url' + " = " + str(qa['question_url']) + "\n")
    file.write('expert_name' + " = " + str(qa['expert_name']) + "\n")
    file.write('acces_date' + " = " + str(qa['acces_date']) + "\n")
    file.write('answer' + " = " + str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "\t")) # + "\n")
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
    file.write("<tr><td " + style1column + " >acces_date</td><td " + style2column + " >" + str(
        qa['acces_date']) + "</td></tr>\n")
    file.write("</table></I></FONT>\n</NOMORPH>\n&nbsp\n<div>")
    file.write("<b>Ответ:</b><p>" + str(qa['answer']).replace("С уважением,", "").rstrip().replace("\n", "<br>")
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
    file.close()


def export(t):
    print("export")
    for QA in t:
        file = str(QA['id'])
        file = ("0"*(13-len(file))) + file
        hdr_write(file, QA)
        hdr_write_a(file, QA)
        hdr_write_q(file, QA)
        htm_write(file, QA)
        htm_write_a(file, QA)
        htm_write_q(file, QA)

# t = banki.getQAbankiru(1)

t = banki.getQuestionList (['Банкротство банков', 'http://www.banki.ru/services/questions-answers/?id=4826772?p=0'], 100100000000)
export(t)

# t_file = open("ban.html", "w")
# t_file.write(json.dumps(t))
# t_file.close()
# print(t)

