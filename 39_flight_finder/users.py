
class User:

    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.email = ""

    def create_user(self):
        self.name = input("What is your first name?")
        self.lastname = input("What is your last name?")
        first_email = input("What is your email?")
        second_email = input("Please re-enter your email")
        if first_email == second_email:
            self.email = first_email
            return True

        return False

