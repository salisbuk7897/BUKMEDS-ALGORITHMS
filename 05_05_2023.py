import sys
import json
# Define Some Test Cases
Tests = [
    {"input":"<<>>", "output": 0 },
    {"input":"<><>", "output": 0 },
    {"input":"<<<", "output": 3 },
    {"input":">><<<>>", "output": -1 },
    {"input":"", "output": 0 },
    ]

# The Challenge Floor Instruction
instruction= """<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<
<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><
<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>
<>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>
<><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><
><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<
><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><
<<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>
<><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><
<>><<>><<>><"""

# Define a function to finf floor
def findFloor(input):
    floor = 0
    for i in input: # loop through input/floor instruction
        if(i == "<"):
            floor += 1 # move up if sign says <
        elif(i == ">"):
            floor -= 1 # move 1 floor down if the sign says >
    return floor # return floor number

# define a function to test cases
def testCases(Tests):
    num = 0 # Case Number
    for i in Tests: #Loop through the test
        num += 1 # Increase case number by 1 
        print("Running TEST CASE: {}".format(num))
        returnedFloor = findFloor(i["input"]); # Call findFloor() function and save result
        passed = returnedFloor == i["output"] # Compare returned floor with expected output
        print("Expected Outcome: {} \nReturned Outcome: {}".format(i["output"] ,returnedFloor))
        if(passed):
            print("Test Case PASSED\n")
        else:
            print("Test Case FAILED\n")

def main():
    print(findFloor(instruction))

if __name__ == "__main__": # Main entry point
    if(len(sys.argv) <= 1): # If the only argument is file name
        main()  # Run main function
    elif (sys.argv[1] == "sampleTest"): # If user specified a second argument "sampleTest"
        testCases(Tests) # Run Sample Test function
    elif (sys.argv[1] == "find"):  # If a user specified a second argument 'find', followed by string of floorInstructions
        try:
            print(findFloor(sys.argv[2])) # Find the floor number
        except:
            print("Please enter a floor instruction. e.g '<<>>><<><>'")