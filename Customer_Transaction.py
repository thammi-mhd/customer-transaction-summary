def calculation_pdct(transaction):
    amt_ttl = []
    for i in range(0, len(transaction)):
        sum = 0
        print(f"\nProcessing transactions for Customer {transaction[i][0]}:")
        for j in transaction:
            if transaction[i][0] == j[0]:
                print(f"  - Transaction: {j}")  # Showing each transaction for this customer
                sum += j[1]
        amt_ttl.append(sum)
        print(f"Total amount for Customer {transaction[i][0]}: {sum}")
        print(f"Running total of all transactions processed so far: {amt_ttl}")
  
    max_amt = max(amt_ttl)
    for i, item in enumerate(transaction):
        if amt_ttl[i] == max_amt:
            print(f"\nThe highest amount is with Customer {item[0]} and the amount is {max_amt}")
            break

transactions = [
    (1, 200),
    (2, 150),
    (1, 300),
    (3, 400),
    (2, 50),
    (3, 100),
]
calculation_pdct(transactions)
