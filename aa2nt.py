def aa2nt(seq):
  seq = list(seq)
  nuc = ""
  for i in seq:
    if (i == "A"):
      nuc += "GCT"
    elif (i == "R"):
      nuc += "CGC"
    elif (i == "N"):
      nuc += "AAC"
    elif (i == "D"):
      nuc += "GAT"
    elif (i == "C"):
      nuc += "TGT"
    elif (i == "Q"):
      nuc += "CAA"
    elif (i == "E"):
      nuc += "GAA"
    elif (i == "G"):
      nuc += "GGT"
    elif (i == "H"):
      nuc += "CAT"
    elif (i == "I"):
      nuc += "ATC"
    elif (i == "L"):
      nuc += "TTG"
    elif (i == "K"):
      nuc += "AAA"
    elif (i == "M"):
      nuc += "ATG"
    elif (i == "F"):
      nuc += "TTT"
    elif (i == "P"):
      nuc += "CCC"
    elif (i == "S"):
      nuc += "TCT"
    elif (i == "T"):
      nuc += "ACA"
    elif (i == "W"):
      nuc += "TGG"
    elif (i == "Y"):
      nuc += "TAT"
    elif (i == "Z"):
      nuc += "TGC"
    elif (i == "B"):
      nuc += "GAC"
    elif (i == "*"):
      nuc += "TAA"
    elif (i == "-"):
      nuc += "---"
    else:
      nuc += "???"
  
  return nuc;
