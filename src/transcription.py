import sys

fp = sys.argv[1] #relative or absolute file path to DNA sequence
genomicData = ""
rna = ""

'''
Split into codons
'''
with open(fp, "r") as f:
  for line in f:
    genomicData = " ".join(line[i:i+3] for i in range(0, len(line), 3))
f.close()

'''
If last codon is not a proper codon, remove
'''
if(len(genomicData[genomicData.rfind(' '):]) == 4):
  genomicData = genomicData[:genomicData.rfind(' ')]

'''
Transcription
'''
for i in range(0,len(genomicData)):
    if genomicData[i] == 'a':
        rna += 't'
    elif genomicData[i] == 't':
        rna += 'u'
    elif genomicData[i] == 'c':
        rna += 'g'
    elif genomicData[i] == 'g':
        rna += 'c'
    else:
        rna += ' '

'''
Write to file
'''
with open(fp + "_transcripted", "w") as out:
  out.write(rna)
out.close()
