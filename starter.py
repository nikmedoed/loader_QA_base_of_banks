import banki
import ff
import core_of_export


def main():
    core_of_export.placeqa = "ExportedFiles_ff/"
    ff.getQAff(3)
    print("go to banki")
    core_of_export.placeqa = "ExportedFiles_banki/"
    banki.getQAbankiru(1)


if __name__ == '__main__':
    # multiprocessing.freeze_support()
    main()