cp syms.txt symsi.txt
echo "XXX	5004" >> symsi.txt
str="'$*'"
echo $str > z.txt
python3 drawfst.py > temp.txt

fstcompile --isymbols=symsi.txt --osymbols=syms.txt temp.txt F.fst


fstcompose F.fst L.fst FoL.fst     



fstshortestpath FoL.fst | fstprint --isymbols=symsi.txt --osymbols=syms.txt > final.txt




python3 getanswer.py
