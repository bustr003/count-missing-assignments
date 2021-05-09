"""
TITLE: main.py
AUTHOR: Mhealyssah Bustria
DATE CREATED: Fri 18 Sep
MODIFIED: Sun 09 May 2021
"""

# OPENING STATEMENTS
program = "grading"
print( '=== ' + program + ' ===' )

# MODULES
import time as t
#custom modules
import gradingFN as fn

# files to use
infile = 'grades.csv'
outfile = 'missing_submissions.txt'

# Get assignment name
assignName = input("Enter the name of the assignment: ")

# open the input file (the transcript) and create a list to hold each line
print('Grades will be read from', infile, ". . .")
records = fn.get_file_lines(infile)

# open the output file (to hold the grading results)
results = open(outfile, 'w') #'w' means overwrite existing content
print('Results will be written to', outfile, ". . . ")

t0 = t.time() # start timer
results.write("=== " + assignName + " - missing submissions ===\n")

# write the grading results
fn.write_results(records, results)

results.close() #close the output file
print('DONE.\nCheck the re-written', outfile)

# ENDING STATEMENTS
t1 = t.time()
print( 'time to run: ', t1-t0, ' seconds' )
print( '=== ' + program + ' end ===' )

#EOF grading.py