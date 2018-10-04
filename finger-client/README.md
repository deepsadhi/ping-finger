Finger Client
-------------

Requirements:
```bash
$ sudo apt-get install python-minimal # Or install python2.7 using any package manager
$ cd finger-client
$ chod +x finger-client # If the file is not executable
```

Executable
```bash
$ ./finger-client 
$ ./finger-client [user]
$ ./finger-client [user@host]
```

How to make executable:
* Add line "#!/usr/bin/python2" in the first line of "finger-client" file 
* Remove extension ".py" from file name
* Make file excutable with command "chomd +x finger-client"

Source code:
* Python source code can be found in "finger-client.py" file
```bash
$ python2 finger-client.py
```

Submitted by:
* JID: J00627938
* Name: Deepak Adhikari