class Contact:
    id = 0
    contact_kind = 0
    def main():
        pass

    if __name__ == '__main__':
        main()

    def __init__(self,ck):
        Contact.id +=1
        self.id =  Contact.id 
        self.contact_kind =ck

    def __repr__(self):
        return self.id
        
        
    def to_string(self):
        return f"id {self.id} вид контакта {self.contact_kind}"

