class Word:
    def __init__(self):
        self.wordbook = {}
    
    def add(self, eng, kor):
        self.wordbook[eng] = kor
    
    def delete(self, eng):
        if eng in self.wordbook:
            self.wordbook.pop(eng)
            return True
        else:
            return False

    def print(self):
        for eng, kor in self.wordbook.items():
            print(f'{eng}: {kor}')

my_book = Word()
my_book.add('grape', '포도')
my_book.add('peach', '복숭아')
my_book.add('watermelon', '수박')
my_book.add('mango', '망고')
my_book.print()
print(my_book.delete('watermelon'))
print(my_book.delete('mango'))
print(my_book.delete('carrot'))
my_book.print()