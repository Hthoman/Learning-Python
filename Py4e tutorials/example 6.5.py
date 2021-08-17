text = "X-DSPAM-Confidence:    0.8475"
startpos=text.find('0')
endpos=text.find('5',startpos)
output=text[startpos : endpos+1]
float(output)
print(output)
