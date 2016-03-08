#!/bin/bash

PWD=$(pwd)
count=$(ls *.css | wc -l)
concat=_minified
remove=$(rm -f)

function clean {
	name=${arg:4}${concat}
	path="$PWD"/$arg/
	if [ -f $path/$name.css ]; then
		rm $path$name.css
	fi	
}

function minimize_base {
	name=${arg:4}${concat}
	path="$PWD"/$arg
	clean
	count=$(ls $path/*.css | wc -l)
	if [ $count -gt 1 ]; then
	     $(cat $path/*.css > $path/$name.css)
	     echo "minified file for base directory created"
	fi
}

function minimize_pages {
	name=${arg:4}${concat}
	path="$PWD"/$arg
	clean
	count=$(ls $path/*.css | wc -l)
	if [ $count -gt 1 ]; then
	     $(cat $path/*.css > $path/$name.css)
	     echo "minified file for pages directory created"
	fi
}

function main-menu {
	if [ "$arg" == "css/base" ]; then
	minimize_base
	elif [ "$arg" == "css/pages" ]; then
	minimize_pages
	else
	echo "==================================================="
	echo "Please specify the path of the files to be minified"
	echo "==================================================="
	echo "css/base"
	echo "css/pages"
	fi
}

arg=$1
main-menu
