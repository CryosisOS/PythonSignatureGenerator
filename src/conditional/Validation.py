# Author: CryosisOS
# Date Created: 2018-07-24

class Validation:
    
    @staticmethod
    def condition(user_choice):
        choice = user_choice
        if choice in ["1", "html", "HTML"]:
            return True
        elif choice in ["2", "rtf", "RTF"]:
            return True
        elif choice in ["3", "txt", "TXT"]:
            return True
        else:
            return False
