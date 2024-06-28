# !bin/bash
# Daniel OUATTARA
# 27 06 2024

import json

"""
JSON: Javascript Object Notation
--------------------------------
{
    "title": "Gattaca",
    "release_year": 1997,
    "is_awesome": true,
    "won_oscar": false,
    "actors": ["Ethan Hawke", "Uma Thurman", "Alan Arkin", "Loren Dean"],
    "budget": null,
    "credits": {
        "director": "Andrew Niccol",
        "writer": "Andrew Niccol",
        "composer": "Michael Nyman",
        "cinematographer": "Sławomir Idziak"
    }
}



XML equivalent
--------------

<movie>
    <title>Gattaca</title>
    <release_year>1997</release_year>
    <is_awesome>true</is_awesome>
    <won_oscar>false</won_oscar>
    <actors>
        <actor>Ethan Hawke</actor>
        <actor>Uma Thurman</actor>
        <actor>Alan Arkin</actor>
        <actor>Loren Dean</actor>
    </actors>
    <budget>null</budget>
    <credits>
        <director>Andrew Niccol</director>
        <writer>Andrew Niccol</writer>
        <composer>Michael Nyman</composer>
        <cinematographer>Sławomir Idziak</cinematographer>
    </credits>
</movie>

"""


"""How to use the JSON module in Python
-----------------------------------------"""

for item in dir(json):
    print(item)

"""
JSONDecodeError
JSONDecoder
JSONEncoder
__all__
__author__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__
__version__
_default_decoder
_default_encoder
codecs
decoder
detect_encoding
dump(j, f) :: write JSON object to file, or file-like object 
dumps (j) :: Output JOSN object as string
encoder
load (f) :: Load JSON data from file, or file-like object
loads(s) :: Load JSON data from a string
scanner
"""
