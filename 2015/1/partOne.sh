#!/bin/bash
up=`cat input | awk -F"(" '{print NF-1}'`
down=`cat input | awk -F")" '{print NF-1}'`
echo $(($up - $down))
