# Assignment 3.2
score = input("Enter Score: ")
score = float(score)
if 0.0 < score > 1.0:
    print("Invalid value")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.9:
    print("F")
