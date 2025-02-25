import lxml.etree as et

tree = et.parse('knights.xml')
print(f"{tree = }")

root = tree.getroot()
print(f"{root = }")
for knight in root:
    print(knight.findtext('name'))
print()

for name_tag in tree.findall('.//name'):
    print(name_tag.text)