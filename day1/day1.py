from functools import reduce

def count_gold(file):
    lines = f.read().split("\n\n")

    temp = []
    newList = []
    totals = []
    ans = 0
    max = 0
    for i in lines:
        temp = i.split("\n")

        sum = 0
        for j in temp:
            if j == '':
                j = 0
            sum += int(j)

            if sum > max:
                max = sum
                sum = 0
            totals.append(sum)
    
    print(f"Top elf is {max}")

    totals.sort(reverse=True)
    print(f"1- {totals[0]} 2- {totals[1]} 3- {totals[2]}")
    ans = totals[0] + totals[1] + totals[2]
    print(f"Sum of top 3 is {ans}")

with open('output.txt') as f:
    count_gold(f)