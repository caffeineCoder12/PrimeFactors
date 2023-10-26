#Python program to print all factors and prime factors of a number

num = int(input("Enter number to find out its factors "))

fac = []
pfac = []

#Storing factors in list called fac
for i in range(1,num+1):
    if num%i == 0:
        fac.append(i)
    else:
        continue

#Storing prime factors in list called pfac
for x in fac:
    
    for i in range(1,x+1):
        if x%i == 0:
            pfac.append(i)
        else:
            continue

print("Factors of",num,"are",fac,"and prime factors are",pfac)

