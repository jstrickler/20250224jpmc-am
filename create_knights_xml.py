import lxml.etree as et

root = et.Element('knights')
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip() # remove \n
        name, title, color, quest, comment = line.split(':')
        knight_tag = et.SubElement(root, "knight")
        name_tag = et.SubElement(knight_tag, "name", title=title)
        name_tag.text = name
        et.SubElement(knight_tag, "color").text = color
        et.SubElement(knight_tag, "quest").text = quest
        et.SubElement(knight_tag, "comment").text = comment

raw_xml_doc = et.tostring(root, pretty_print=True)
xml_doc = raw_xml_doc.decode()
print(xml_doc)

tree = et.ElementTree(root)
tree.write('knights.xml', pretty_print=True, xml_declaration=True)
