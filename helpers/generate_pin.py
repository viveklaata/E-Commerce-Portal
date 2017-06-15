import random

def generate_pin():
  numbers = '0123456789'
  return str(random.choice(numbers)+random.choice(numbers)+random.choice(numbers)+random.choice(numbers))