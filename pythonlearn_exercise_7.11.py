# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. 
# Executing the program will look as follows:

# file = input('insert file: ')
# fhand= open(file)
# for line in fhand:
    # ucase = line.upper()
    # print(ucase)




# Q2   
# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form: 
# X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.



file = input('Enter the file name: ')
fhand= open('file')
count= 0
r_sum=0
for line in fhand:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):        
        count = count + 1
        r_sum= r_sum + float(line[19:])
# print(summ)
# print('Number of lines: ',count)
        avg= r_sum/count
print('Average spam confidence: ', avg)