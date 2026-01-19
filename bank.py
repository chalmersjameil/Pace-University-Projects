class BankAccount:
    def __init__(self, name: str, balance: float):
        """
        Initialize a BankAccount instance.
        :param name: Name of the account holder.
        :param balance: Initial balance of the account.
        """
        self.name = name
        self.balance = balance
        self.frozen = False

    def get_name(self):
        """Return the account holder's name."""
        return self.name

    def get_balance(self):
        """Return the account balance."""
        return self.balance

    def is_frozen(self):
        """Return whether the account is frozen."""
        return self.frozen

    def deposit(self, amount: float):
        """
        Deposit money into the account.
        :param amount: Amount to deposit.
        :return: True if the deposit is successful.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        if self.frozen:
            print("Account is frozen. Cannot deposit funds.")
            return False
        self.balance += amount
        return True

    def withdraw(self, amount: float):
        """
        Withdraw money from the account with enhanced checks.
        :param amount: Amount to withdraw.
        :return: True if the withdrawal is successful.
        """
        if self.frozen:
            print("Account is frozen. Cannot withdraw funds.")
            return False
        if amount > 1000:
            print("Shady transaction! Withdrawal over $1000 is not allowed. Freezing account.")
            self.freeze()
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        self.balance -= amount
        return True

    def freeze(self):
        """Freeze the account."""
        self.frozen = True

    def unfreeze(self):
        """Unfreeze the account."""
        self.frozen = False

    def __str__(self):
        """
        Return a string representation of the account.
        :return: A formatted string with account details.
        """
        status = "Frozen" if self.frozen else "Active"
        return f"BankAccount(name={self.name}, balance=${self.balance:.2f}, status={status})"
