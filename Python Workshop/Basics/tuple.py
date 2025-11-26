students=("sara","ana","ram","ajit","nair","pal","varshh","thej","appi","suru","dikku","pal")
print(students[0])
print(students[-1])
print(students.count("pal"))
print(students)
print(type(students))
print("-------")

students_name={"sara","ana","ram","ajit","nair","pal","varshh","thej","appi","suru","dikku","pal"}
print(students_name)

print(students_name.add("jjj"))
print(students_name.remove("suru"))
students_name.clear()
print(students_name)
print(type(students_name))

print("--------")



data={"name":"vbs","age":22,"DOB":"21/08/2003","branch":"MCA","Pno":9535385775}
print(data)
print(type(data))

data["age"]=50
print(data)
print(data.keys())
print(data.values())

print(data.update(name="varsha"))
print(data)

