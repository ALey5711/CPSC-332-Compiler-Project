
"""
parse_table = [
    # i    +    -   *   /   (     )   $    E   T   F
    ['S5', '', '', '', '', 'S4', '', '', '1', '2', '3'],  # 0
    ['', 'S6', 'S7', '', '', '', '', 'ACC', '', '', ''],  # 1
    ['', 'R3', 'R3', 'S8', 'S9', '', 'R3', 'R3', '', '', ''],  # 2
    ['', 'R6', 'R6', 'R6', 'R6', '', 'R6', 'R6', '', '', ''],  # 3
    ['S5', '', '', '', '', 'S4', '', '', '10', '2', '3'],  # 4
    ['', 'R8', 'R8', 'R8', 'R8', '', 'R8', 'R8', '', '', ''],  # 5
    ['S5', '', '', '', '', 'S4', '', '', '', '11', '3'],  # 6
    ['S5', '', '', '', '', 'S4', '', '', '', '12', '3'],  # 7
    ['S5', '', '', '', '', 'S4', '', '', '', '', '13'],  # 8
    ['S5', '', '', '', '', 'S4', '', '', '', '', '14'],  # 9
    ['', 'S6', 'S7', '', '', '', 'S15', '', '', '', ''],  # 10
    ['', 'R1', 'R1', 'S8', 'S9', '', 'R1', 'R1', '', '', ''],  # 11
    ['', 'R2', 'R2', 'S8', 'S9', '', 'R2', 'R2', '', '', ''],  # 12
    ['', 'R4', 'R4', 'R4', 'R4', '', 'R4', 'R4', '', '', ''],  # 13
    ['', 'R5', 'R5', 'R5', 'R5', '', 'R5', 'R5', '', '', ''],  # 14
    ['', 'R7', 'R7', 'R7', 'R7', '', 'R7', 'R7', '', '', ''],  # 15
]
"""

# Parsing Table as a dictionary
parse_table = {
    0: {'program': 'S2', 'var': '', 'begin': '', 'end': '', 'integer': '', 'show': '', '"value="': '', ';': '', ':': ',', '+': '',
        '-': '', '*': '', '/': '', '0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': '', 'a': '',
        'b': '', 'r': '', 's': '', 'P': '', 'I': '', 'R': '', 'D': '', 'B': '', 'T': '', 'S': '', 'C': '', 'W': '', 'G': '', 'A': '',
        'E': '', 'H': '', 'F': '', 'N': '', 'X': '', 'K': '', 'M': '', 'L': ''},
}

productions = {
    1: ['E', 'E+T'],
    2: ['E', 'E-T'],
    3: ['E', 'T'],
    4: ['T', 'T*F'],
    5: ['T', 'T/F'],
    6: ['T', 'F'],
    7: ['F', '(E)'],
    8: ['F', 'i']
}

first_sets = {
    'E': {'(', 'i'},
    'T': {'(', 'i'},
    'F': {'(', 'i'}
}

follow_sets = {
    'E':  {'$', '+', '-', ')'},
    'T':  {'$', '+', '-', ')', '*', '/'},
    'F':  {'$', '+', '-', ')', '*', '/'}
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

        if top.isdigit():
            # Valid state to pop
            action = parse_table[int(top)].get(current_input, None)

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
                lhs, rhs = productions[rule_id]  # Get the production
                # Count the number of symbols in the RHS
                num_rhs_symbols = len(rhs)

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
                new_state = parse_table[int(reduction_pop)].get(
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
expressions = ["(i+i)*i$", "(i*)$"]  # "(i+i)/i$"
for expr in expressions:
    print(f"Testing expression: {expr}")
    parse(expr)
    print("\n")
