import sys

if(len(sys.argv) != 5):
    print "\nThe proper usage of this program is:\n python music.py [Path to protein seq] [Title] [Composer] [Tagline]\n"
    sys.exit(0)

notes = {
  'A':("<c a>2 ", "<e' a'>2 "),
  'C':("g2 ", "d'4 e' "),
  'D':("e2 ", "e'4 a' "),
  'E':("<c g>2 ", "a'4 <a' c'> "),
  'F':("a2 ", "<g' a'>4 c'' "),
  'G':("a2 ", "<g' a'>4 a' "),
  'H':("r4 g ", " r4 g' "),
  'I':("<c e>2 ", "d'4 g' "),
  'j':("a4 a ", "g'4 g' "),
  'K':("a2 ", "<g' a'>4 g' "),
  'L':("e4 g ", "a'4 a' "),
  'M':("c4 e ", "a'4 g' "),
  'N':("e4 c ", "a'4 g' "),
  'P':("a2 ", "e'4 <e' g'> "),
  'Q':("a2 ", "a'4 a' "),
  'R':("g4 e ", "a'4 a' "),
  'S':("a2 ", "g'4 a' "),
  'T':("g2 ", "e'4 c' "),
  'V':("e4 e ", "a'4 c' "),
  'W':("e4 a ", "a'4 c' "),
  'Y':("<c g>2  ", "<a' g'>2")
}

proteinSeq = ""
fp = sys.argv[1]
title = sys.argv[2]
composer = sys.argv[3]
tagLine = sys.argv[4]

with open(sys.argv[1], "r") as protein:
    for line in protein:
        proteinSeq = line

upper_staff = ""
lower_staff = ""
for i in proteinSeq.upper():
    (l,u) = notes[i]
    upper_staff += u
    lower_staff += l

staff = "{\n\\new PianoStaff << \n"
staff += "  \\new Staff {" + upper_staff + "}\n"
staff += "  \\new Staff { \clef bass " + lower_staff + "}\n"
staff += ">>\n}\n"

title = "\header { title = \"" + str(title) + "\" composer = \"" + str(composer) + "\" tagline = \"" + str(tagLine) + "\" }"

print title + staff
