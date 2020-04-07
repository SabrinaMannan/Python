numb1=int(input("numb1:"))
numb2=int(input("numb2:"))
numb3=int(input("numb3:"))

if numb1>numb2:
    if numb1>numb3:
        print(numb1, "is the largest")
    else:
        print(numb3,"is largest")

if numb2>numb1:
    if numb2>numb3:
        print(numb2,"is the largest")
    else:
        print(numb3,"is the largest")
