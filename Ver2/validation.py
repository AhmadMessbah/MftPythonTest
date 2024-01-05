import re


def name_validator(name):
    if re.match("^[a-z]{2,20}$", name):
        return name
    else:
        raise ValueError("Invalid")