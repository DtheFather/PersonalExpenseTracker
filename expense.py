from dataclasses import dataclass

@dataclass
class Expense:
    expense_id: int
    title: str
    amount: float
    category: str
    date: str

    def to_list(self):
        return [self.expense_id, self.title, self.amount, self.category, self.date]

    @staticmethod
    def from_list(data):
        return Expense(int(data[0]), data[1], float(data[2]), data[3], data[4])
