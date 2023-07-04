# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
floatvaltotal = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        cpos = line.find(':')
        value = line[cpos+1:]
        floatval = float(value)
        count = count + 1
        floatvaltotal = floatvaltotal + floatval
        average = floatvaltotal / count
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        
print('Average spam confidence:', average )