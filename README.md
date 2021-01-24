# FileBased Key_Value Pair
FreshWorks Test
# Requirements
Python 3</br>
Json
# Usage
<pre>
1) keypair=KeyVal()                   //creating object to keyval pair
2) keypair.load("path")              // create a new file and also  load the file if already exist
3) keypair.create(key,val,lifetime) //creates a new key value pair
4) keypair.read(key)               // returns value of specified key
5) keypair.delete(key)            //delete the key specified
</pre>
# Implementation Overview
1) Taking Key-Value input from user</br>
2) Storing them into file</br>
3) Reading data from file and convert it into Key-Value pair</br>
4) Performing Operations required by user and saving result
5) Saving file can be performed using other thread for better performance

<b>Python Packages used in Implementation</b>
1) json  (Converts Key-Value pair to String and String to Key-Value pair) </br>
2) threading (For Multi Threading) </br>
3) datetime ( For storing timestamp of key)
## Tasks
### Load File
<b>Tasks</b>
1) Load Data from file if exists
2) Create File if not exists
3) Create file in default directory if path is not specified
### Create Key-Value Pair
<b>Tasks</b>
1) Create Key-Value Pair 
2) Validate Key-Value Pair  
3) Check whether key already exist
4) Check size of file will exceed 1GB if Key-Value Pair added
5) If key value pair satisfies all the rules then save it into file
6) Store Key-Value Pair along with time-stamp
### Read Key-Value Pair
<b>Tasks</b>
1) Check wether Key exist
2) If key exist then check wether key is <b>alive</b>
3) Return Value of specified Key
### Delete Key-Value Pair
<b>Tasks</b>
1) Check wether Key exist
2) If key exist then check wether key is <b>alive</b>
3) Delete Key if exist
4) Update File 
