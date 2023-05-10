import sys
import itertools

#define Test Cases
Tests = [
    {"eff": [4, 2, 8, 1, 9], "outcome" : 2 },
    {"eff": [1, 2, 4], "outcome" : 1 },
]

efficiency_inatruction = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

#define the efficiency function
def getPair(eff):
    cost = 0
    possible = len(eff) - 1
    num_of_pairs = possible/2
    #print(num_of_pairs)
    cst = {}
    for each in itertools.permutations(eff,2):
        price = each[0]- each[1]
        if(price >= 0):
            cst[each] = price
    sorted_cst = sorted(cst.items(), key=lambda x:x[1])
    #print(sorted_cst)
    for i in range(0,int(num_of_pairs)):
        cost += sorted_cst[i][1]
    #print("cost: {}".format(cost))
    return cost

#define function for test cases
def testCases(tests):
    num = 0
    for i in tests:
        num += 1
        print("Test Case {}".format(num))
        minCost = getPair(i["eff"])
        passed = (minCost == i["outcome"])
        print("Efficiency: {}\nExpected Outcome: {}\nReturned Outcome: {}".format(i["eff"], i["outcome"], minCost))
        if passed:
            print("Test Case PASSED\n")
        else:
            print("Test Case FAILED\n")

#define Main Function
def main():
    mincost = getPair(efficiency_inatruction)
    print("Minimum Cost = {}".format(mincost))

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        main()
    elif(sys.argv[1] == 'sampleTest'):
        testCases(Tests)
