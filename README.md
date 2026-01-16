Customer Transaction Summary

This is a simple Python project that analyzes customer transactions to calculate the total amount spent by each customer. The program also identifies the customer with the highest overall transaction value.

I created this project to strengthen my understanding of core Python concepts such as loops, conditional logic, tuple handling, and basic data processing.

Project Overview

Processes a list of customer transactions

Calculates the total spending for each customer

Displays transaction details while processing

Identifies the customer with the highest total transaction amount

Concepts Practiced

Nested loops

Conditional statements

Tuples and iteration

Basic aggregation logic

Problem-solving using plain Python

Technologies Used

Python 3.x

Sample Input
transactions = [
    (1, 200),
    (2, 150),
    (1, 300),
    (3, 400),
    (2, 50),
    (3, 100)
]

Sample Output
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

Output Explanation

Processing transactions for Customer X indicates the start of processing for a specific customer.

Transaction lines show individual transaction entries.

Total amount for Customer X displays the sum of all transactions for that customer.

Running total of all transactions shows the cumulative totals after each customer is processed.

The final line identifies the customer with the highest total transaction amount
