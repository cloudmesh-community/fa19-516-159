# Austin Zebrowski

# E.Cloudmesh.Common.3
# Develop a program that demonstrates the use of FlatDict

from cloudmesh.common.FlatDict import FlatDict

mydictionary = {
    "name": "Katelyn"
    , "type": "Student"
    , "biometrics": {
        "height": 5.5,
        "weight": 120,
        "eye": "brown"
    }
}

mydictionary = FlatDict(mydictionary)
print(mydictionary.name, "weighs", mydictionary.biometrics__weight, "pounds")