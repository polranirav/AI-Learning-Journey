import xml.etree.ElementTree as ET

# Create XML structure
person = ET.Element("person")
ET.SubElement(person, "name").text = "Nirav"
ET.SubElement(person, "age").text = "25"

skills = ET.SubElement(person, "skills")
ET.SubElement(skills, "skill").text = "Python"
ET.SubElement(skills, "skill").text = "AI"

# Write to XML file
tree = ET.ElementTree(person)
tree.write("person.xml")

print("XML written to person.xml")