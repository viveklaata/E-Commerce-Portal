from Portal.models import Listing
import random

def generate_listing_code():
  def generate_key():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    firstPart = random.choice(alpha) + random.choice(alpha) + random.choice(alpha)
    secondPart = random.choice(numbers) + random.choice(numbers) + random.choice(numbers)
    code = firstPart + secondPart
    return code

  code = generate_key()

  if len(Listing.objects.filter(code=code)) > 0:
    return generate_listing_code()

  return code