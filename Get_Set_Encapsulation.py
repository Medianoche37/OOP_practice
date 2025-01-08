class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number ,self._balance = account_number,balance
        #защищенные атрибуты класса
    def get_account_number(self):#геттер-метод для атрибута,
        # используется для получения значения атрибута
        return self._account_number

    def get_balance(self):#геттер-метод для атрибута,
        # используется для получения значения атрибута
        return self._balance

    def set_balance(self,value):#сеттер-метод для атрибута,
        # используется для установки значения атрибута
        self._balance = value

