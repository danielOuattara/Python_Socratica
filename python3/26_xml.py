# !bin/bash
# Daniel OUATTARA
# 27 06 2024


"""
https://docs.python.org/3/library/xml.html#module-xml

https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

"""


import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

for item in dir(ET):
    print(item)

"""
C14NWriterTarget
Comment
Element
ElementPath
ElementTree
HTML_EMPTY
PI
ParseError
ProcessingInstruction
QName
SubElement
TreeBuilder
VERSION
XML
XMLID
XMLParser
XMLPullParser
_Element_Py
_ListDataStream
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_escape_attrib
_escape_attrib_c14n
_escape_attrib_html
_escape_cdata
_escape_cdata_c14n
_get_writer
_looks_like_prefix_name
_namespace_map
_namespaces
_raise_serialization_error
_serialize
_serialize_html
_serialize_text
_serialize_xml
_set_factories
canonicalize
collections
contextlib
dump
fromstring
fromstringlist
indent
io
iselement
iterparse
parse
re
register_namespace
sys
tostring
tostringlist
warnings
"""


"""
use `inspect module` to inspect the content of a module`
"""


print('-------------------------------------------------')

# Display classes in the ET module

for (name, member) in getmembers(ET, isclass):
    if not name.startswith('_'):
        print(name)

"""
C14NWriterTarget
Element  <--
ElementTree <--
ParseError
QName
TreeBuilder
XMLParser
XMLPullParser

More on 'Element' and 'ElementTree' classes

XML = Tree of Elements

ElementTree: 
xml is tree of data, grouped as nodes: parent and children nodes
each node can have  0, 1 or more children

Element:

# pur  element
<user></user> 

# element with one attribute
<user id='24'></user> 

# element with one attribute & text content
<user id='24'>John Doe</user> 

# element with one attribute, text content et other XML element
<user id='24'>
    John Doe
    <country>
        China
    </country>
</user> 

etc...
"""


print('-------------------------------------------------')

# Display functions in ET module

for (name, member) in getmembers(ET, isfunction):
    if not name.startswith('_'):
        print(name)

"""
Comment
PI
ProcessingInstruction
XML
XMLID
canonicalize
dump
fromstring :: (String) => Element
fromstringlist
indent
iselement
iterparse
parse :: (File) => ElementTree
register_namespace
tostring :: (Element) => String
tostringlist
"""
