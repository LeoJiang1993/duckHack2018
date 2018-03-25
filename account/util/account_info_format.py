import re


def check_email_format(email):
    email_checker = re.compile(r"^\w+@stevens\.edu$]", 0)
    return email_checker.fullmatch(email)


def check_password_format(password):
    return re.fullmatch(
        r"^(?=.*[0-9].*)(?=.*[A-Z].*)(?=.*[a-z].*).{8,20}|(?=.*[0-9].*)(?=.*[A-Z].*)(?=.*[@$_*#].*).{8,20}|(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[@$_*#].*).{8,20}|(?=.*[A-Z].*)(?=.*[a-z].*)(?=.*[@$_*#].*).{8,20}$",
        password, 0)
