import random
def generate_random_letter():
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return random.choice(alphabet)
for _ in range(5):
  print(generate_random_letter())