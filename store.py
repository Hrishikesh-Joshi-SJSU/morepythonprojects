# ----------------------------------------------------------------------
# Name:      store
# Purpose:   illustrate the use of classes and inheritance
# Author(s): Hrishikesh Joshi and Paul Chon
# Date: 9 March 2023
# ----------------------------------------------------------------------
"""
This project will represent items sold by a fictional online store.

The program will implement four classes: Product, Book, VideoGame, and
Bundle. The product class will be used to represent generic items in the
store. Book and VideoGame will be used to represent specific items(books
and video games) sold by the store. Bundle will be used to represent
combinations of items sold by the store. For example, a bundle could
consist of 1 book, 2 video games, and 3 products.
"""

class Product:
    """The product class will be used to represent generic items sold
    in the store"""
    category = "GN"
    next_serial_number = 1
    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.stock = 0
        self.id = self.generate_product_id()
        self.sales = 0
        self.sales = []
        self.reviews = []
    def restock(self, quantity):
        '''
        this method updates the amount of items of a particular product.

        :param quantity: the amount by which the the stock of the item
        should increase
        :return: none.
        '''
        if quantity>0:
            self.stock += quantity
    def review(self, stars, text):
        '''

        this method represents a user reviewing a product. it updates
        the self.reviews list.
        :param stars: the # of stars the user of the product believes
        it deserves.
        :param text: the comments the user has while reviewing the
        product.
        :return: none
        '''
        if 0 <= stars <= 5:
            self.reviews.insert(-1, (stars, text))
    def sell(self, quantity, sale_price):
        '''
        this method represents the sale of a product. if the quantity
        is greater than the stock of the item, then this method will
        only count the sales of available stock of an item.

        :param quantity: the number of items of a product to be sold.
        :param sale_price: the price at which the items of a product
        will be sold at.
        :return: none
        '''
        if quantity>0 and sale_price>0:
            items_to_sell = min(quantity, self.stock)
            for i in range(items_to_sell):
                self.stock-=1
                self.sales.insert(-1, sale_price) # check this
    @ classmethod
    def generate_product_id(cls):
        '''
        this class method produces the id for each instanct of product.
        :return: the generated id of the product.
        '''
        id = f'{cls.category}{cls.next_serial_number:06}'
        cls.next_serial_number += 1
        return id


    @property
    def lowest_price(self):
        '''
        this property method return the lowest price the item was sold
        for.
        :return: the minimum sale value of the instance of product. it
        returns 'no sales' if the product has never been sold.
        '''
        if self.sales:
            return min(self.sales)
        return 'no sales'
    @property
    def average_rating(self):
        '''
        this property method calculates the average rating of the
        product by users
        :return: the average rating of product by users.
        '''
        total = 0
        if self.reviews:
            for i in self.reviews:
                total += i[0]
            return total/len(self.reviews)
        return 'no ratings'


    def __str__(self):
        ''' the string representation of product'''

        return f'{self.description}\nProduct id: {self.id}\nList Price' \
               f': {self.list_price}\nAvailable in stock: {self.stock}'

class VideoGame(Product):
    '''this class represents video game products of the fictional
    online store. it extends the product class'''
    category = 'VG'
    next_serial_number = 1
    def __init__self(self, description, list_price):
        super().__init__(self, description, list_price)
class Book(Product):
    '''
    this class represents book products of the fictional online store.
    it also extends the product class
    '''
    category = "BK"
    next_serial_number = 1
    def __init__(self, description, author, pages, list_price):
        super().__init__(description, list_price)
        self.pages = pages
        self.author = author
    def __lt__(self, other):
        ''' this method makes a book less than another book if
        the book has less pages than the other book.'''
        return self.pages<other.pages

def main():
    toy = VideoGame("5",5)
    print(toy.id)
    boy = VideoGame("5", 6)
    print(boy.id)
    coy = VideoGame("6", 6)
    print(coy.id)
if __name__ == '__main__':
    main()