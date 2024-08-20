class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __repr__(self):
        title = self.name.center(30, "*") + "\n"
        ledger = ""
        for line in self.ledger:
            desc = "{:<23}".format(line["description"])
            amount = "{:>7.2f}".format(line["amount"])

            ledger += "{}{}\n".format(desc[:23], amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return title + ledger + total

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
        self.balance += amount

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount), "description": desc})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False


def create_spend_chart(categories):
    # Header Section
    header = "Percentage spent by category\n"

    # Chart Section
    chart = ""
    spent_amounts = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(
        map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts)
    )

    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + "|"
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    # Footer Section
    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.name, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(
        map(lambda description: description.ljust(max_length), descriptions)
    )
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")
