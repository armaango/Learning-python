# Enter your code here. Read input from STDIN. Print output to STDOUT
cases,impcanLoose = tuple(raw_input().split())
cases , impcanLoose = int(cases), int(impcanLoose)
imp = 0
impMustWin = 0
totalLuck = 0
luckList = []
for x in range(0,cases):
    luck, impornot = tuple(raw_input().split())
    luck , impornot = int(luck), int(impornot)
    totalLuck += luck
    if impornot == 1:
        imp += 1
        luckList.append(luck)
impMustWin = imp - impcanLoose
for d in range (0,impMustWin) :
    totalLuck -= 2*(sorted(luckList))[d]
print totalLuck