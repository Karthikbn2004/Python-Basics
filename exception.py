try:
    a= 10 / 0
    print(a)
except:
        print("Some exception raised")
else:
    print("No exception raised,everything worked")
finally:
    print("This is a final block")
print("Outside try block")
print("starting line")

a = [11, 22, 33]
print(a)

print(a[1])


output:
  Some exception raised
This is a final block
Outside try block
starting line
[11, 22, 33]
22
