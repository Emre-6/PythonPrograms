import module

result=module.number
result=module.numbers
result=module.student
result=module.student["name"]
result=module.student["grade"]
result=module.total(10,20)

import module as m

result=m.numbers

from module import student, total

result=student
result=total(10,20)

from module import *

result=number
result=student["grades"]


print(result)


