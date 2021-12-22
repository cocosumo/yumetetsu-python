#!/bin/bash

INTERVAL=2 #Set Interval
currentDate=`date`

while true
do
	git fetch

	GIT=$(git status)
	
	if grep -q 'behind' <<< "$GIT"; 
	then
		echo "PULLING BRANCH!";
		git pull
	else
		echo $currentDate " BRANCH IS ALREADY UPDATED"
	fi
	sleep $INTERVAL
done
#test