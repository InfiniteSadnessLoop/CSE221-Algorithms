inp = int(input())
for i in range(inp) :
    a=input()
    x=a.split(' ')
    if ('+') in x:
        res= float(x[1]) + float(x[3])
    if ('-') in x:
        res= float(x[1]) - float(x[3])
    if ('*') in x:
        res= float(x[1]) * float(x[3])
    if ('/') in x:
        res= float(x[1]) / float(x[3])
    print(res)
