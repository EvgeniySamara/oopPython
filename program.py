from contact import Contact

c1 = Contact(1)
c2 = Contact(3)
c3 = Contact(3)

contacts = []
contacts.append(c1)
contacts.append(c2)
contacts.append(c3)

for c in contacts:
    print (c.to_string())

