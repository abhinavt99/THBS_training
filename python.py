n = input()
k = int(len(n))
for i in range(k):
    for j in range(i+1):
        print("*", end="")
    print()