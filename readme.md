## Puzzle 1: Floor Number
```File Name: 05_05_2023.py```  
The above file contains a solution to the first puzzle. it returns the floor number. It is re-usable. it can be run in 3 ways in the terminal/command prompt:
  - ```py 05_05_2023.py``` : in this case, there is only one argument which is the file name. It returns the answer to the puzzle instruction specified in the challenge document.
  - ```py 05_05_2023.py sampleTest``` : This takes the filename and another argument 'sampleTest'. This runs some sample tests specified in the challenge document as well as some edge cases. You can edit the test cases in the file to add more test cases.
  - ```py 05_05_2023.py find '<><<>>>'``` : This takes the filename, 'find' argument and a string of floor instructions. It returns the floor number based on the floor instruction specified in the terminal.

Puzzle 1 floor instruction in the document
```
<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<
<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><
<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>
<>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>
<><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><
><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<
><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><
<<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>
<><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><
<>><<>><<>><
```

Answer to Puzzle 1
```
56
```

## Puzzle 2: Distance of Winning Runner
```File Name: 06_05_2023.py```  
The above file contains a solution to the second puzzle. it returns the distance of the winning runner in 1234 seconds. It uses modulus to calculate the number of rounds(running + racetime) and the remaining seconds(out of which another runtime is deducted). it can be run in 4 ways in the terminal/command prompt:
  - ```py 06_05_2023.py``` : in this case, there is only one argument which is the file name. It returns the answer to the puzzle instruction specified in the challenge document. which is the distance of the winning runner in 1234 seconds.
  - ```py 06_05_2023.py sampleTest``` : This takes the filename and another argument 'sampleTest'. This runs some sample tests specified in the challenge document as well as some edge cases. You can edit the test cases in the file to add more test cases.
  - ```py 06_05_2023.py race 1234``` : This takes the filename, 'race' argument and a racetime in seconds. It returns the distance of all the runners.
  - ```py 06_05_2023.py raceLeader 1234``` : This takes the filename, 'raceLeader' argument and a racetime in seconds. It returns the distance of winning runner.

Puzzle 2 distance of winning runner instruction in the document
```
1) John can run 10 m/s for 6 seconds, but then must rest for 20 seconds
2) James can run 8 m/s for 8 seconds, but then must rest for 25 seconds
3) Jenna can run 12 m/s for 5 seconds, but then must rest for 16 seconds
4) Josh can run 7 m/s for 7 seconds, but then must rest for 23 seconds
5) Jacob can run 9 m/s for 4 seconds, but then must rest for 32 seconds
6) Jerry can run 5 m/s for 9 seconds, but then must rest for 18 seconds

After 1234 seconds, what is the distance of the winning runner?
```

Answer to Puzzle 2
```
Jenna 3540m
```

## Puzzle 3: Average of Permutation numbers divisible by 7
```File Name: 08_05_2023.py```  
The above file contains a solution to the third puzzle. it returns the Average of max and min permutation numbers of 1867 divisible by 7.  it can be run in 4 ways in the terminal/command prompt:
  - ```py 08_05_2023.py``` : in this case, there is only one argument which is the file name. It returns the answer to the puzzle instruction specified in the challenge document. Average of max and min permutation numbers of 1867 divisible by 7.
  - ```py 08_05_2023.py sampleTest``` : This takes the filename and another argument 'sampleTest'. This runs some sample tests specified in the challenge document as well as some edge cases. You can edit the test cases in the file to add more test cases.
  - ```py 06_05_2023.py findAverage 1234``` : This takes the filename, 'findAverage' argument and a number. It returns the Average of max and min permutation numbers of the given number which are divisible by 7.

Puzzle 3 instruction in the document
```
What you’ll need to do is determine if any of the permutations of 1867 are divisible by 7, and
if so, what is the average between the smallest and largest permutation? Decimals are
allowed.
```

Answer to Puzzle 3
```
5152.0
```

## Puzzle 4: Minimum Cost of Paired Workers
```File Name: 10_05_2023.py```  
The above file contains a solution to the fourth puzzle. it returns the Minimum cost of paired workers based on the efficiencies given in the instruction document.  it can be run in 2 ways in the terminal/command prompt:
  - ```py 10_05_2023.py``` : in this case, there is only one argument which is the file name. Returns minimum cost of paired workers based on the efficiencies given in the instruction document.
  - ```py 10_05_2023.py sampleTest``` : This takes the filename and another argument 'sampleTest'. This runs some sample tests specified in the challenge document as well as some edge cases. You can edit the test cases in the file to add more test cases.

Puzzle 4 instruction in the document
```
What is the minimum cost of this array of efficiencies:
[1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]
```

Answer to Puzzle 4
```
Minimum Cost = 539
```

## Puzzle 6: Minimum Number of Steps
```File Name: 14_05_2023.py```  
The above file contains a solution to the sixth puzzle. it returns the minimum number of steps needed to disconect a series of nodes under threat in a network based on the instruction given in the instruction document.  it can be run in 3 ways in the terminal/command prompt:
  - ```py 14_05_2023.py``` : in this case, there is only one argument which is the file name. Returns minimum number of steps needed to disconect a series of nodes under threat in a network based on the instruction given in the instruction document.
  - ```py 14_05_2023.py sampleTest``` : This takes the filename and another argument 'sampleTest'. This runs some sample tests specified in the challenge document as well as some edge cases. You can edit the test cases in the file to add more test cases.
  - ```py 14_05_2023.py minSteps aabbbccaabbbddd``` : This takes the filename, 'minSteps' argument and a number. It returns minimum number of steps needed to disconect a series of nodes under threat in a network based on the series given in the terminal.

Puzzle 6 instruction in the document
```
What is the minimum number of steps required to delete this series:
“kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhi
gtefhgbjkkkknbmssdsdsfdvneurghiueor”
```

Answer to Puzzle 6
```
Minimum Number of Steps: 82
```