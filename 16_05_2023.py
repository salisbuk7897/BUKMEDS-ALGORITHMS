import sys

#Define Test Cases
Tests = [
    {"input": [
    [0,0,0,0,1],
    [1,0,0,1,0],
    [1,0,0,1,1],
    [0,0,1,0,0],
    [1,0,0,0,0]
], "outcome": 2129920 }
]
instruction = [
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,0,0,1,0],
    [0,1,0,1,0],
    [1,1,0,1,1]
]

#Define the function to scan each minute
def scanGrid(grid):
    layout = []
    totalScore = 0
    loopGrid = grid
    newGrid = []
    t=True
    time = 0
    while t:
        #loop through grid to discover new lifeforms/empty spaces
        bottomborder = len(loopGrid)
        #print("{} Minute(S)".format("Start" if time == 0 else time))
        for i in range(bottomborder):
            #print("{} {} {} {} {}".format("X" if loopGrid[i][0]==1 else ".", "X" if loopGrid[i][1]==1 else ".", "X" if loopGrid[i][2]==1 else ".", "X" if loopGrid[i][3]==1 else ".", "X" if loopGrid[i][4]==1 else "."))
            rightborder = len(loopGrid[i])
            newOneGrid = []
            for j in range(rightborder):
                newMainGrid = 0
                leftGrid = 0
                topGrid = 0
                rightGrid = 0
                bottomGrid = 0
                mainGrid = loopGrid[i][j]
                if(j-1 < 0):
                    leftGrid = 0
                else:
                    leftGrid = loopGrid[i][j-1]
                if(i-1 < 0):
                    topGrid = 0
                else:
                    topGrid = loopGrid[i-1][j]
                if(j+1 >= rightborder):
                    rightGrid = 0
                else:
                    rightGrid = loopGrid[i][j+1]
                if(i+1 >= bottomborder):
                    bottomGrid = 0
                else:
                    bottomGrid = loopGrid[i+1][j]
                totalAdjacentNodes = topGrid+leftGrid+rightGrid+bottomGrid 
                #Lifeform Passes away except if there is exactly one adjacent lifeform
                if(mainGrid == 1 and (totalAdjacentNodes == 1)):
                    newMainGrid = 1
                elif(mainGrid == 0 and ((totalAdjacentNodes == 1) or (totalAdjacentNodes == 2))):
                #Empty Space gets new life form if one or two adjacent lifeform are present
                    newMainGrid = 1
                else:
                    newMainGrid = 0
                newOneGrid.append(newMainGrid)
            newGrid.append(newOneGrid)
        loopGrid = newGrid
        success, elem, lay = checkLayout(layout, newGrid)
        newGrid = []
        layout = lay
        if(success == "Yes" or time==86):
            t=False
            time += 1
            loopGrid = elem
            cells = lifeformScore(elem)
            print("{} Minute(S)".format("Start" if time == 0 else time))
            for i in range(len(loopGrid)):
                print("{} {} {} {} {}".format("X" if loopGrid[i][0]==1 else ".", "X" if loopGrid[i][1]==1 else ".", "X" if loopGrid[i][2]==1 else ".", "X" if loopGrid[i][3]==1 else ".", "X" if loopGrid[i][4]==1 else "."))
            for i in cells:
                score = 2**i
                print("Score = 2**{} = {}".format(i, score))
                totalScore+= score
            print("LifeForm Total Score: {}".format(totalScore))
        else:
            time += 1
    return totalScore
                
def lifeformScore(elem):
    gridNo = -1
    cells = []
    for i in range(len(elem)):
        for j in range(len(elem[i])):
            if(elem[i][j] == 1):
                gridNo += 1
                cells.append(gridNo)
            else:
                gridNo += 1
    return cells

def checkLayout(layout, ng):
    elem = []
    lay = layout
    success = "No"
    if ng in lay:
        elem = ng
        success = "Yes"
        lay.append(ng)
    else:
        lay.append(ng)
    return success, elem, lay
    
def testCases(tests):
    num = 0
    for i in tests:
        num += 1
        print("Test Case {}".format(num))
        score = scanGrid(i["input"])
        passed = (score == i["outcome"])
        print("Input: {}\nExpected Outcome: {}\nReturned Outcome: {}".format(i["input"], i["outcome"], score))
        if passed:
            print("Test Case PASSED\n")
        else:
            print("Test Case FAILED\n")

def Main():
    scanGrid(instruction)

if __name__ == "__main__":
    if(len(sys.argv) <= 1):
        Main()
    elif(sys.argv[1] == 'sampleTest'):
        testCases(Tests)

