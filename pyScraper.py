
import os
import sys
import getopt
import shutil
import time
from datetime import datetime

EXT_TYPE = 0
MOVE_TYPE = 1
SCR_DIR = 2
DEST_DIR = 3

COPY = 0
MOVE = 1

REPORT_NAME = "_report.txt"

ignoreDirKeyWords = [
    'Recycle',
    'Windows',
    'System Volume Information',
    'AppData'
]


def argumentExtraction(argv):
    destFile = None
    srcFile = None
    extType = None
    moveType = None

    try:
        [opts, argv] = getopt.getopt(
            argv, "ht:s:d:cm", ["help", "type=", "srcfile=", "destfile=", "copy", "move"])
    except getopt.GetoptError:
        helpPrints()
        return None
    for opt, arg in opts:
        if opt == '-h':
            helpPrints()
            exit()
        elif opt in ("-t", "--type"):
            extType = arg.split(' ')
            print('File type is {0}'.format(extType))
        elif opt in ("-s", "--srcfile"):
            srcFile = arg
            print("Source Directory is {0}".format(srcFile))
        elif opt in ("-d", "--destfile"):
            destFile = arg
            print("Destination Directory is {0}".format(destFile))
        elif opt in ("-c", "--copy"):
            moveType = COPY
            print('Copy the files from {0} to {1}'.format(srcFile, destFile))
        elif opt in ("-m", "--move"):
            moveType = MOVE
            print('Move the files from {0} to {1}'.format(srcFile, destFile))

    return [extType, moveType, srcFile, destFile]


def helpPrints():
    print('\npyScraper.py <arguments> \n')
    print('~~~ARGUMENT LIST~~~\n')
    print('-t:\tfile extension to be moved/copied\t-t <type>\n')
    print('-s:\tSource Directory\t-s <srcpath>\n')
    print('-d:\tDestination Path\t-d <destpath>\n')
    print('-c:\tCopy the file to the destination\n')
    print('-m:\tMove the file from the source to the destination\n')


def main(argv):

    scraperParams = argumentExtraction(argv)
    if(scraperParams != None):
        scraper(scraperParams)


def scraper(scraperParams):
    fileMoved = 0

    reportFile = open(os.path.join(scraperParams[DEST_DIR], REPORT_NAME), "a+")
    reportFile.write("{0}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    startTime = time.time()

    for root, _, files in os.walk(scraperParams[SCR_DIR], topdown=True):
        ignoreDir = any(word for word in ignoreDirKeyWords if word in root)
        if(ignoreDir == False):
            print("root directory: {0}".format(root))
            for filename in files:
                print("filename: {0}".format(filename))
                _, extension = os.path.splitext(filename)

                extensionExists = extension.lower() in scraperParams[EXT_TYPE]
                if extensionExists:
                    moveFile = os.path.join(root, filename)
                    if(scraperParams[MOVE_TYPE] == COPY):
                        print('copy file {0}'.format(moveFile))
                        try:
                            dest = shutil.copy2(
                                moveFile, scraperParams[DEST_DIR])
                            print('file copied to {0}'.format(dest))
                            reportFile.write('{0}\t--->\t{1}\n'.format(moveFile, dest))
                            fileMoved += 1
                        except:
                            print('FAILED to copy file {0}'.format(moveFile))
                    elif(scraperParams[MOVE_TYPE] == MOVE):
                        print('move file {0}'.format(moveFile))
                        try:
                            dest = shutil.move(
                                moveFile, scraperParams[DEST_DIR])
                            print('file moved to {0}'.format(dest))
                            reportFile.write('{0}\t--->\t{1}\n'.format(moveFile, dest))
                            fileMoved += 1
                        except:
                            print('FAILED to move file {0}'.format(moveFile))

    endTime = time.time()
    totalTime = endTime - startTime
    print("Time Taken: {0}".format(totalTime))
    print("Total Files Moved: {0}".format(fileMoved))

    reportFile.write("Time Taken: {0}\n".format(totalTime))
    reportFile.write("Total Files Moved: {0}".format(fileMoved))
    reportFile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
