# sungoku
A sudoku creator and solver in python that is able to create sudokus in machine and human-readable format.

There are no external dependencies apart from python3.

## Usage

Generate ten sudokus with at least 30 hints as csv:
```
./sungoku.py create --number 10  --min-hints 30
# quiz,num_hints,difficulty
# 040006000000907008159030040038000120010002000900000005060020007080409030090063450,30,MEDIUM
# 087000051640000000050708302000000000000072000706450109005809000079540003012000005,30,EASY
# 036020070000608010801000000602004150000090460000002003209000031007013096083000000,30,HARD
# ...
```
Generate a sudoku in human-readable format:
```
./sungoku.py create --pretty
#     4 | 6   1 | 9    
#       |       |   8  
# 1 6   | 8 7   |      
# - - - + - - - + - - -
#       |   4   |      
# 6 1   |     2 |      
# 2   9 | 7     |     3
# - - - + - - - + - - -
#       |       | 1    
# 7     | 1     |   3 2
# 3     |   8   | 7 6  
#
# Number of hints: 26
# Difficulty: MEDIUM
```
Solve a list of sudokus from a file and check if it is minimal and a unique solution exists:
```
./sungoku.py solve -a  < some_file.csv
```
Do a whole Sunday afternoon worth of sudokus within a matter of seconds, so you can go back and watch your favourite sitcom:
```
./sungoku.py create -n 8 | ./sungoku.py solve -p > /dev/null
```
