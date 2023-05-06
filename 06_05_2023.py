import sys

# def modul(a, speed, runtime, rest):
#     rnd = runtime + rest
#     print(rnd)
#     mod = a % rnd
#     print(mod)
#     divNumber = a - mod
#     print(divNumber)
#     rounds = divNumber/rnd
#     print(rounds)
#     if mod <= runtime:
#         run = (rounds * (runtime * speed)) + (mod * speed)
#     elif mod <= rnd:
#         run = (rounds * (runtime * speed)) + (runtime * speed)
#     print(int(run))
#     print("-----------")

# def findDistance(name, racetime):
#     run = 0
#     remTime = racetime
#     for i in Runners:
#         if(i["name"] == name):
#             runner = i
#             speed = i["Speed"]
#             runtime = i["runtime"]
#             rest = i["rest"]
#             while True:
#                 if remTime <= 0:
#                     break
#                 else:
#                     if remTime <= 0 or remTime <= runtime:
#                         run += remTime * speed
#                         break
#                     else:
#                         remTime -= runtime
#                         run += runtime * speed
#                         remTime -= rest
#                         if remTime <= 0:
#                             break
#                         else:
#                             continue
#     print(run)

#Define Runners
Runners = [
    {"name": "John", "Speed": 10, "runtime": 6, "rest": 20 },
    {"name": "James", "Speed": 8, "runtime": 8, "rest": 25 },
    {"name": "Jenna", "Speed": 12, "runtime": 5, "rest": 16 },
    {"name": "Josh", "Speed": 7, "runtime": 7, "rest": 23 },
    {"name": "Jacob", "Speed": 9, "runtime": 4, "rest": 32 },
    {"name": "Jerry", "Speed": 5, "runtime": 9, "rest": 18 },
]
#Define Test cases
Tests = [
    {"name":"John", "racetime": 8, "outcome": 60},
    {"name":"James", "racetime": 8, "outcome": 64},
    {"name":"John", "racetime": 100, "outcome": 240},
    {"name":"James", "racetime": 100, "outcome": 200},
]

#define the findDistance function
def findDistance(name, racetime):
    run = 0
    remTime = racetime
    for i in Runners:
        if(i["name"] == name):
            speed = i["Speed"]
            runtime = i["runtime"]
            rest = i["rest"]
            rnd = runtime + rest
            mod = racetime % rnd
            divNumber = racetime - mod
            rounds = divNumber/rnd
            if mod <= runtime:
                run = (rounds * (runtime * speed)) + (mod * speed)
            elif mod <= rnd:
                run = (rounds * (runtime * speed)) + (runtime * speed)
    return int(run)
    
#define the race function
def race(runners, racetime):
    for i in runners:
        distance = findDistance(i["name"], racetime)
        print('{} {}m'.format(i["name"], distance))

#define the racelead function
def raceLead(runners, racetime):
    leaderboard ={}
    for i in runners:
        distance = findDistance(i["name"], racetime)
        leaderboard[i["name"]] = distance
    maxim = max(zip(leaderboard.values(), leaderboard.keys()))
    print('{} {}m'.format(maxim[1], maxim[0]))

#define Testcase function
def testCases(tests):
    num = 0
    for i in tests:
        num += 1
        print("Test Case {}".format(num))
        distance = findDistance(i['name'], i["racetime"])
        passed = distance == i['outcome']
        print('Racer: {} \nRace Time: {}\nExpected Distance: {}\nReturned Distance: {}'.format(i['name'], i["racetime"], i['outcome'], distance ))
        if passed:
            print("Test Case PASSED\n")
        else:
            print("Test Case FAILED\n")

def main():
    raceLead(Runners, 1234)

if __name__ == '__main__':
    if(len(sys.argv) <= 1):
        main()
    elif(sys.argv[1] == 'sampleTest'):
        testCases(Tests)
    elif(sys.argv[1] == 'race'):
        try:
            race(Runners, int(sys.argv[2]))
        except:
            print("An Exception occured. try 'py 06_05_2023.py race 12345'.")
    elif(sys.argv[1] == 'raceLeader'):
        try:
            raceLead(Runners, int(sys.argv[2]))
        except:
            print("An Exception occured. try 'py 06_05_2023.py raceLeader 14'.")

#testCases(Tests)
#raceLead(Runners, 1234)
#findDistance("James", 100)
#findDistance("John", 100)
#modul(1234, 8, 8, 25)
#modul(1234, 10, 6, 20)


