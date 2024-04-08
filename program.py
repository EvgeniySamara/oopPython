from contact import Contact
 # from Webout.webout import Webout



def main():
    c1 = Contact(1)
    c2 = Contact(3)
    c3 = Contact(3)

    contacts = [c1, c2, c3]

    for c in contacts:
        print(c.to_string())

    # wb = Webout()
    # print(wb.__dict__)
    #wb.run
    print(c1.__repr__())
    print(c1.__str__())


if __name__ == '__main__':
    main()
