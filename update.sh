#!/bin/bash

INTERVAL=2 #Set Interval

while true
do
	git fetch

	GIT=$(git status)
	
	if grep -q 'behind' <<< "$GIT"; 
	then
		echo "PULLING BRANCH!";
		git pull
	else
		echo "BRANCH IS ALREADY UPDATED"
	fi
	sleep $INTERVAL
done
#test