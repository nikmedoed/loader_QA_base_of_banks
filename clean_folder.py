import os
import core_of_export


def clean_folders():
    print( os.listdir(core_of_export.placeq))
    for i in os.listdir(core_of_export.placeq):
        os.remove(core_of_export.placeq+i)
    print( os.listdir(core_of_export.placea))
    for i in os.listdir(core_of_export.placea):
        os.remove(core_of_export.placea+i)
    print( os.listdir(core_of_export.placeqa))

    for i in os.listdir(core_of_export.placeqa):
        try:
            os.remove(core_of_export.placeqa+i)
        except:
            None


if __name__ == '__main__':
    clean_folders()