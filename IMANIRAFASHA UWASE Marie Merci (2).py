from collections import deque

class BankTransactionManager:
    def __init__(self):
        self.transaction_stack = []  # Stack for undoing transactions
        self.transaction_queue = deque()  # Queue for processing transaction requests
        self.transaction_history = []  # List for storing transaction history

    def process_transaction(self, transaction):
        # Enqueue transaction request for processing
        self.transaction_queue.append(transaction)

    def complete_transaction(self):
        if self.transaction_queue:
            transaction = self.transaction_queue.popleft()  # Dequeue and process the transaction
            # Store the completed transaction in history
            self.transaction_history.append(transaction)
            # Push the transaction onto the stack for potential undo
            self.transaction_stack.append(transaction)
            print(f"Transaction '{transaction}' completed.")

    def undo_last_transaction(self):
        if self.transaction_stack:
            transaction = self.transaction_stack.pop()  # Pop the last transaction
            print(f"Undoing transaction '{transaction}'.")
            # Potentially reverse the transaction here if needed
        else:
            print("No transactions to undo.")

    def view_transaction_history(self):
        return self.transaction_history

# Example usage
manager = BankTransactionManager()

manager.process_transaction("Deposit $100")
manager.process_transaction("Withdraw $50")
manager.complete_transaction()
manager.complete_transaction()

print(manager.view_transaction_history())  # ["Deposit $100", "Withdraw $50"]

manager.undo_last_transaction()  # "Undoing transaction 'Withdraw $50'"
print(manager.view_transaction_history())  # ["Deposit $100", "Withdraw $50"]
