#!/bin/bash

import os
from os import listdir
import re
from os.path import isfile, join

## Function to replace white space using regex
def replace_whitespace(filename):
    open_file = open(filename, 'r')
    f1 = open_file.read()
    f1 = re.sub(r'\s+', ' ', f1)
    f2.write(f1)
    open_file.close()


mypath = os.getcwd() 
dirs = mypath.split('/')
current_dir = dirs[-1]
new_css_name = current_dir + '_minified.css'
new_path = mypath + '/' + new_css_name
main_file = mypath + '/' + 'main.css'
if os.path.isfile(new_css_name):
    os.remove(new_css_name)

## get the list of css files
onlyfiles = [f for f in listdir(mypath) if f.endswith('.css')]

## open folder_minified.css in append mode
f2 = open(new_path, 'a')

## replace white space for main.css '(if main exists)' 
if os.path.isfile(main_file):
    replace_whitespace(main_file)
    onlyfiles.remove('main.css')

## repeat the same for all other .css files
for filename in onlyfiles:
    replace_whitespace(filename)

f2.close()
