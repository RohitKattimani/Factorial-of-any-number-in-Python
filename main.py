Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def factorial(a):
  if a == 0:
    return 1
  else:
    return a * factorial(a - 1)


a = int(input("Enter an Integer: "))
print(factorial(a))