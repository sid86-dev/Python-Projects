from fuzzywuzzy import fuzz, process


choices = ["Sid lives in new york","Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys", "sids Cowboy"]

p = process.extract("lives new", choices,limit=1, scorer=fuzz.ratio)
print(p)
p = process.extractOne("cowboys", choices, scorer=fuzz.ratio)
print(p)

r = fuzz.ratio('My name is Sid', 'Sid')
p = fuzz.partial_ratio('My name is Sid', 'name is sid')

print(r)
print(p)