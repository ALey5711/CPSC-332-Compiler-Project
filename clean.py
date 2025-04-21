import re
from typing import List

FILE_PATH = 'final.txt'
OUTPUT_FILE_PATH = 'final25.txt'


def add_spaces_around_operators(line: str) -> str:
    """
    Adds spaces around operators and punctuation outside of quoted strings.
    Preserves spacing and characters inside quoted segments.
    """
    segments = re.split(r'(".*?")', line)  # Split by quoted parts
    spaced_segments: List[str] = []

    for i, seg in enumerate(segments):
        if i % 2 == 1:
            spaced_segments.append(seg)  # Preserve quoted strings
        else:
            seg = re.sub(r'\s*=\s*', ' = ', seg)
            seg = re.sub(r'\s*\+\s*', ' + ', seg)
            seg = re.sub(r'\s*-\s*', ' - ', seg)
            seg = re.sub(r'\s*\*\s*', ' * ', seg)
            seg = re.sub(r'\s*/\s*', ' / ', seg)
            seg = re.sub(r'\s*;\s*', ' ; ', seg)
            seg = re.sub(r'\s*,\s*', ' , ', seg)
            seg = re.sub(r'\s*:\s*', ' : ', seg)
            seg = re.sub(r'\s*\(\s*', ' ( ', seg)
            seg = re.sub(r'\s*\)\s*', ' ) ', seg)
            spaced_segments.append(seg)

    return re.sub(r'\s+', ' ', ''.join(spaced_segments)).strip()


def clean(input_path: str = FILE_PATH, output_path: str = OUTPUT_FILE_PATH) -> None:
    """
    Cleans the source file by:
    - Removing full-line and inline comments
    - Skipping blank lines
    - Adding space around tokens (outside of quoted text)
    - Writing cleaned lines to the output file
    """
    cleaned_lines: List[str] = []
    inside_multiline_comment = False

    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            original_line = line.rstrip()
            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Remove inline comments (// some text //)
            line = re.sub(r'//.*?//', '', line)

            # Handle full-line comments
            if line.startswith('//') and line.endswith('//'):
                continue
            elif line.startswith('//'):
                inside_multiline_comment = True
                continue
            elif inside_multiline_comment:
                if line.endswith('//'):
                    inside_multiline_comment = False
                continue

            # Apply spacing rule
            line = add_spaces_around_operators(line)

            # Remove extra internal spaces
            line = re.sub(r'\s+', ' ', line).strip()

            if line:
                cleaned_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(cleaned_lines))


if __name__ == "__main__":
    clean()
    # Optional second pass example:
    clean(input_path='final25.txt', output_path='check.txt')
