import sys
#define test cases
Tests = [
    {"input": "aabbbcccaacccaa", "outcome":4},
    {"input": "aabbaa", "outcome": 2}
] 

challenge_instruction = """kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"""

#Define function to get minimum number of steps
def numberOfSteps(series):
    wordd = series #copy series(network) to variable word
    t = True #Initialize loop condition
    count = 0 #Initialize a variable count for number of steps
    num = 1 # initialize number of network that fall between 2 similar networks(e.g 'g' and 'g') in the series to check. starting with 1(e.g 'fjf')
    lenword = 0 #Initialize len of wordd
    rounds = 20 #Set number of round to loop the series at a single time
    while t: 
        #print(num)
        if(len(wordd) <= 0):
            break
        for i, j in enumerate(wordd):
            if((i+num+1) <= (len(wordd) - 1) and j != wordd[i+1] and j == wordd[i+num+1]):
                sepCount = 0
                startword = ""
                endword = ""
                intercept = wordd[i:i+num+2]
                if (i+num+2 <= (len(wordd)-1)):
                    endword = wordd[i+num+2:]
                if (i>1):
                    startword = wordd[:i]
                #print(intercept, startword, endword) #break work into start, intercept and end components. intercept is the network series of intrest from which to remove a middle character(s) so that we can get two networks close to each other
                uniqlist= {}
                uniq1 = set(intercept)
                for f in range(len(uniq1)):
                    ltr1 = uniq1.pop()
                    uniqlist[ltr1] = [int(i1) for i1, j1 in enumerate(intercept) if j1 == ltr1]
                # check if networks are cuncurrent in the intercept before removing
                uniq = set(intercept)
                getLen = len(uniq)
                for y in range(getLen):
                    ltr = uniq.pop()
                    ltrlist = uniqlist[ltr]
                    if len(ltrlist) == 1 and ltr !=j:
                        intercept = intercept.replace(ltr, "")
                        sepCount += 1
                    elif len(ltrlist) == 2 and (ltrlist[1]-ltrlist[0] == 1) and ltr !=j:
                        intercept = intercept.replace(ltr, "")
                        sepCount += 1
                    elif len(ltrlist) > 2:
                        c = False
                        for k in range(len(ltrlist)):
                            if k+1 < len(ltrlist) and ltrlist[k+1]-ltrlist[k] != 1:
                                c = True
                                #print("ltr: {}, ltrlist: {}".format(ltr, ltrlist))
                                break
                        if c == False:
                            intercept = intercept.replace(ltr, "")
                            sepCount += 1
                    # if(ltr != j):
                    #     intercept = intercept.replace(ltr, "")
                    #     count += 1
                #print(sepCount)
                count += sepCount
                #reconstruct the word(network series) after removing the characters of interest and noting the count(number of networks removed)
                wordd = startword+intercept+endword
                break
            elif((i+num+2) >= (len(wordd) - 1)):
                if num == rounds:
                    if lenword == len(wordd):
                        #print(wordd, count)
                        uniq = set(wordd)
                        #print(len(uniq))
                        for z in range(len(uniq)):
                            ltr = uniq.pop()
                            wordd = wordd.replace(ltr, "")
                            count += 1
                        wordd = wordd
                        #t = False
                        break
                    else:
                        num = 1
                        lenword = len(wordd)
                        break
                else:
                    #print("reached")
                    num += 1
                    did = False
                    break

    return count

def Main():
    minNum = numberOfSteps(challenge_instruction)
    print("Minimum Number of Steps: {}".format(minNum))

def testCases(tests):
    num = 0
    for i in tests:
        num += 1
        print("Test Case: {}".format(num))
        minNum = numberOfSteps(i["input"])
        passed = (minNum == i["outcome"])
        print("Input: {}\nExpected Outcome: {}\nReturned outcome: {}".format(i["input"], i["outcome"], minNum))
        if passed:
            print("Test Case PASSED\n")
        else:
            print("Test Case FAILED\n")



if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        Main()
    elif sys.argv[1] == 'sampleTest':
        testCases(Tests)
    elif sys.argv[1] == 'minSteps':
        minSteps = numberOfSteps(sys.argv[2])
        print("Minimum Number of Steps: {}".format(minSteps))