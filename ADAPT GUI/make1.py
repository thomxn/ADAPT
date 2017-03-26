from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

###############################
#      Main Class Window      #
###############################

class MainWindow(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        mv_View = QGridLayout()

        stack.setCurrentWidget(self.d_Dialog(mv_View))
        self.setLayout(mv_View)
        self.show()


    def d_Dialog(self, mv_View):

        dup_b  = QPushButton('Duplicate')
        dup_b.setFont(QFont('Calibri',12))
        dup_b.setCheckable(True)

        model = CheckableDirModel()
        tree = QTreeView()
        tree.setModel(model)

        tree.setAnimated(True)
        tree.setIndentation(20)
        tree.setSortingEnabled(False)

        lay = QHBoxLayout()
        lay.addStretch(1)
        lay.addWidget(dup_b)

        layout = QGridLayout()
        layout.addWidget(tree,0,0)
        layout.addLayout(lay,1,0)
        #layout.addWidget(dup_b,1,0,1,1)

        mv_View.addLayout(layout,0 ,0,Qt.Alignment())
        dup_b.clicked[bool].connect(lambda : get_Value(model))

def get_Value(model):

    list = model.exportChecked()
    Duplicate(list)

###########################
#        Duplicate        #
###########################
import os
import sys
import hashlib


def Duplicate(folders):
    dups = {}

    for i in folders:
        # Iterate the folders given
        if os.path.exists(i):
            # Find the duplicated files and append them to the dups
            joinDicts(dups, findDup(i))
        else:
            print('%s is not a valid path, please verify' % i)
    printResults(dups)
# Reading out files to Hash
def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
# Checking for Duplicates
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
# Merging/Appending Dict.
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
# Result Printing Method.
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('\nThe following files are identical. The name could differ, but the content is identical')
        print('\n___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________\n')
    else:
        print('\nNo duplicate files found.')


#Duplicate()


#####################################
#Checkable dir model using QDirModel#
#####################################

class CheckableDirModel(QDirModel):  # QtGui changed to QtWidgets


    def __init__(self, parent=None):

        QDirModel.__init__(self, None)
        self.checks = {}
        self.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)


    def data(self, index, role=Qt.DisplayRole):

        if role != Qt.CheckStateRole:
            return QDirModel.data(self, index, role)
        else:
            if index.column() == 0:
                return self.checkState(index)



    def flags(self, index):
        return QDirModel.flags(self, index) | Qt.ItemIsUserCheckable



    def checkState(self, index):
        if index in self.checks:
            return self.checks[index]
        else:
            return Qt.Unchecked



    def setData(self, index, value, role):

        if (role == Qt.CheckStateRole and index.column() == 0):
            self.checks[index] = value
            self.exportChecked()
            return True

        return QDirModel.setData(self, index, value, role)


    def exportChecked(self):

        selection = []
        for key in self.checks:
            if self.checks[key] == 2:

                str = self.filePath(key)
                while str not in selection:
                    selection.append(str)


        return selection


##########################
#   Main Function Block  #
##########################
if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = QMainWindow()
    screen.setWindowTitle('ADAPT')
    screen.setWindowIcon(QIcon('logo.png'))
    screen.setGeometry(100, 100, 640, 280)

    stack = QStackedWidget()

    main = MainWindow()

    #main.show()
    sys.exit(app.exec_())