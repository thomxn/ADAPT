import os,sys
import json

dirIndex = {}
dir ={}
def indexer(root):
    dir[root] = {}
    for path in os.listdir(root):
        curr_path = os.path.join(root, path)
        if os.path.isfile(curr_path):

            name, ext = os.path.splitext(curr_path)

            if ext in dir[root]:
                    dir[root][ext] += 1
            else:
                    dir[root][ext] = 1

        elif os.path.isdir(curr_path):
              temp = indexer(curr_path)
              for v in temp[curr_path]:
                # print curr_path, v, temp[curr_path][v]
                if v in dir[root]:
                    # print root, v
                    dir[root][v] += temp[curr_path][v]
                else:
                    dir[root][v] = temp[curr_path][v]
                    # print temp[v]


    return dir
indexer('F:\Movies')
with open ('index.txt', 'r') as f:
    my_dict = json.loads(f)
print my_dict


# https://www.zippymoviez.us/forum/-22-tamil-camvcdpredvdscrwebrip/?page=4