from sys import argv

try:
    n = int(argv[1])
    m = int(argv[2])
except ValueError:
    print("Please enter a NUMBER")
    exit(1)
if n <=0 or m <=0:
    print("Need a NUMBER greater than zero")
    exit(1)

cycmas = [i+1 for i in range(n)]
k = True
massive = []
answer = []
index = 0

while k:
    massive.append(cycmas[index])

    if len(massive) > m-1:
        answer.append(str(massive[0]))

        if massive[-1:][0] == cycmas[0]:
            k = False
        massive = []

    else:
        index += 1

    if index > (len(cycmas) - 1):
        index = 0

ans = "".join(answer)
print(ans)