ByOne = [
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"
]
strNum = raw_input("Please enter an integer:\n>> ")
def subhounder(inputNum):
    num = int(inputNum)
    if 0 <= num <= 19:
        return ByOne[num]
