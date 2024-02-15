#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
          self.items.append(title)

        self.last_transaction.append({"title": title, "price": price, "quantity": quantity})

        return self.items

    def apply_discount(self):
        if self.discount:
          self.total = int(self.total) * ((100 - self.discount) / 100)
          print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
       self.total -= (
          self.last_transaction[-1]["price"] * self.last_transaction[-1]["quantity"]
       )

       return self.total