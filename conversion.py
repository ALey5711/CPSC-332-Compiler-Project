FILE_PATH = 'final25.txt'


lines_to_ignore = [
    'project s2025',
    'var',
    'begin',
    'a1 , b2s , ar , bb : integer ;'
    'show',
    'end'
]

def lineConversion(FILE_PATH):
     with open(FILE_PATH, 'r') as file:
        lines = file.readlines()
        for lines in file:
            if any(phrase in lines_to_ignore for phrase in lines_to_ignore):
                continue
            else:
                with open('project2025.py','w', encoding = 'UTF-8') as outfile:
                        line_to_add = lines.strip(';')
                        outfile.write(line_to_add + '\n')