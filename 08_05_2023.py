## importing the module
import itertools
import sys
#define Test Cases:
Tests = [
    {"num":'789', "outcome": 892.5}
]

def numberPermutation(num):
    permList = []
    number = ""
    try:
        number = str(num)
    except:
        number = num

    ## itertools.permutations method
    permutaion_list = list(itertools.permutations(number))
    for tup in permutaion_list:
        permList.append(int("".join(tup)))
    return permList

def modSeven(permlist):
    modlist = []
    for i in permlist:
        if i%7 == 0:
            modlist.append(i)
    return modlist

def avrPerm(prmlist):
    minNum = min(prmlist)
    maxNum = max(prmlist)
    avrg = (minNum + maxNum)/2
    return avrg

def testCases(tests):
    num = 0
    for i in Tests:
        num += 1
        print("Test Case {}".format(num))
        permList = numberPermutation(i["num"])
        prmlist = modSeven(permList)
        avrNum = avrPerm(prmlist)
        passed = (avrNum == i["outcome"])
        print("Number: {}\nExpected Outcome: {}\nReturned Outcome: {}".format(i["num"], i["outcome"], avrNum))
        if passed:
            print("Test Case PASSED\n")
        else:
            print("Test Case FAILED\n")

def main():
    permList = numberPermutation("1867")
    prmlist = modSeven(permList)
    avrNum = avrPerm(prmlist)
    print(avrNum)

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        main()
    elif sys.argv[1] == 'sampleTest':
        testCases(Tests)
    elif sys.argv[1] == 'findAverage':
        permList = numberPermutation(sys.argv[2])
        prmlist = modSeven(permList)
        avrNum = avrPerm(prmlist)
        print(avrNum)
