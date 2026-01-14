# Create a list called surprise with the elements Groucho, Chico, and Harpo.
surprise = ['Groucho', 'Chico', 'Harpo']

# Lowercase the last element of the surprise list, reverse it, and then capitalize it.
last_el = surprise[2].lower()
print(last_el)

el_reverse = last_el[::-1]
print(el_reverse)

el_capitalize = el_reverse
print(el_capitalize.capitalize())
