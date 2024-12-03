# Read the file 
# indentify all of the mul(a,b) functions only in that regex
# actually do the a*b
# add all of the multiplication results together

import re

def main():

    input = open("input.txt", "r")
    data = input.read()
    print(data)

    sum = 0
    # ingnore the read until mul( id detected
    muls = []
    
    muls.append(re.findall(r'mul\((\d+),(\d+)\)', data))

    for mul in muls:
        # multiply the two numbers and add result to the sum
        for m in mul:
            sum += int(m[0]) * int(m[1])
    
    print(sum)
    input.close()


if __name__ == "__main__":
    main()


