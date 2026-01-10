marks={ 
       "Niloy":85,
       "Turin":90,
       "Kabaya":78,
       0:"Niloy"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Luffy":95})
print(marks)

print(marks["Niloy"])
print(marks[0])
print(type(marks))
print(marks.get("Turin"))#prints 90
print(marks["Turin"])#prints 90


print(marks.get("Turin2"))#prints None
print(marks["Turin2"])# Returns an error