# !bin/bash
# Daniel OUATTARA
# 27 06 2024


"""
https://docs.python.org/3/library/xml.html#module-xml

https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

"""

import xml.etree.ElementTree as ET

print('------------------------------------------')

tree = ET.parse('./26_holders.xml')
root_element = tree.getroot()
print(ET.tostring(root_element))

print('------------------------------------------')


# Get 'coin' attribute
coin = root_element.get('coin')
print(f"Crypto name = {coin}")

print('------------------------------------------')

# To set a new 'launched' attribute
root_element.set('launched', '20240627')
# check attributes on root !
print(f'root_element.attrib = {root_element.attrib}')


# Save updated XML
tree.write('./26_holders.xml')  # check that xml file updated !

print('------------------------------------------')

# Add an 'id' attribute to each investor
id = 0
for investor in tree.findall('investor'):
    id += 1
    investor.set('id', str(id))

# Save updated XML
tree.write('./26_holders.xml')  # check that xml file updated !
print(('Added "id" to each investor !'))


print('------------------------------------------')

# Delete 'id' attributes
for investor in tree.findall('investor'):
    del (investor.attrib['id'])

# Save updated XML
tree.write('./26_holders.xml')  # check that xml file updated !
print(('Deleted "id" form each investor !'))

print('------------------------------------------')

# Add new investor method 1

investor_1 = ET.fromstring('<investor>Allan Carr</investor>')
root_element.append(investor_1)
# Save updated XML
tree.write('./26_holders.xml')  # check that xml file updated !
print(('investor_1 saved to file !'))

print('------------------------------------------')

# Add new investor method 1

investor_2 = ET.Element('investor')
investor_2.text = "Karl Zero"
root_element.append(investor_2)
# Save updated XML
tree.write('./26_holders.xml')  # check that xml file updated !
print(('investor_2 saved to file !'))


print('------------------------------------------')

for (id, investor) in enumerate(root_element.findall('investor')):
    investor.set('id', str(id))

tree.write('./26_holders.xml')  # check that xml file updated !


print('------------------------------------------')

# Select investor n°4 :

investor = root_element.find(".//investor[@id='4']")
print(investor.text)
