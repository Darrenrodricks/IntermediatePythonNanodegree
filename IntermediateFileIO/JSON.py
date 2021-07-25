import json

[
    {
        "class": "Iris-setosa",
        "petallength": 1.4,
        "petalwidth": 0.2,
        "sepallength": 5.1,
        "sepalwidth": 3.5
    },
    {
        "class": "Iris-versicolor",
        "petallength": 4.7,
        "petalwidth": 1.4,
        "sepallength": 7,
        "sepalwidth": 3.2
    },
    {
        "class": "Iris-virginica",
        "petallength": 6,
        "petalwidth": 2.5,
        "sepallength": 6.3,
        "sepalwidth": 3.3
    }
]

# The general pattern for reading and writing plain text from files is:
#
# 1. Extract data from a JSON file into Python
#   - Open a file-like object f
#   - Call json.load(f) or a similar method
# 2. Do something with the data, now within Python
# 3. Write data from Python to a file.
#   -  Open a file-like object f
#   -  Call json.dump(obj, f) or a similar method


[
    {
        "name": "Udacity",
        "role": 100,
        "description": "A stellar Python instructor is needed for a new course!",
        "available": True
    },
    {
        "name": "Udacity",
        "role": 404,
        "description": "A quality assistance engineer who can start immediately.",
        "available": False
    }
]


# Extract data into Python
with open('listings.json', 'r') as infile:
    contents = json.load(infile)  # Parse JSON data into a Python object. (A)

# Filter out all unavailable job listings.
available = [job for job in contents if job["available"]]

# Write available listings to an output file.
with open('available-listings.json', 'w') as outfile:
    json.dump(available, outfile, indent=2)