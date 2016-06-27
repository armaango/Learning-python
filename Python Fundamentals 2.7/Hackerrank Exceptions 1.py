# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = int(raw_input())
while cases > 0 :
    i = 0
    inp = raw_input()
    nums = inp.split()
    try:
        n1 = int(nums[0])
        i = 1
        n2 = int(nums[1])
    except:
        if i == 1:
            print "Error Code: invalid literal for int() with base 10: '"+nums[1]+"'"
        else:
            print "Error Code: invalid literal for int() with base 10: '"+nums[0]+"'"
        cases -= 1
        continue
    try:
        print n1/n2
    except:
        print "Error Code: integer division or modulo by zero"
        cases -= 1
        continue
    cases -= 1