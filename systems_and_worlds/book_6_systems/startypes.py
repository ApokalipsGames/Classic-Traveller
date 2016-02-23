# startypes.py
# collection of lists containing star type data

# subdwarf type stars (5 rows x 8 columns)
type_SD = [['I', 'I', 'I', 'I', 'O', 'O', 'O', 'O'],
          ['I', 'I', 'H', 'H', 'O', 'O', 'O', 'O'],
          ['I', 'H', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['H', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

# white dwarf type stars (5 rows x 6 columns) [5][6]
type_WD = [['H', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O']]

# bright supergiant stars (15 rows x 13 cols)
#           B0   B5   A0   A5   F0   F5   G0   G5   K0   K5   M0   M5   M9
type_Ia = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
           ['_', '_', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', '_', '-', '-', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', '_', '_', '-', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', 'I', 'I', '_', '_', '_', '_', '-', '-', '-'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-'],
           ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'I', 'I', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'H', 'H', 'H', 'H', 'O', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
           ['H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

# weaker supergiant stars (15 x 13)
#           B0   B5   A0   A5   F0   F5   G0   G5   K0   K5   M0   M5   M9
type_Ib = [['_', '_', '_', '_', '_', '-', '-', '-', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', '_', '_', '-', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', 'I', 'I', '_', '_', '-', '-', '-', '-'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '_', '-', '-', '-'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-', '-'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-'],
           ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'H', 'H', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I'],
           ['I', 'H', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'H', 'H', 'I', 'I'],
           ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'H', 'H'],
           ['H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

# bright giant stars (14 x 13)
#           B0   B5   A0   A5   F0   F5   G0   G5   K0   K5   M0   M5   M9
type_II = [['_', '_', '_', '_', '_', '_', '_', '_', '-', '-', '-', '-', '-'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '-', '-', '-', '-'],
           ['_', '_', '_', 'I', 'I', 'I', 'I', 'I', 'I', '_', '-', '-', '-'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-', '-', '-'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-', '-'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-', '-'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'H', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'H', 'H', 'I', 'I', 'I'],
           ['I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'H', 'I', 'I'],
           ['I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'H', 'H'],
           ['H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

# giant stars (14 x 13)
#           B0   B5   A0   A5   F0   F5   G0   G5   K0   K5   M0   M5   M9
type_III= [['_', '_', '_', 'I', 'I', 'I', 'I', 'I', 'I', '_', '_', '-', '-'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '_', '-', '-'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-', '-'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-', '-'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', '-'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['_', 'I', 'I', 'I', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'I', 'H', 'O', 'O', 'O', 'H', 'H', 'I', 'I', 'I', 'I'],
           ['I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'H', 'H', 'I', 'I'],
           ['I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'H', 'H'],
           ['I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

# subgiant stars (14 x 9)
#           B0   B5   A0   A5   F0   F5   G0   G5   K0   K5   M0   M5   M9
type_IV = [['_', '_', '_', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
           ['_', 'I', 'I', 'I', 'I', 'H', 'H', 'H', 'O'],
           ['_', 'I', 'I', 'H', 'H', 'O', 'O', 'O', 'O'],
           ['I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

# main sequence stars (14 x 13)
#           B0   B5   A0   A5   F0   F5   G0   G5   K0   K5   M0   M5   M9
type_V = [['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'H', 'H', 'O', 'O'],
          ['_', '_', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O'],
          ['_', '_', 'I', 'I', 'I', 'I', 'I', 'H', 'H', 'O', 'O', 'O', 'O'],
          ['_', 'I', 'I', 'I', 'I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['_', 'I', 'I', 'I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['_', 'I', 'I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['I', 'I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['I', 'I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['I', 'H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['H', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]