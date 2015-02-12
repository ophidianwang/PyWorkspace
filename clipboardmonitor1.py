# encoding: utf-8

import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))

#import pyperclip
from Tkinter import *

recent_value = ""

test = Tk()

while True:
    #tmp_value = pyperclip.paste()
    tmp_value = test.clipboard_get()

    if tmp_value != recent_value:
        recent_value = tmp_value
        print "Value changed: %s" % recent_value

        if os.path.isfile(recent_value):
        	print recent_value+ " is a file"
        elif os.path.isdir(recent_value):
        	print recent_value+ " is a dir"

    time.sleep(0.1)