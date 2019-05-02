num1=1;
num2=1;
echo $num1
echo $num2
while [ $(($num1 + $num2)) -le 100 ] 
do
    {
        temp=$num2
        num2=$num1
        num1=$(($num1 + $temp))
        if [ $(( $num1%2 )) -gt 0  ]
        then
             echo $num1
        fi
    }
done
