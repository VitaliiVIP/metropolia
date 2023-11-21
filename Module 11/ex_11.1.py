class Publication:
    def __init__(self, name):
        self.name=name

    def print_information(self):
        print(f"{self.name}")

class Book(Publication):
    def __init__(self, name, author, pages):
        self.author=author
        self.pages=pages
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Author - {self.author}\nPages - {self.pages}\n")

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor=editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Main editor - {self.editor}\n")

publications=[]
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))
for product in publications:
    product.print_information()