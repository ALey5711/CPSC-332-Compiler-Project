from clean import clean
from conversion import lineConversion
from runner import import_from_path


if __name__ == "__main__":
    clean('final.txt', 'final25.txt')
    # Optional second pass example:
    clean(input_path='final25.txt', output_path='check.txt')

    lineConversion('final25.txt')

    import_from_path('project2025.py', 'project2025.py')
