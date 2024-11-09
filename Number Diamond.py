from math import floor
def pattern(n):
    l = len(n)
    for i in range(l*2-1):
        if i < l:
            print(" "*(l*2-i), end="")
            for j in range(i + 1):
                print(f"{n[j]}", end=" ")
        else:
            if l <= 3:
                print(" "*(floor(l/2)+i), end=" ")
            elif l < 6:
                print(" "*(floor(l/2)+i-1), end=" ")
            elif l == 6:
                print(" " *(floor(l/2)+4+(i-l)), end=" ")
            elif l < 9:
                print(" " *(floor(l/2)+5+(i-l)), end=" ")
            elif l >= 9:
                print(" " *(floor(l/2)+6+(i-l)), end=" ")
            # print(" "*(l // 2 + max(0, (4 if l == 6 else 5) + (i - l))),end="") # This line from ChatGPT!
            for j in range((l * 2 - 1 - i)):
                print(f"{n[j]}", end=" ")
        print()
while True:
    pattern(input("Enter a number: "))