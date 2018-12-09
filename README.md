# aa2nt
Convert amino acid sequence to nucleotide sequence

Based off of [this](https://www.mathworks.com/help/bioinfo/ref/aa2nt.html) MatLab program, but re-written in Python.

## Syntax

`seqNuc = aa2nt(secAA)`

## Input Arguments

| parameter | value |
|-----------|-------|
| `seqAA`   | String of one-letter amino acid codes to be converted to bases. For acceptable codes, see [Amino Acid Codes]()|

## Output Arguments

| argument | value |
|----------|-------|
| `seqNuc` | String of one-letter nucleotide base codes.|

## Amino Acid Codes

| Amino Acid | One-letter code |
|------------|-----------------|
| Alanine    | A               |
| Arginine   | R               |
| Asparagine | N               |
| Aspartic acid (Aspartate)| D |
| Cysteine   | C               |
| Glutamine  | Q               |
| Glutamic acid (Glutamate)| E |
| Glycine    | G               |
| Histidine  | H               |
| Isoleucine | I               |
| Leucine    | L               |
| Lysine     | K               |
| Methionine | M               |
| Phenylalanine| F             |
| Proline    | P               |
| Serine     | S               |
| Threonine  | T               |
| Tryptophan | W               |
| Tyrosine   | Y               |
| Valine     | V               |
| Asparagine or Aspartic acid (Aspartate)| B |
| Glutamine or Glutamic acid (Glutamate)| Z |
| Unknown amino acid| X        |
| Translation stop| *          |
| Gap        | -               |
| Other      |                 |
