import os

f_dic = {} # dictionary to save the count
p_list = [] # list to save all file paths

# retrive file paths to all files
def getDir(i_path):
    for pth in os.listdir(i_path):
        try:
            path1 = os.path.join(i_path,pth)
            if os.path.isdir(path1):
                getDir(path1)
            if os.path.isfile(path1):
                p_list.append(path1)
        except:
            pass

    return 0

#get total count to all type of files
def getCount(p_list):
    for i in range(0,len(p_list)):
        path1 = p_list[i]
        if os.path.isfile(path1):
            f_path, f_extension = os.path.splitext(path1)

            if f_extension in f_dic:
                f_dic[f_extension] += 1
            else:
                f_dic[f_extension] = 1

    return 0


#Main Function:
i_path = raw_input("Enter A Path: (eg: D:/dir1/dir2)")
c = getDir(i_path)
d = getCount(p_list)
print f_dic
