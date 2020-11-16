file = input('Enter the file name: ')
fhand= open(file)
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
