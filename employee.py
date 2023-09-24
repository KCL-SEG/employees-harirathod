"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class ContractType:
    def __init__(self):
        pass

    def get_pay(self) -> int:
        pass

    def __str__(self) -> str:
        pass


class CommissionType:
    def __init__(self):
        pass

    def get_pay(self) -> int:
        pass

    def __str__(self) -> str:
        pass

class Employee:
    def __init__(self, name: str, contract_type: ContractType, commission_type: CommissionType):
        self.name = name
        self.contract_type = contract_type
        self.commission_type = commission_type
 
    def get_pay(self) -> int:
        return self.contract_type.get_pay() + self.commission_type.get_pay()


    def __str__(self) -> str:
        return self.name + str(self.contract_type) + str(self.commission_type) + f'. Their total pay is {self.get_pay()}.'

# Types of Contracts (Monthly or Hourly).
class MonthlyContractor(ContractType):
    def __init__(self, salary: int):
        self.salary = salary

    def get_pay(self) -> int:
        return self.salary
    
    def __str__(self) -> str:
        return f' works on a monthly salary of {self.salary}'

class HourlyContractor(ContractType):
    def __init__(self, hours: int, rate: int):
        self.hours = hours
        self.rate = rate

    def get_pay(self) -> int:
        return  self.hours * self.rate
    
    def __str__(self) -> str:
        return f' works on a contract of {self.hours} hours at {self.rate}/hour'


# Types of Commissions (None, Bonus, or Contract).
class NoCommission(CommissionType):
    def __init__(self):
        super().__init__()

    def get_pay(self) -> int:
        return 0
    
    def __str__(self) -> str:
        return ""

class BonusCommission(CommissionType):
    def __init__(self, bonus: int):
        self.bonus = bonus

    def get_pay(self) -> int:
        return self.bonus
    
    def __str__(self) -> str:
        return f' and receives a bonus commission of {self.bonus}'

class ContractCommission(CommissionType):
    def __init__(self, contract_count: int, contract_rate: int):
        self.contract_count = contract_count
        self.contract_rate = contract_rate

    def get_pay(self) -> int:
        return self.contract_count * self.contract_rate
    
    def __str__(self) -> str:
        return f' and receives a commission for {self.contract_count} contract(s) at {self.contract_rate}/contract'







# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContractor(4000), NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContractor(100, 25), NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContractor(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContractor(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContractor(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContractor(120, 30), BonusCommission(600))
