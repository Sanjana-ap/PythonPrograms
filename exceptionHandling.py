a = [11,22,33]
try:
    a=10/0
    print(a[2])
    print(a[5])   # one type of try at a time
    print(y)
except ZeroDivisionError:
    print("caught")
except IndexError:
    print("Index")
except:
    print("common block")
finally:
    print("Exceptions were caught")
