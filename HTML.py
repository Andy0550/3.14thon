# Michael Dvořák
# Python_3.7.0

import collections

GoT = collections.namedtuple("noble_houses","house_name noble_name noble_surname house_motto")
houses= []

houses.append(GoT("House Baratheon", "extinct", "extinct", "Ours Is the Fury"))
houses.append(GoT("House Bolton", "extinct" , "extinct", "Our Blades Are Sharp")) 
houses.append(GoT("House Lannister", "Jaime", "Lannister", "Hear Me Roar!"))
houses.append(GoT("House Martell", "Ellaria", "Sand", "Unbowed, Unbent, Unbroken"))
houses.append(GoT("House Stark", "Sansa", "Stark", "Winter Is Coming"))
houses.append(GoT("House Targaryen", "Daenerys", "Targaryen", "Fire and Blood"))
houses.append(GoT("House Tully", "Edmure", "Tully", "Family, Duty, Honor"))
houses.append(GoT("House Greyjoy", "Euron", "Greyjoy", "We Do Not Sow"))
houses.append(GoT("House Arryn", "Robin", "Arryn", "As High as Honor"))
houses.append(GoT("House Stokeworth", "Tanda", "Stokeworth", "Proud to Be Faithful"))


f = open("hw10_dvorak.html", "w", encoding="utf8")

table = '<html><table border="1"><tr><th>House Name</th><th>Noble Name</th><th>Noble Surname</th><th>House Motto</th></tr>'

for x in houses:
    table += "<tr>"
    for y in x:
        table += "<td>" + y + "</td>" 
    table += "</tr>"
    
table += "</table></html>"


f.write(table)    
f.close()

