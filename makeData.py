import os,sys
import json
dirIndex = {}
# dir ={}
# count = 0
fp = open ('dir.tsv', 'w')
count = 0
# fp.write('Label\tGroup\n')
fp.close()
def indexer(root):
    # fp.write('ollo')
   try:
    if root not in dirIndex:
        global count
        dirIndex[root] = count
        count = count+1
        # count+=1
    for path in os.listdir(root):
        curr_path = os.path.join(root, path)
        f = open('dir.tsv', 'a')

        f.write((path+'\t'+str(dirIndex[root])+'\n').encode('utf8'))
        # f.close()
            # name, ext = os.path.splitext(curr_path)
        if os.path.isdir(curr_path):
               indexer(curr_path)
        #       for v in temp[curr_path]:
        #         # print curr_path, v, temp[curr_path][v]
        #         if v in dir[root]:
        #             # print root, v
        #             dir[root][v] += temp[curr_path][v]
        #         else:
        #             dir[root][v] = temp[curr_path][v]
        #             # print temp[v]
   except:
       pass
indexer('F:\Movies')
print dirIndex