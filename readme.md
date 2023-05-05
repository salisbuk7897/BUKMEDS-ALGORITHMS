## Puzzle 1: Floor Number
```File Name: 05_05_2023.py```  
The above file contains a solution to the first puzzle. it returns the floor number. It is re-usable. it can be run in 3 ways in the terminal/command prompt:
  - ```py 05_05_2023.py``` : in this case, there is only one argument which is the file name. It returns the answer to the puzzle instruction specified in the challenge document.
  - ```py 05_05_2023.py sampleTest``` : This takes the filename and another argument 'sampleTest'. This runs some sample tests specified in the challenge document as well as some edge cases. You can edit the test cases in the file to add more test cases.
  - ```py 05_05_2023.py find '<><<>>>'``` : This takes the filename, 'find' aregument and a string of floor instructions. It returns the floor number based on the floor instruction specified in the terminal.

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