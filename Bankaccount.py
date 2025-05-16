class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ {amount} сом салынды. Жаңы баланс: {self.balance} сом.")
        else:
            print("❗ Туура эмес сумма.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❗ Туура эмес сумма.")
        elif amount > self.balance:
            print("❗ Баланста жетиштүү каражат жок.")
        else:
            self.balance -= amount
            print(f"✅ {amount} сом алынды. Калган баланс: {self.balance} сом.")

    def show_balance(self):
        print(f"💰 {self.owner} аккаунтунун балансы: {self.balance} сом")


def main():
    name = input("Атыңызды киргизиңиз: ")
    account = BankAccount(name)

    while True:
        print("\n=== 🏦 Банк Менюсу ===")
        print("1. Баланс текшерүү")
        print("2. Акча салуу")
        print("3. Акча алуу")
        print("4. Чыгуу")

        choice = input("Тандооңуз (1-4): ")

        if choice == "1":
            account.show_balance()
        elif choice == "2":
            try:
                amount = float(input("Салуу суммасы: "))
                account.deposit(amount)
            except ValueError:
                print("❗ Туура эмес сумма.")
        elif choice == "3":
            try:
                amount = float(input("Алуу суммасы: "))
                account.withdraw(amount)
            except ValueError:
                print("❗ Туура эмес сумма.")
        elif choice == "4":
            print("🚪 Программа жабылды.")
            break
        else:
            print("❗ Туура эмес тандоо.")

if __name__ == "__main__":
    main()
