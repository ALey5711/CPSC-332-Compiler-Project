FILE_PATH = 'final25.txt'


lines_to_ignore = [
    'program s2025 ;', 'Program s2025 ;', 'PROGRAM S2025 ;', 'PROGRAM s2025 ;',
    'var', 'VAR', 'Var',
    'begin', 'Begin', 'BEGIN',
    'a1 , b2s , ar , bb : integer ;', 'A1, B2S, AR, BB : integer ;', 'a1,b2s,ar,bb:integer;',
    'A1,B2S,AR,BB:integer;',
    'end', 'END', 'End'
]

def lineConversion(FILE_PATH):
    with open(FILE_PATH, 'r') as file:
        with open('project2025.py','w', encoding = 'UTF-8') as outfile:
            for line in file:
                if any(phrase in line for phrase in lines_to_ignore):
                    continue
                if any(('show') or ('SHOW') or ('Show') in line):
                    line = line.replace('show', 'print').replace('SHOW', 'print').replace('Show', 'print')
                    line_to_add = line.replace(';', '')
                    outfile.write(line_to_add + '\n')

