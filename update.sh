#!/bin/bash

GIT=$(git status)

if grep -q 'behind' <<< "$GIT"; then
	echo "FOUND!";
fi