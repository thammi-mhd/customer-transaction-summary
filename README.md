# customer-transaction-summary
A simple Python project that analyzes customer transactions to calculate total spending per customer and identifies the customer with the highest overall transaction total. Great for practicing data analysis using basic Python constructs like loops, conditionals, and tuples.



# Customer Transaction Summary in Python

This project processes a list of customer transactions to determine the total amount spent by each customer. It also identifies the customer with the highest total transaction amount.

## 🔧 Features
- Calculates total transaction amount per customer
- Identifies and displays the customer with the highest overall transactions
- Demonstrates nested loops, conditional logic, and tuple handling in Python

## 🧠 Technologies Used
- Python 3.x

## 🧾 Sample Input
```python
transactions = [
    (1, 200),
    (2, 150),
    (1, 300),
    (3, 400),
    (2, 50),
    (3, 100) ]
```


OUTPUT example
```python
(1, 200)
(1, 300)
500
[200, 300]
(2, 150)
(2, 50)
200
[200, 300, 150, 50]
(3, 400)
(3, 100)
500
[200, 300, 150, 50, 400, 100]
the highest amount is with the customer 1  and the amount is 300
```
