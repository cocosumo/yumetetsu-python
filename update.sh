#!/bin/bash

git fetch

GIT=$(git status)

if grep -q 'behind' <<< "$GIT"; 
then
	echo "UPDATED";
	git pull
else
	echo "ALREADY UPDATED"
fi