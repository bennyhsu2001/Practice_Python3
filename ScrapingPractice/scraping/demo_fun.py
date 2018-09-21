def fun1(name="guest"):
    print("Hello {}".format(name))

def count(*add_all):
    # print(add_all)  #(1,2,3,4,5) tuple
    count = 0
    for i in add_all:
        count += i
    return count
def fun2(start, *args, **kwargs):
    print("start = {}".format(start))
    print("args = {}".format(args))     #(1, 2, 3)
    print("kwargs = {}".format(kwargs)) #{'a': 4, 'b': 5, 'c': 6}

# fun1("tom")
# print(count(1,2,3,4,5))
fun2("a",1,2,3,a=4,b=5,c=6)
