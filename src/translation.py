'''
DNA to Amino Acid
'''

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import sys

if len(sys.argv) != 2:
    print "\nThe proper usage of this program is:\n python music.py [Path to protein seq]\n"
    sys.exit(0)

fp = sys.argv[1] #relative or absolute file path to DNA sequence
genomicData = ""
protein = ""

'''
Read DNA
'''
with open(fp, "r") as f:
  for line in f:
    genomicData = "".join(line[i:i+3] for i in range(0, len(line), 3))
f.close()

'''
Trim DNA to multiple of 3
'''
while(len(genomicData) % 3 != 0):
    genomicData = genomicData[:len(genomicData) - 1]

coding_dna = Seq(genomicData, IUPAC.unambiguous_dna)
protein = coding_dna.translate(stop_symbol='') #So there is no stop codon

'''
Write to file
'''
with open(fp + "_translated", "w") as out:
  out.write(str(protein))
out.close()
