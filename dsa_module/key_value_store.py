class Storage:

    def __init__(self):
        self.data = {}  # hashmap
        self.transactions = []  # stack of operations in transaction

    def set(self, key, value):
        if self.transactions:
            self.transactions[-1]["writes"][key] = value
        else:
            self.data[key] = value

    def get(self, key):
        if self.transactions:
            for transaction in self.transactions[-1::-1]:
                if key in transaction["writes"]:
                    return transaction["writes"][key]
        if key not in self.data:
            raise KeyError("key not found")
        return self.data[key]

    def delete(self, key):
        if self.transactions:
            for transaction in self.transactions[-1::-1]:
                if key in transaction["writes"]:
                    del transaction["writes"][key]
                    return
        if key not in self.data:
            raise KeyError("key not found")
        del self.data[key]

    def begin(self):
        self.transactions.append({"reads": {}, "writes": {}})

    def commit(self):
        if not self.transactions:
            raise ValueError("No txn to commit")
        transaction = self.transactions.pop()
        for key, value in transaction["writes"].items():
            if not value:
                del self.data[key]
            else:
                self.data[key] = value

    def rollback(self):
        if not self.transactions:
            raise ValueError("No txn to rollback")
        del self.transactions[-1]

    def __str__(self):
        return f"Data = {self.data} | Txns = {self.transactions}"


s = Storage()
s.begin()
s.set("hello", "apurv")
s.set("where", "is")
s.set("hello1", "apurv")
s.set("where1", "is")
print(s.get("hello"))
s.commit()
print(s.get("hello"))
print(s)