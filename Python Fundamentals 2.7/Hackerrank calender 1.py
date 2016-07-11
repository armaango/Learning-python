# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
mm, dd, yy = (int(i) for i in raw_input().split())
result = calendar.weekday(yy, mm, dd)
if result == 0:print "MONDAY"
elif result == 1:print "TUESDAY"
elif result == 2:print "WEDNESDAY"
elif result == 3:print "THURSDAY"
elif result == 4:print "FRIDAY"
elif result == 5:print "SATURDAY"
elif result == 6:print "SUNDAY"