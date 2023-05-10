import sys
import itertools

#define Test Cases
Tests = [
    {"eff": [4, 2, 8, 1, 9], "outcome" : 2 },
    {"eff": [1, 2, 4], "outcome" : 1 },
]

eff1 = [4, 2, 8, 1, 9]
eff2 = [1, 2, 4]
efficiency_inatruction = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]

#define the efficiency function
def getPair(eff):
    workers = {}
    pair = []
    cost = 0
    possible = len(eff) - 1
    num_of_pairs = possible/2
    #print(num_of_pairs)
    cst = {}
    for each in itertools.permutations(eff,2):
        price = abs(each[0]- each[1])
        #if(price >= 0):
        cst[each] = price
    sorted_cst = sorted(cst.items(), key=lambda x:x[1])
    sorted_pair = sorted(cst.items(), key=lambda x:x[1])
    #print(sorted_pair)
    for i in sorted_pair:
        if len(workers) == 0:
            workers[i[0]] = i[1]
        else:
            d = ""
            for j in workers:
                #print("j0: {}, j1: {}, i0: {}, i1: {}, j1i0: {}".format(j[0],i[0][0], j[1],i[0][1], (int(j[1]) != int(i[0][0]))))
                if((int(j[0]) != int(i[0][0])) and (int(j[0]) != int(i[0][1])) and (int(j[1]) != int(i[0][0])) and (int(j[1]) != int(i[0][1]))):
                    d = "!found"
                else:
                    d = "found"
                    break
            if(d == "!found"):
                workers[[i][0][0]] = i[1]
        #print("done")
    sorted_workers = sorted(workers.items(), key=lambda x:x[1])
    #print(len(sorted_workers))
    #print(sorted_workers)
    for i in sorted_workers:
        #print(i[1])
        cost += i[1]
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
