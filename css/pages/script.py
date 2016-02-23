#!/bin/bash

import os
from os import listdir
import re
from os.path import isfile, join

mypath = os.getcwd()
dirs = mypath.split('/')
current_dir = dirs[-1]
new_css_name = current_dir + '_minified.css'
new_path = mypath + '/' + new_css_name
main_file = mypath + '/' + 'main.css'
if os.path.isfile(new_css_name):
    os.remove(new_css_name)

#print new_path

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print onlyfiles

f2 = open(new_path, 'a')

if os.path.isfile(main_file):
    f1 = open(main_file, 'r')
    #print f1
    for line in f1:
        line = re.sub(r'\s+', ' ', line)
#        line = line.replace("\n", "")
        f2.write(line)
    f2.write('\n')
    onlyfiles.remove('main.css')
    f1.close()

onlyfiles = onlyfiles[1:]
onlyfiles.remove('script.py')

#print onlyfiles

for file in onlyfiles:
    f1 = open(file, 'r')
#    print file
    
    for line in f1:
        line = re.sub(r'\s+', ' ', line)
#        line = line.replace("\n", "")
        f2.write(line)
    f2.write('\n')
    f1.close()

f2.close()