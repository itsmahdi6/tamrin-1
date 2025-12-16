class books :
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def display_details(self) :
        print(f"\n--- Books Information ---")
        print(f"books title is :{self.title}")
        print(f"Books author is :{self.author}")
        print(f"Books price is :{self.price}\n")
    def apply_discount(self,percent) :
        discount_amount = self.price*(percent/100)
        self.price-=discount_amount
book1 = books(f"crime and punishment","dastayofski" ,100000)
book2 = books(f"100 years solitude","garcia" ,150000)
print(f"first book information :")
book1.display_details()
print(f"second book information :")
book2.display_details()
book2.apply_discount(15)
print(f"final information for first book :")
book1.display_details()
print(f"final information for second book :")
book2.display_details()
            