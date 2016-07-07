# Enter your code here. Read input from STDIN. Print output to STDOUT
data , chk  = raw_input(), raw_input()
count = 0
for i in range(0,len(data)):
    if data[i:i+len(chk)] == chk :
        count +=1
print count