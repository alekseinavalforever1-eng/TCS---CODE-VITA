def solve():
    initial_balance = int(input().strip())
    n = int(input().strip())
    
    balance = initial_balance
    transactions = []     
    commits = []           
    
    for _ in range(n):
        op = input().strip().split()
        
        if op[0] == "read":
            print(balance)
        
        elif op[0] == "credit":
            amount = int(op[1])
            balance += amount
            transactions.append(("credit", amount))
        
        elif op[0] == "debit":
            amount = int(op[1])
            balance -= amount
            transactions.append(("debit", amount))
        
        elif op[0] == "abort":
            t_index = int(op[1]) - 1  # 1-based index
            if 0 <= t_index < len(transactions):
                typ, amount = transactions[t_index]
                
                # reverse effect of transaction
                if typ == "credit":
                    balance -= amount
                else:
                    balance += amount
                transactions.pop(t_index)
        
        elif op[0] == "commit":
            commits.append(balance)
            transactions.clear()
        
        elif op[0] == "rollback":
            c_index = int(op[1]) - 1
            if 0 <= c_index < len(commits):
                balance = commits[c_index]
                transactions.clear()   
    
# ---------------- MAIN ----------------
if __name__ == "__main__":
    solve()
