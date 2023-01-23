"""Create a program to check eligibility of the person for loan  with the help of oops concepts and exception handling. Person whose salary is less than 10K/ Month will not be eligible for the loan."""

# custom class to raise exception when salary of the person is less than 10k/month.
class LoanEligibilityException(Exception):
    pass

class Person:
    def __init__(self):
        self.salary = int(input("Enter your salary:"))

    def check_loan_eligibility(self):
        if self.salary < 10000:
            raise LoanEligibilityException("Person whose salary is less than 10K/month will not be eligible for the loan.")
        else:
            print("You are eligible for the loan.")

try:
    person1 = Person()                   # creating person1 object from Person class
    person1.check_loan_eligibility()     # check_loan_elibility method is called to check the person's eligibility for loan.
except LoanEligibilityException as e:    # if the provided conditions are not fulfilled then an exception will be raised.
    print(e)

