"""
TITLE: grading.py
AUTHOR: Mhealyssah Bustria
DATE CREATED: Fri 18 Sep
"""

#OPENING STATEMENTS
program = "grading"
print( '===' + program + '===' )

#MODULES
import time as t
#custom modules
import gradingFN as fn

#start timer
t0 = t.time()

#files to use
infile = 'grades.csv'
outfile = 'missing_submissions.txt'

#open the input file (the transcript) and create a list to hold each line
print('grades will be read from', infile)
records = fn.get_file_lines(infile)

#open the output file (to hold the grading results)
print('results will be written to', outfile)
results = open(outfile, 'w') #'w' means overwrite existing content

#write the grading results
#results.write(infile_name[:-4] + "\n")
results.write("=== list of missing submissions ===\n")
fn.write_results(records, results)

results.close() #close the output file
print('DONE. check the re-written', outfile)

#ENDING STATEMENTS
t1 = t.time()
print( 'time to run: ', t1-t0, ' seconds' )
print( '===' + program + ' end===' )
#EOF srtbot.py