#
# from multiprocessing import Process
# from time import sleep
#
# def FI(i):
#     for k in range(i):
#         print("function", k)
#         sleep(0.01)
#
# def FI2(i):
#     for k in range(i):
#         print("function 2 ", k)
#         sleep(0.01)
#
# def main():
#     l = 1000
#
#     Process(target=FI, args=(l,)).start()
#     Process(target=FI2, args=(l,)).start()
#
#     for i in range (l):
#         print ("main", i)
#         sleep(0.01)
#     # p1.join()
#     # p2.join()
#
#
# if __name__ == '__main__':
#     main()




import requests
from lxml import html

url = "https://ff.ru/asks/255-kredit/?page=3"

requests.packages.urllib3.disable_warnings()
data = requests.api.request('post',url , data={'bar': 'baz'}, json=None, verify=False).text
t = html.document_fromstring(data).find_class('questions')[0].getchildren()
temp = map(lambda x: ["тема", "https://ff.ru" + x.getchildren()[1].getchildren()[0].get('href')], t)
k = list(zip(temp, [i for i in range(10, 10+len(t))]))

print( len(t))
print(k)