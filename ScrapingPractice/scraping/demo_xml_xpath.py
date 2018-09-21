import xml.etree.ElementTree as ET

tree = ET.parse('employees.xml')
root = tree.getroot()

# print(root.findall('.'))   #[Employees]
# print(root.findall('..'))  #[]
# print(root.findall('*'))   #[employee,employee,contractor,partime]
# print(root.findall('.//name')) #[name,name,name,name]

# print(root.findall('*[@id]'))  #[employee,employee]
# print(root.findall('*[@id="b231334"]'))  #[employee]
# print(root.findall('*[hours]'))  #[partime,partime]
# print(root.findall('*[hours="6"]'))  #[partime]

print(root.findall('employee[1]/name')[0].text)
print(root.findall('employee[last()-1]/name')[0].text)
