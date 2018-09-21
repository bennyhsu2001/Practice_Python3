import xml.etree.ElementTree as ET

tree = ET.parse('employees.xml')

root = tree.getroot()

print(root.tag)  #employees

for child in root:
    print(child)

for ele in root.iter('name'):
    print(ele)

for ele in root.findall('employee'):
    print(ele.get('id'))   
    print(ele.find('name').text)

