text = "X-DSPAM-Confidence:    0.8475"
cpos = text.find(':')
string = text[cpos+1:]
float = float(string)
print(float)