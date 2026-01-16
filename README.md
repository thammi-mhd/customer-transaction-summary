# customer-transaction-summary

A simple Python project that analyzes customer transactions to calculate total spending per customer and identifies the customer with the highest overall transaction total. This project is useful for practicing data analysis using basic Python constructs such as loops, conditionals, and tuples.

---

# Customer Transaction Summary in Python

This project processes a list of customer transactions to determine the total amount spent by each customer. It also identifies the customer with the highest total transaction amount.

---

## Features

* Calculates total transaction amount per customer
* Identifies and displays the customer with the highest overall transactions
* Demonstrates nested loops, conditional logic, and tuple handling in Python

---

## Technologies Used

* Python 3.x

---

## Sample Input

```python
transactions = [
    (1, 200),
    (2, 150),
    (1, 300),
    (3, 400),
    (2, 50),
    (3, 100)
]
```

---

## Sample Output

```text
Processing transactions for Customer 1:
  - Transaction: (1, 200)
  - Transaction: (1, 300)
Total amount for Customer 1: 500
Running total of all transactions processed so far: [500]

Processing transactions for Customer 2:
  - Transaction: (2, 150)
  - Transaction: (2, 50)
Total amount for Customer 2: 200
Running total of all transactions processed so far: [500, 200]

Processing transactions for Customer 3:
  - Transaction: (3, 400)
  - Transaction: (3, 100)
Total amount for Customer 3: 500
Running total of all transactions processed so far: [500, 200, 500]

The highest amount is with Customer 1 and the amount is 500
```

---

## Output Explanation

* **Processing transactions for Customer X** shows the start of processing for each customer
* **Transaction** lines list individual transaction records
* **Total amount for Customer X** shows the total spending of that customer
* **Running total of all transactions** shows cumulative totals after each customer is processed
* The final line identifies the customer with the highest total transaction amount
