import sys

digits = [
    '   \n'
    '  |\n'
    '  |\n'
    ,
    ' _ \n'
    ' _|\n'
    '|_ \n'
    ,
    ' _ \n'
    ' _|\n'
    ' _|\n'
    ,
    '   \n'
    '|_|\n'
    '  |\n'
    ,
    ' _ \n'
    '|_ \n'
    ' _|\n'
    ,
    ' _ \n'
    '|_ \n'
    '|_|\n'
    ,
    ' _ \n'
    '  |\n'
    '  |\n'
    ,
    ' _ \n'
    '|_|\n'
    '|_|\n'
    ,
    ' _ \n'
    '|_|\n'
    ' _|\n'
    ]

digit = ''
for line in sys.stdin:
    digit = digit + line

print repr(digit)
