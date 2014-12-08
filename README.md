Genomic Music
=============

Making music from a genome. The genome should be provided as raw data (i.e., TCAGATCAA...)  

Prerequisites
=============

Install `Biopython` by `pip install biopython`  
Install `Lilypond`. The executable shell script is included in the `prereq` folder.  

How to use
==========

Have a one line text file that is a lower-case DNA sequence in the `genomicData` folder. The file for the oxytocin receptor for H. Sapiens is included   
`cd` to the `src` folder  
Run `python tranlation.py ../genomicData/[FileName]`  
Run `python music.py ../genomicData/[FileName + "_translated"] [Title] [Composer] [TagLine] > ../music.ly`  
Run `lilypond ../music.ly`  
Run `timidity music.midi -Ow -o - | lame - -b 64 music.mp3`  

Open `music.pdf` and look at your sheet music or play `music.mp3` and listen to it.  
