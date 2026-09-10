def eval_gates(n, g_defs, t, i_defs, tgt_gate):
    
    g_outs = {g: [0] * t for g in g_defs}

    inputs = {}
    
    
    for d in i_defs:
        p = d.split()
        var = p[0]
        vals = list(map(int, p[1:]))
        inputs[var] = vals
    
    
    for g in g_defs:
        out_var, op = g.split('=')
        op = op.strip()
        
        # Extract input variables
        in1, in2 = op[op.index('(')+1:op.index(')')].split(',')
        in1, in2 = in1.strip(), in2.strip()
        
        
        for c in range(1, t):
            if op.startswith("AND"):
                g_outs[out_var][c] = (inputs[in1][c - 1] & inputs[in2][c - 1])
            elif op.startswith("OR"):
                g_outs[out_var][c] = (inputs[in1][c - 1] | inputs[in2][c - 1])
            elif op.startswith("NAND"):
                g_outs[out_var][c] = not (inputs[in1][c - 1] & inputs[in2][c - 1])
            elif op.startswith("NOR"):
                g_outs[out_var][c] = not (inputs[in1][c - 1] | inputs[in2][c - 1])
            elif op.startswith("XOR"):
                g_outs[out_var][c] = (inputs[in1][c - 1] ^ inputs[in2][c - 1])
            
            
            g_outs[out_var][c] = int(g_outs[out_var][c])
    
    return ' '.join(map(str, g_outs[tgt_gate]))

N = int(input())
gates = [input().strip() for _ in range(N)]
T = int(input())
inputs = [input().strip() for _ in range(T)]
target_gate = input().strip()


result = eval_gates(N, gates, T, inputs, target_gate)
print(result)
