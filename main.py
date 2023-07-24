import pandas as pd
import re
import string, sys

# testing purpose
BAD_WORDS = [",", "gamil", "gmil", ",", "gail", "gmal"]

SET_1 = ["gem", "gamil", "gmil", "gail", "gmal", "gmel", "outlok", "outlk", "gml", "yhoo", "bng", "gel"]

SET_2 = [",", "!", ":", "[]", "<", ">", "|"]


GOOD_MAIL = [
    "gmail", ".com", "outlook.com", "outlook", "yahoo", "affimedia", 
]

class EmailValidator:

    def length_checker(self, email):
        try:
            if len(email) >= 7:
                return True
            else:
                return False
        except Exception as e:
            return e


    def is_valid(self, email):
        try:
            for b in BAD_WORDS:
                if b in email:
                    return False
            return True
        except Exception as e:
            return e
    

    def match_pattern(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        else:
            return None


    def check_domain(self, email):
        df = pd.read_csv("domain.csv")
        domains = df["good_email"].tolist()
        for d in domains:
            if d in email and self.match_pattern(email) is True:
                return True
        return False


    def word_checker_and_replace(self, email):
        
        #if self.is_valid(email) is not True:
        bad_words = []
        for bw in BAD_WORDS:            # pattern = re.compile(r'\b' + re.escape(bw) + r'\b', re.IGNORECASE)
            if bw in email:
                bad_words.append(bw)
        #print( bad_words )
        for s2 in SET_2:
            if s2 in email:
                email = email.replace(s2, ".")

        for s in SET_1:
            if s in email:
                email = email.replace(s, "gmail")
        
        if self.check_domain(email) is True:
            print("Email Valid")
            return email
        else:
            return "Pattern not matched"
        
        
    # def is_valid(self, email):
    #     return self.length_checker(email) and self.word_checker(email)

# test code
validator = EmailValidator()
email = sys.argv[1]
print(validator.word_checker_and_replace(email))
