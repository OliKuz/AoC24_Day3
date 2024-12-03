# Read the file 
# indentify all of the mul(a,b) functions only in that regex
# actually do the a*b
# add all of the multiplication results together


# TASK 2 --> ignore mul() functions that are have don't() somewhere before them

import re

def main():

    input = open("input.txt", "r")
    data = input.read()

    sum = 0
    # ingnore the read until mul( id detected
    muls = []
    dos = []
    
    muls.append(re.findall(r'mul\((\d+),(\d+)\)', data))

    for mul in muls:
        # multiply the two numbers and add result to the sum
        for m in mul:
            sum += int(m[0]) * int(m[1])

    
    print(f"Sum is task 1: {sum}")


    # TASK 2

    instructions = re.findall(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', data)

    enabled = True 
    sum_task2 = 0

    for instr in instructions:
        if instr[0] == "do()":
            enabled = True
        elif instr[0] == "don't()":
            enabled = False
        else: 
            if enabled:
                a, b = instr[1], instr[2]
                sum_task2 += int(a) * int(b)

    print(f"Sum in task 2: {sum_task2}")

    input.close()


if __name__ == "__main__":
    main()


