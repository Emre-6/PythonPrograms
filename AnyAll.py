result=all([True,True,False])
result=all([True,True,True])
result=any([True,False,False])

numbers=[1,3,6,8,9,10]

result=any([bool(number)for number in numbers])
result=all([bool(number) for number in numbers])
result=all([bool(number) for number in numbers if number%2==1])
result=all([number%2==0 for number in numbers])
result=any([number%2==0 for number in numbers])

people=["Tony","Henry","James"]

result=any([person[0]=='H' for person in people])
result=all([person[0]=='H' for person in people if person[0]=='a'])

print(result)

