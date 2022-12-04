def prioritize():
    with open('input.txt') as f:
        lines = f.readlines()
        
        sum = 0
        for rucksack in lines:

            ruck1, ruck2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

            duplicate = None
            for item in ruck1:
                if item in ruck2:
                    duplicate = item

            sum += calculate_priority(duplicate)

        print(f'Prio sum is: {sum}')

def prioritize2():
    with open('input.txt') as f:
        lines = f.readlines()
        subList = [lines[n:n+3] for n in range(0, len(lines), 3)]

        trio_sum= 0
        for trio in subList:
            duplicate = None
            for ruck in trio:
                group_total = 0
                for item in ruck:
                    if item in trio[1] and item in trio[2]:
                        duplicate = item
                        group_total += calculate_priority(duplicate)
                        break
                if(group_total >0):
                    break
            trio_sum += group_total
                        
        print(f'Three group elf prio sum is: {trio_sum}')
def calculate_priority(dupe):
    prio = 0
    if dupe.islower():
        prio = ord(dupe) - 96    

    else:
        prio = ord(dupe) - 38
    
    return prio

prioritize()
prioritize2()