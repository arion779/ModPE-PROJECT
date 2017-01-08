import os

path = "/sdcard/ModPE/"
project_name = "Project"

folders = \
[
   ["images" , [
     
     ["items-opaque", []],
     ["terrain-atlas", []],
     ["armor", [] ],
     ["mob", [] ]
   
   ] ],
   ["script" , [] ]

]

def create_folder(path):
    if not os.path.exists(path):
       os.mkdir(path)
       
def build(root,data):
    if data:
       for d in data:
           name = d[0]
           path = os.path.join(root,name)
           create_folder(path)
           build(path,d[1])
           
       
full_path = os.path.join(path,project_name) 
create_folder(full_path)        
    
build(full_path,folders)
print("")
print (full_path)
