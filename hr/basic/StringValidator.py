if __name__ == '__main__':
    s = input()

    isAnyAlphaNumeric=False
    isAnyAlphabetical=False
    isAnyDigit=False
    isAnyLowercase=False
    isAnyUppercase=False
    for c in s:
        if(c.isalnum()):isAnyAlphaNumeric=True
        if(c.isalpha()):isAnyAlphabetical=True
        if(c.isdigit()):isAnyDigit=True
        if(c.islower()):isAnyLowercase=True
        if(c.isupper()):isAnyUppercase=True
    print(isAnyAlphaNumeric)
    print(isAnyAlphabetical)
    print(isAnyDigit)
    print(isAnyLowercase)
    print(isAnyUppercase)



# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
