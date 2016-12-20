import os
import core_of_export


def clean_folders(qa= "ExportedFiles/"):
    a = qa + "answers/"
    q = qa + "questions/"
    # print( os.listdir(q))
    for i in os.listdir(q):
        os.remove(q+i)
        print(q+i)
    # print( os.listdir(a))
    for i in os.listdir(a):
        os.remove(a+i)
    # print( os.listdir(qa))

    for i in os.listdir(qa):
        try:
            os.remove(qa+i)
        except:
            None


if __name__ == '__main__':
    # clean_folders("E:/clouds/MailCloud/ExportedFiles_ff/")
    clean_folders("E:\clouds\MailCloud\ExportedFiles_Banks\ExportedFiles_banki/".replace("\\","/"))
    # clean_folders("E:/clouds/MailCloud/ExportedFiles_banki/")