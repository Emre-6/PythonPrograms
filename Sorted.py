numbers=[1,59,44,64,97,2,3]

#numbers.sort()
result=sorted(numbers)
result=sorted(numbers,revese=True)
result=sorted((1,53,45,67,97,5,7))

#print(numbers)

users=[
    {"username":"jamessmith","tweets":["tweet1","tweet2"],"email":"info@gmail.com"},
    {"username":"jamessmith","tweets":[]},
    {"username":"jamessmith","tweets":["tweet1"],"name":"","phone":"434312134"}
    
]

result=sorted(users,key=len)
result=sorted(users,key=len,reverse=True)
result=sorted(users,key=lambda user: user["username"])
result=sorted(users,key=lambda user: len(user["tweets"]))

courses=[
    {"Title":"Python Course","Students":25000}
    {"Title":"Web Develoing","Students":25000}
    {"Title":"Javascript Course","Students":5000}

]

result=sorted(courses, key=lambda course: course["students"])
result=sorted(courses, key=lambda course: course["students"],reverse=True)
result=map (lambda course: course["title"] course sorted(courses, key=lambda course: course["students"],reverse=True))

print(list(result))

