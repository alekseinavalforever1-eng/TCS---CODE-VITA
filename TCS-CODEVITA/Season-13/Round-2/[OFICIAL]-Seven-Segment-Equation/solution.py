
import sys

# Define Symbols based on Fig 1, 2, 3
# Format: 3 rows of 3 chars concatenated
SYMBOLS = {
    "one":   "     |  |",
    "two":   " _  _||_ ",
    "three": " _  _| _|",
    "four":  "   |_|  |",
    "five":  " _ |_  _|",
    "six":   " _ |_ |_|",
    "seven": " _   |  |",
    "eight": " _ |_||_|",
    "nine":  " _ |_|  |",
    "zero":  " _ | ||_|",
    "add":   "    _| | ",
    "mul":   "   |_||_|",
    "sub":   "   |_|| |",
    "div":   " _  _| _|", # Same as three
    "open":  "|  |  |  ",
    "close": "  |  |  |",
}

# Map Pattern -> List of (Char, Type)
PATTERNS = {}

def register(name, char, type_):
    p = SYMBOLS[name]
    if p not in PATTERNS:
        PATTERNS[p] = []
    PATTERNS[p].append((char, type_))

register("one", '1', 'N')
register("two", '2', 'N')
register("three", '3', 'N')
register("four", '4', 'N')
register("five", '5', 'N')
register("six", '6', 'N')
register("seven", '7', 'N')
register("eight", '8', 'N')
register("nine", '9', 'N')
register("zero", '0', 'N')

register("add", '+', 'O')
register("mul", '*', 'O')
register("sub", '-', 'O')
register("div", '/', 'O')

register("open", '(', 'O')
register("close", ')', 'O')

# Build Universe of LEDs
ALL_LEDS = set()
for p in PATTERNS:
    for r in range(3):
        for c in range(3):
            idx = r*3 + c
            char = p[idx]
            if char != ' ':
                ALL_LEDS.add((r, c, char))

def get_active_leds(grid_str):
    leds = set()
    for r in range(3):
        for c in range(3):
            idx = r*3 + c
            char = grid_str[idx]
            if char != ' ':
                leds.add((r, c, char))
    return leds

def leds_to_grid(leds):
    grid = [' '] * 9
    for (r, c, char) in leds:
        idx = r*3 + c
        grid[idx] = char
    return "".join(grid)

def solve():
    try:
        input_data = sys.stdin.read().split('\n')
    except:
        return

    if not input_data:
        return

    try:
        N = int(input_data[0].strip())
    except:
        return

    lines = [l for l in input_data[1:] if len(l) > 0]
    if len(lines) < 3:
        return
    
    l1 = lines[0].ljust(3*N)
    l2 = lines[1].ljust(3*N)
    l3 = lines[2].ljust(3*N)
    
    current_grids = []
    for i in range(N):
        g = l1[i*3:i*3+3] + l2[i*3:i*3+3] + l3[i*3:i*3+3]
        current_grids.append(g)
    
    priority_line = ""
    for l in lines[3:]:
        if any(c in "+-*/" for c in l):
            priority_line = l.strip()
            break
    
    try:
        costs = list(map(int, lines[-1].strip().split()))
        X, Y, P, Q = costs
    except:
        X, Y, P, Q = 1, 1, 1, 1

    # Debug: Print parsed grids
    for idx, g in enumerate(current_grids):
        print(f"Char {idx}: '{g}'")
        if g in PATTERNS:
            # pass
            print(f"  Matches: {PATTERNS[g]}")
        else:
            print(f"  Unknown Pattern")
            # pass

    # Generate all valid base interpretations
    # Each grid maps to 1 or more (Char, Type)
    # We need to form all combinations
    
    possible_chars = []
    for g in current_grids:
        if g in PATTERNS:
            possible_chars.append(PATTERNS[g])
        else:
            # Invalid char in input?
            # Assume it's a valid char that we will toggle FROM.
            # But we don't know its Type (N/O).
            # We can treat it as '?' and Type '?'
            possible_chars.append([('?', '?')])

    import itertools
    base_interpretations = list(itertools.product(*possible_chars))
    
    # Filter base interpretations?
    # We only need one valid one to define the "Starting State".
    # But if there's ambiguity (3 vs /), the starting state is ambiguous.
    # The problem implies "The equation". Singular.
    # "The equation is said to be valid only if all the operands are positive".
    # This suggests we should find the interpretation that makes a valid equation.
    
    valid_base_eqs = []
    for interp in base_interpretations:
        eq_str = "".join(c for c, t in interp)
        # Check if valid syntax?
        # We can just store it.
        valid_base_eqs.append(interp)
        
    if not valid_base_eqs:
        # If no valid interpretation, we can't start?
        # Or maybe we assume the input is valid despite our parser?
        # No, if we can't parse, we can't toggle.
        pass
        
    # If multiple valid base eqs, which one is "The equation"?
    # Usually the one that parses correctly.
    # But we iterate toggles on the GRIDS.
    # The cost depends on the Type transition.
    # If the base type is ambiguous, the cost is ambiguous.
    # However, for a specific toggle at index `i`, we only care about the type of `i`.
    # If `i` is `3` or `/`, its type is N or O.
    # If we toggle `i`, we transition from N or O.
    
    max_ratio = -1.0

    # Precedence evaluator
    def evaluate(eq_str):
        # Tokenize
        tokens = []
        num = ""
        for c in eq_str:
            if c.isdigit():
                num += c
            else:
                if num:
                    tokens.append(int(num))
                    num = ""
                tokens.append(c)
        if num:
            tokens.append(int(num))
            
        # Handle Brackets
        while '(' in tokens:
            try:
                end = tokens.index(')')
                start = -1
                for i in range(end - 1, -1, -1):
                    if tokens[i] == '(':
                        start = i
                        break
                if start == -1: return -1
                sub_expr = tokens[start+1:end]
                val = eval_tokens(sub_expr)
                if val == -1: return -1
                tokens = tokens[:start] + [val] + tokens[end+1:]
            except ValueError:
                return -1

        return eval_tokens(tokens)

    def eval_tokens(tokens):
        def process_op(toks, ops_to_process):
            new_toks = []
            i = 0
            while i < len(toks):
                t = toks[i]
                if isinstance(t, str) and t in ops_to_process:
                    if not new_toks: return None
                    lhs = new_toks.pop()
                    if i + 1 >= len(toks): return None
                    rhs = toks[i+1]
                    if not isinstance(rhs, int): return None
                    res = 0
                    if t == '+': res = lhs + rhs
                    elif t == '-': res = lhs - rhs
                    elif t == '*': res = lhs * rhs
                    elif t == '/': 
                        if rhs == 0: return None
                        res = lhs // rhs
                    new_toks.append(res)
                    i += 2
                else:
                    new_toks.append(t)
                    i += 1
            return new_toks

        current_tokens = tokens
        for op_char in priority_line:
            current_tokens = process_op(current_tokens, [op_char])
            if current_tokens is None: return -1
            
        if len(current_tokens) == 1 and isinstance(current_tokens[0], int):
            return current_tokens[0]
        return -1

    # Iterate over each character position
    for i in range(N):
        original_grid = current_grids[i]
        active = get_active_leds(original_grid)
        
        # Try toggling each LED in the Universe
        for led in ALL_LEDS:
            # Toggle
            is_on = led in active
            new_active = active.copy()
            if is_on:
                new_active.remove(led)
                toggle_cost = X
            else:
                new_active.add(led)
                toggle_cost = Y
            
            new_grid = leds_to_grid(new_active)
            
            if new_grid in PATTERNS:
                # Valid target symbol(s)
                targets = PATTERNS[new_grid]
                
                # For each possible target interpretation
                for (new_char, new_type) in targets:
                    
                    # We need the Old Type to calculate Transition Cost.
                    # The Old Type depends on the interpretation of the Original Grid.
                    # We iterate over all valid base interpretations.
                    
                    for base_interp in valid_base_eqs:
                        # base_interp is a list of (char, type) for the whole equation
                        old_char, old_type = base_interp[i]
                        
                        # Calculate Cost
                        trans_cost = 0
                        if old_type == 'N' and new_type == 'O': trans_cost = P
                        elif old_type == 'O' and new_type == 'N': trans_cost = Q
                        
                        total_cost = toggle_cost + trans_cost
                        
                        # Construct new equation string
                        # Replace i-th char in base_interp
                        new_eq_list = [c for c, t in base_interp]
                        new_eq_list[i] = new_char
                        new_eq_str = "".join(new_eq_list)
                        
                        # Evaluate
                        try:
                            val = evaluate(new_eq_str)
                            if val >= 0:
                                ratio = val / total_cost
                                if ratio > max_ratio:
                                    max_ratio = ratio
                        except:
                            pass

    if max_ratio < 0:
        print("0.00")
    else:
        print(f"{max_ratio:.2f}")

if __name__ == '__main__':
    solve()
