import banki
import json

# banki.getQAbankiru(1)

t = banki.getQuestionList (['Банкротство банков', 'http://www.banki.ru/services/questions-answers/?id=4826772?p=0'], 100100000000)
# t_file = open("ban.html", "w")
# t_file.write(json.dumps(t))
# t_file.close()


print(t)

