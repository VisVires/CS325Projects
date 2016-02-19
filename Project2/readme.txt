Project 2: Coin Change
Group 11: Karen Thrasher, Kyle Livermore, William George

Files:
coin.py - main implementation of coin change code
stub.py - testing environment and contains code for 
          test cases from project assignment

******************************************
            INSTRUCTIONS
******************************************
To run code on input file:
python coin.py -i inputFileName
		Ex. python coin.py -i Coin1
	Note: Do not add .txt extension on input file
	Produces file: inputFileNamechange.txt
		Ex. Coin1change.txt
	Note: Input file should not contain any blank lines

To run code for problems 4-6:
python coin.py --minCoin
	Produces files: 8 labeled files corresponding to each problem
	Note: Takes a while to run and generate data

To utilize runTimeData to generate data for problem 7:
python coin.py --runTimeData
	Produces file: runTime.csv
	Note: Takes a while to run and generate data

To utilize denominationsTime to generate data for problem 8:
python coin.py --denominationsTime
	Note: Takes a while to run and generate data

General run notes - engineering server FLIP:
python coin.py
	Runs main program
python stub.py 
	Runs test cases from "Testing for Correctness" part of assignment