# FileBased_Key_Val
FreshWorks Test
# Requiements
Python 3</br>
Json
# Implementation Overview
1) Taking Key-Value input from user</br>
2) Storing them into file</br>
3) Reading data from file and convert it into Key-Value pair</br>
4) Performing Operations required by user and saving result

<b>Python Packages used in Implementation</b>
1) json  (Converts Key-Value pair to String and String to Key-Value pair) </br>
2) threading (For Multi Threading) </br>
3) datetime ( For storing timestamp of key)

### Load File
<b>Tasks</b>
1) Load Data from file if exists
2) Create File if not exists
3) Create file in default directory if path is not specified
<pre>
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
</pre>
