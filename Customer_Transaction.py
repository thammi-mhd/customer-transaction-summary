def calculation_pdct(transaction):
  length = int(len(transaction)/2)
  amt_ttl = []
  for i in range(0,length):
    sum = 0
    for j in transaction:
      if transaction[i][0] == j[0]:
        sum += j[1]
        print(j)
        amt_ttl.append(j[1])
    print(sum)
    print(amt_ttl)
  max_amt = max(amt_ttl)
  for item in transaction:
    if item[1] == max_amt:
      print("the highest amount is with the customer ",item[0]," and the amount is",item[1])    
    



transactions = [
    (1, 200),
    (2, 150),
    (1, 300),
    (3, 400),
    (2, 50),
    (3, 100),
]
calculation_pdct(transactions)
