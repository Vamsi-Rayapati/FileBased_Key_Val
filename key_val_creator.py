import json
import os
import sys
from threading import Thread
from datetime import datetime,timedelta
jsontype=[str,bool,int,float,list,dict]
def isjsontype(val):
    if((type(val) in jsontype)or val is None):
        return True
    else:
        return False
def updatedata(self,jsonstr):
    f=open(self.filepath,"w")
    f.write(jsonstr)
    f.close()
class KeyVal:
    def __init__(self):
        self.data={}
        self.filepath=""
    def load(self,path="data.txt"):
        self.filepath=os.path.abspath(path)
        try:
            f=open(self.filepath,"r")
            jsonstr=f.read()
            self.data=json.loads(jsonstr)
            f.close()
        except:
            thread = Thread(target = updatedata, args = (self,json.dumps(self.data)))
            thread.start()
            thread.join();
    def create(self,key,val,lifetime=None):
        if(key in self.data):
            print("Key already exist")
        elif((type(key)==str)and(isjsontype(val))):
            if(len(key)<=32 and sys.getsizeof(val)/1024<=16):
                if(lifetime!=None):
                    self.data[key]=[val,str(datetime.now()+timedelta(seconds=lifetime))]
                else:
                    self.data[key]=[val,None]
                jsonstr=json.dumps(self.data)
                if(((sys.getsizeof(jsonstr)+os.stat(self.filepath).st_size)/(1<<30))<=1):
                    thread = Thread(target = updatedata, args = (self,jsonstr ))
                    thread.start()
                    thread.join();
                else:
                    print("File size exceeded 1GB")
            else:
                print("Size issue")
        else:
            print("Data Type error")

    def read(self,key):
        if key not in self.data:
            return "Key not found "
        elif self.data[key][1]==None:
            return self.data[key][0]
        elif(datetime.now()<=datetime.strptime(self.data[key][1],"%Y-%m-%d %H:%M:%S.%f")):
            return self.data[key][0]
        else:
            return "Key is expired"

    def delete(self,key):
        if key not in self.data:
            print("Key not found ")
        elif self.data[key][1]==None:
            del self.data[key]
        elif(datetime.now()<=datetime.strptime(self.data[key][1],"%Y-%m-%d %H:%M:%S.%f")):
            del self.data[key]
        else:
            print("Key is expired")
        thread = Thread(target = updatedata, args = (self,json.dumps(self.data)))
        thread.start()
        thread.join();
    def show(self):
        print(self.data)


if __name__ == "__main__":
    keyval=KeyVal();
    keyval.load("E:/students.txt")
    keyval.create("sai","cse",300)
    keyval.create("vamsi",1234)
    keyval.create("karthik",[20,20])
    keyval.create("sai",2020)
    keyval.create(90,880)  
    keyval.create("bhanu",{90:80,70:60})
    keyval.create("sravzan",188.5)
    keyval.create("mariii",[90,-0,"kiki"])
    print(keyval.read("sai"))
    keyval.delete("sai")
    print(keyval.read("sai"))
    keyval.show();

