#!/bin/bash
len=$#
arr=($@)
for i in $( seq 0 $len )
do
    for j in $( seq 0 $(($len-2)) )
    do
        if [ $((${arr[$j]}))  -gt $((${arr[$(($j+1))]})) ]
        then
            temp=${arr[$j]}
            arr[$j]=${arr[$(($j+1))]}
            arr[$((j+1))]=$temp
        fi
    done
done
echo ${arr[*]}

