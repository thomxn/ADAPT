import os
import shutil

extCnt = {}

def fcount(path):
   
    for f in os.listdir(path):
        path1 = os.path.join(path, f)
        if os.path.isfile(path1):
            
            f_path, f_extension = os.path.splitext(path1)

            if f_extension in extCnt:
                extCnt[f_extension].append(f_path)
            else:
                extCnt[f_extension] = [f_path]

#Printing the File Structure
    #for f in extCnt :
    #    print "\n",f,"\n"
    #    t_print(extCnt, f)
    #    print "\n\n"

#def t_print(extCnt, f):

#    for i in range(0,len(extCnt[f])):
#        print "\t",extCnt[f][i], "\n"

def sortfiles():
    
    for key in extCnt:
        
        if len(extCnt[key])> 7 :# count to max limit of similar files in a folder
            
            #changing to Directory
            os.chdir(path)
            n_folder= key[1:] + ' Folder'
            os.mkdir(n_folder)
                
            for i in range(0, len(extCnt[key])):
                f_path = os.path.join(path,extCnt[key][i] + key)
                try:
                    shutil.move(f_path, os.path.join(path, n_folder))
                except:
                    pass

#main Funtion
path = raw_input("Enter a Directory : ")
n = raw_input("Enter Max-Count for free Distribution : ")
n = int(n)
fcount(path)
sortfiles()
