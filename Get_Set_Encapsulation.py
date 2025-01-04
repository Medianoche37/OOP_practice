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


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name

    def __get_salary(self):
        return self.__salary

    def __set_salary(self, value):
        if isinstance(value, int | float) and value > 0:
            self.__salary = value
        else:
            print(f"ErrorValue:{value}.")

    title = property(fget=__get_name) # свойство , можем обращаться к __get_name как к атрибуту
    reward = property(fget=__get_salary, fset=__set_salary) # свойство
# Функция property позволяет превращать атрибуты класса в свойства или управляемые атрибуты
# property(fget=None, fset=None, fdel=None, doc=None)


class UserMail:
    def __init__(self, login, email):
        self.login, self.__email = login, email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str) and len(a := value.split("@")) == 2 and "." in a[1]:
            self.__email = value
        else:
            raise ValueError(f"ErrorMail:{value}")

    email = property(fget=get_email, fset=set_email)


print('hello')




