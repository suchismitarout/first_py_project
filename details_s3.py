import json
def read_file():
    with open("details.txt", "r") as fr:
        file_contents = fr.read()
        return file_contents

def convert(contents):
    list_of_lines = contents.split("\n")
    list_of_dict = []
    for i in list_of_lines:
        if len(i) != 0:
            d = json.loads(i)
            list_of_dict.append(d)
    return list_of_dict

def find_min_age(list_of_dict):
    sum = 0
    for j in list_of_dict:
         sum = sum + j['age']
         min_age = sum // len(list_of_dict)
    return min_age


def find_avg_salary(list_of_dict):
    sum = 0
    for k in list_of_dict:
        sum = sum + k['salary']
        avg_salary = sum // len(list_of_dict)
    return avg_salary


contents = read_file()
list_of_dict = convert(contents)
#print(type(list_of_dict))
age = find_min_age(list_of_dict)
print("minium age is", age)
salary = find_avg_salary(list_of_dict)
print("average salary is", salary)

## write in a shell sctipt which will download file and invoke this python program from shell script.



