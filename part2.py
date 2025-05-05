from table import table
from tokenizer import lexer

# Parsing Table as a dictionary
productions = {
    1: {'E': ['program', ';', 'var', 'D', 'begin', 'S', 'end']},
    2: {'I': ['L', 'R']},
    3: {'I': ['L']},
    4: {'D': ['B', ':', 'T', ';']},
    5: {'B': ['I', ',', 'B']},
    6: {'B': ['I']},
    7: {'T': ['integer']},
    8: {'S': ['C']},
    9: {'S': ['C', 'S']},
    10: {'C': ['W']},
    11: {'C': ['A']},
    12: {'W': ['show', '(', 'G', 'I', ')', ';']},
    13: {'W': ['show', '(', 'I', ')', ';']},
    14: {'G': ['"value=",']},
    15: {'A': ['I', '=', 'E', ';']},
    16: {'E': ['E', '+', 'H']},
    17: {'E': ['E', '-', 'H']},
    18: {'E': ['H']},
    19: {'H': ['H', '*', 'F']},
    20: {'H': ['H', '/', 'F']},
    21: {'H': ['F']},
    22: {'F': ['I']},
    23: {'F': ['N']},
    24: {'F': ['(', 'E', ')']},
    25: {'N': ['K', 'M', 'X']},
    26: {'N': ['K', 'M']},
    27: {'N': ['M', 'X']},
    28: {'N': ['M']},
    29: {'X': ['M', 'X']},
    30: {'X': ['M']},
    31: {'K': ['+']},
    32: {'K': ['-']},
    33: {'M': ['0']},
    34: {'M': ['1']},
    35: {'M': ['2']},
    36: {'M': ['3']},
    37: {'M': ['4']},
    38: {'M': ['5']},
    39: {'M': ['6']},
    40: {'M': ['7']},
    41: {'M': ['8']},
    42: {'M': ['9']},
    43: {'L': ['a']},
    44: {'L': ['b']},
    45: {'L': ['r']},
    46: {'L': ['s']},
    47: {'R': ['L', 'R']},
    48: {'R': ['M', 'R']},
    49: {'R': ['L']},
    50: {'R': ['M']},
}


def parse(input_string):
    print(f"START PARSE")

    # Initialize the stack with the start symbol and the end marker
    stack = ['0']
    # input_string += '$'  # Append end marker to the input
    index = 0  # Pointer for the input string

    print(f"Initial Stack: {stack}")

    while stack:
        top = stack.pop()  # Get the top of the stack
        # print(f" \nPop: {top}")
        print(f" Pop: {top}")
        current_input = input_string[index]  # Current input symbol

        print(f"Stack: {stack}, Read: {current_input}")

        if isinstance(top, int) or top.isdigit():
            # Valid state to pop
            action = table[int(top)].get(current_input, None)

            print(f" Goto: [{top},{current_input}]={action}")

            if action is None or action == '':
                print(
                    f"Error: No action for state {top} and input '{current_input}'")
                return False

            if action == 'ACC':
                print("ACCEPPTED!!!!!!!!!!!!!!")
                return True  # Accepted
            elif action.startswith('S'):  # Shift action
                # Push top, then current_input, then action[1:]
                new_state = action[1:]

                stack.append(top)
                # Push the current input symbol onto the stack
                stack.append(current_input)
                # Push the new state onto the stack
                stack.append(new_state)
                # Move to the next input symbol
                index += 1

                print(f" Push: {top},{current_input},{new_state}")
                print(
                    f"Shift to state {new_state}, Stack after shift: {stack}")

            elif action.startswith('R'):
                # Logic to do reduction by production Ex: 'R8'
                rule_id = int(action[1:])  # Get the rule number
                production = productions[rule_id]
                lhs = list(production.keys())[0]
                rhs = production[lhs]
                # lhs, rhs = productions[rule_id]  # Get the production

                # Count the number of symbols in the RHS
                num_rhs_symbols = len(rhs)

                print(f"Push {top} back into stack")
                # Push the top, back into the stack before popping again
                stack.append(top)

                # Print the reduction rule
                print(f"Reducing by rule {rule_id}: {lhs} -> {rhs}")

                # Pop the symbols from the stack
                # Pop both the symbols and their associated states
                for _ in range(num_rhs_symbols * 2):
                    stack.pop()

                print(f"Popped: {num_rhs_symbols * 2} times")
                print(f"Stack after length pops: {stack}")

                reduction_pop = stack.pop()
                print(f" Reduction Pop: {reduction_pop}")

                # Get the new state from the parsing table
                new_state = table[int(reduction_pop)].get(
                    lhs, None)  # Look up the new state

                print(f" Goto: [{reduction_pop}, {lhs}]={new_state}")

                if new_state is None or new_state == '':
                    print(
                        f"Error: No reduction action for state {reduction_pop} and input '{lhs}'")
                    return False

                if new_state is not None:
                    stack.append(reduction_pop)
                    stack.append(lhs)
                    stack.append(new_state)  # Push the new state
                    print(f"Push:{reduction_pop},{lhs},{new_state}")
                print(f"Stack after reduction: {stack}")


# Test the parser with the given expressions
with open("final25.txt") as f:
    code = f.read()
tokens = lexer(code)
tokens.append('$')
parse(tokens)

"""
#expressions = # ["(i+i)*i$", "(i*)$"]  # "(i+i)/i$"
for expr in expressions:
    print(f"Testing expression: {expr}")
    parse(expr)
    print("\n")
"""
