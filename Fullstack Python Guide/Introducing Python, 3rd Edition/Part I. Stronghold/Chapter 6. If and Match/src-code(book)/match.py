# The match statement is a recent (version 3.10) addition to Python. 
# It’s similar to the switch statement in other languages like C and Java.
# You give it a subject, then one or more patterns to match against that subject’s value and/or type:

# match subject:
#     case pattern1:
#     case pattern2:
#     other patterns    
#     case _:
#         # if nothing else matches

# The simplest use of match is like the switch statement in languages like C 
# except you don’t use something like break to avoid “falling through” to the next case. 
# If a case does match, its code is executed, and the match statement finishes:
superhero = "Spiderman"
match superhero:
    case "Superman":
        secret_identity = "Clark Kent"
    case "Batman":
        secret_identity = "Bruce Wayne"
    case "Spiderman":
        secret_identity = "Peter Parker"
    case _:
        secret_identity = "?"

print(secret_identity)
