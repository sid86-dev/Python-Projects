import os
import csv

class Readname():
    def __init__(self, loc):
        self.loc = loc

    # get list of filenames in the folder

    def listNames(self):
        filenames = os.listdir(self.loc)
        l = [filename for filename in filenames]
        return l

    # write the list of filenames into csv file

    def collect(self, list):
        try:
            with open('filenames.csv', 'w', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['FILENAMES'])
                for name in list:
                    thewriter.writerow([name])
        except:
            return "No data to write"

if __name__=="__main__":

    path = r'C:\\sid_programmer\\PYTHON\Python Course'

    l = Readname(path)

    files = l.listNames()

    l.collect(files)