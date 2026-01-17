def check_multiple(number):
  if number % 3 == 0 and number % 5 == 0:
    return True
  else:
    return False

def check_password(input_string):
    secret_word = "Python123"
    if input_string == "Python123":
        return "access granted"
    else:
        return "access denied"
  
def calculate_federal_tax(salary):
  if salary <= 11000:
    tax_rate = 0.10
    return salary * tax_rate
  elif salary > 11000 and salary <= 44725:
    tax_rate = 0.12
    return salary * tax_rate
  elif salary > 44725 and salary <= 95375:
    tax_rate = 0.22
    return salary * tax_rate
  else:
    tax_rate = 0.24
    return salary * tax_rate