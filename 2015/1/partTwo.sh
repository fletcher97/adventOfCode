#!/bin/bash
pos=0
count=0
cat input | while read -n 1 c; do
	((count=count+1))
	if [[ $c == "(" ]]; then
		((pos=pos+1))
	else
		((pos=pos-1))
	fi
	if [[ pos -lt 0 ]]; then
		echo $count
		exit 1
	fi
done
