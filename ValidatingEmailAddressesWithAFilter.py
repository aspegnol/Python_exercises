import re
def fun(s):
    return bool(re.match(r'([0-9]|[a-z]|-|_)+\@([0-9]|[a-z])*\.[a-z]{1,3}$',s))
    # return True if s is a valid email, else return False
