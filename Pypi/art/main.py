from art import *
art_1=art("coffee") # return art as str in normal mode
print(art_1)
c[_]
art_2=art("woman",number=2) # return multiple art as str
print(art_2)

▓⚗_⚗▓ ▓⚗_⚗▓ 
art("coffee", number=3, space=5) 
'c[_]     c[_]     c[_]'
art("random") # random 1-line art mode
'(っ◕‿◕)っ '
art("rand")   # random 1-line art mode
't(-_-t) '
art(22,number=1) # raise artError
Traceback (most recent call last):
        ...
art.art.artError: The 'artname' type must be str.