# Austin Zebrowski

# E.Cloudmesh.Common.2
# Develop a program that demonstrates the use of dotdict

from cloudmesh.common.dotdict import dotdict

mydictionary = {
    "name": "Katelyn"
    , "type": "Student"
    , "height": 5.5
}

mydictionary = dotdict(mydictionary)

if mydictionary.height == 5.5:
    print(mydictionary.name, "is five foot five")
else:
    print("wrong height!")