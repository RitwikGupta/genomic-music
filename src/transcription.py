import sys

fp = sys.argv[1] #relative or absolute file path to DNA sequence
genomicData = ""

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
Write to file
'''
with open(fp + "_transcripted", "w") as out:
  out.write(genomicData)
out.close()
