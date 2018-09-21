x = {"name":"Jack","age":30}
print(x["name"])
for k in x:
    print("{0}-{1}".format(k, x[k]))
x["age"]  = 28
x["email"] = "Jack@gmail.com"
print("email" in x)