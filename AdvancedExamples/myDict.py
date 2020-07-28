# Create a mapping of states and abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print these cities
print("-"*10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print states
print("-"*10)
print("Michigan's abbreviation is: ", states['Michigan'])

print("-"*10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

print("-"*10)
for state, abbrev in states.items():
    print("%s state is abbreviated as %s and has city %s" % (state, abbrev, cities[abbrev]))