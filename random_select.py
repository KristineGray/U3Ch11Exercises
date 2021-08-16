import random

def random_from_list(a_list):
  # Your code here to select a random element from the list passed to the function.
  random_index = random.randint(0, len(a_list))
  # Return the selected element
  return a_list[random_index]
