# Write a statement that creates a list with the following
# strings: 'Einstein','Newton','Copernicus', and 'Kepler'.

notables = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
print(notables)

print([n for n in notables if len(notables) < 5])