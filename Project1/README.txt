Code can produce two separate outcomes.  It can run on the test cases or it can produce 
a .CSV file of the data. 

To run on engineering server FLIP:

To run test cases:
python project1.py -i NAME-OF-INPUT-FILE -o NAME-OF-OUTPUT-FILE
ex. python project1.py -i MSS_Problems.txt -o MSS_Results.txt

Note: Input data must be in array form [1, 2, ... , n] with each array on a new line.

To generate .CSV file:
python project1.py --runTimeData