import re
from win32com.shell import shell, shellcon

with open('dirs1.txt', 'r') as f:
    # read_data = f.read()
    # print (read_data)
  print(type(f))
  c=0
  for line in f:
   match=re.search(r'Directory of',line)
   if match:
      #cline=line.split()
      #for v in cline:
       c+=1
     # print(line)
print(c)

# def sendto():
#     "What folder holds the SendTo shortcuts(from the Context Menu)?"
#     return get_path(shellcon.CSIDL_SENDTO)
# sendto()
