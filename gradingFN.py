"""
TITLE: gradingFN.py
AUTHOR: Mhealyssah Bustria
DATE CREATED: Fri 18 Sep 2020
MODIFIED: Sun 09 May 2021
"""

'''
PURPOSE: open a file and make a list of all lines
PARAMETERS:
- infileName: the name of the file to open
RETURN VALUES:
- fileLines
'''
def get_file_lines(infileName):
    print("Reading the file lines. . .")
    infile = open(infileName, 'r')
    fileLines = infile.readlines() # make a list of all lines
    infile.close()
    return fileLines
# end of FN

'''
PURPOSE: print the result of one stuent
PARAMETERS:
- lineNumber: the number of the line in the transcript
- outfile: the file to write to
- lineContent: one line of the transcript
'''
def write_student_result(list_number, outfile, content):
    outfile.write(str(list_number) + " ") # line number

    
    outfile.write(content[1] + ", ")
    outfile.write(content[0] + " ")

    email = content[2] + "@mascot.school.edu"
    outfile.write("\n\t" + email + "\n")
# end of FN

'''
PURPOSE: write grade results
PARAMETERS:
- list_number: the number of students who are to be written
- outfile: the file to write to
- lineContent: one line of the grade records
'''
def write_results(infile_content, outfile): 
    list_number = 0
    # for loop to print the input file line by line
    for line_content in infile_content:
        # if the grade is to be written
        split_content = line_content.split(',')
        if split_content[3] == "0\n":
            list_number += 1
            write_student_result(list_number, outfile, split_content)
    
    if list_number == 0:
        outfile.write( "No students were missing a submission." )
# end of FN