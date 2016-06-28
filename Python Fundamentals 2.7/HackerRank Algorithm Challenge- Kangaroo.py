
x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if( x1 >=x2 ) and (v1 > v2):
    print "NO"
elif ( x2 >=x1 ) and (v2 > v1):
    print "NO"
else :
    h = 0
    for x in range(1,10000) :
        exp1 = x1 + (x * v1)
        exp2 = x2 + (x * v2)
        if exp1 == exp2 :
            h = 1
            print "YES"
            break
        else:
            continue
if h == 0:
    print "NO"