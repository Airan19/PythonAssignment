"""Create a program to validate the age of the voter with the help of custom exception. Voters whose age is less than 18 should not be allowed to vote.

"""

# Creating our custom class to raise exception when voter's age is less than 18
class VoterAgeException(Exception):
    pass
class Voter:
    def __init__(self):
        try:
            self.age = int(input("Enter your age:"))
        except ValueError as e:
            print(e)
        finally:
            print('You provided wrong input type, quitting the program')
            exit()
        
    def vote(self):
        if self.age < 18:
            raise VoterAgeException("Voters whose age is less than 18 are not allowed to vote.")
        else:
            print("You are eligible to vote.")


voter1 = Voter() # Creating a object out of Voter class
try:
    voter1.vote()
except VoterAgeException as e:
    print(e)  # this will print the custom error we have provided above using the raise keyword and VoterAgeException class.

voter2 = Voter() # Creating a object out of Voter class
try:
    voter2.vote()
except VoterAgeException as e:
    print(e)  # this will print the custom error we have provided above using the raise keyword and VoterAgeException class.

