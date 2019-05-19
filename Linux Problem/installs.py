import subprocess
import json

requirements = json.loads(open('packages.json').read())
dict = requirements['Dependencies']
list=[]

for item,version in dict.items():
    command = ["sudo","pip","install",item]
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError:
        list.append(item)

if (len(list)==0):
    print("SUCCESS")
else:
    for i in range(len(list)):
        print ("could not install "+list[i])
