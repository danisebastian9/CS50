# Create an empty set
s = set()

# Add elements to the Set

s.add(2)
s.add(4)
s.add(6)
s.add(9)
s.add(23)

print(s)

# sets values are unique by adding a repeated value, it's going to bypass it
s.add(4)
# remove values
s.remove(9)

print(s)

print(f"The set has {len(s)} elements.")
