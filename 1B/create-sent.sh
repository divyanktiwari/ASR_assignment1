

python3 drawfst1.py $1 $2 $3 $4 | fstcompile --isymbols=syms.txt --osymbols=syms.txt > F1.fst #created fst for condition for w2 following w1


python3 drawfst2.py $1 $2 $3 $4 | fstcompile --isymbols=syms.txt --osymbols=syms.txt > F2.fst # created fst for the condition that w3 and w4 can be anywhere



fstconcat F1.fst F2.fst T.fst     # concatinated both fsts to get both the conditions satisfied
 
fstcompose T.fst L.fst K.fst  # composed the final constraint fst with L.fst


fstshortestpath K.fst | fstprint --isymbols=syms.txt --osymbols=syms.txt > final1.txt # storing the shortest path in a file

python3 form_sent.py  # creates sentence based onoutput in final1.txt
