Genomic Music
=============

Making music from a genome. The genome should be provided as raw data (i.e., TCAGATCAA...)  

Prerequisites
=============

Install `Biopython`  
Install `Lilypond`. The executable shell script is included in the `prereq` folder.  

How to use
==========

Have a one line text file that is a lower-case DNA sequence in the `genomicData` folder  
`cd` to the `src` folder  
Run `python tranlation.py ../genomicData/[FileName]`  
Run `python music.py ../genomicData/[FileName + "_translated"] [Title] [Composer] [TagLine] > ../music.ly`  
Run `lilypond ../music.ly`  

Open `music.pdf` and look at your sheet music
