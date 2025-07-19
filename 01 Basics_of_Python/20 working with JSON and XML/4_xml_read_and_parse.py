import xml.etree.ElementTree as ET

# Sample XML string
xml_data = """
<person>
    <name>Nirav</name>
    <age>25</age>
    <skills>
        <skill>Python</skill>
        <skill>ML</skill>
    </skills>
</person>
"""

# Parse from string
root = ET.fromstring(xml_data)

print("Name:", root.find("name").text)
print("Skills:")
for skill in root.find("skills"):
    print("-", skill.text)