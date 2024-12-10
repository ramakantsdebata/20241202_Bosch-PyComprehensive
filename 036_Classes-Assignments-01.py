def create_digital_book(**params):
    """
    Factory function to create a DigitalBook instance.
    Accepts all necessary parameters and passes them to the DigitalBook constructor.
    """
    return DigitalBook(**params)


class LibraryItem:
    def __init__(self, **kwargs):
        self.title = kwargs.pop('title', None)
        self.year = kwargs.pop('year', None)
        if not self.title or not isinstance(self.year, int):
            raise ValueError("Title must be provided, and year must be an integer.")

    def __str__(self):
        return f"{self.title} ({self.year})"


class Book(LibraryItem):
    def __init__(self, **kwargs):
        self.author = kwargs.pop('author', None)
        if not self.author:
            raise ValueError("Author must be provided.")
        super().__init__(**kwargs)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class DigitalItem(LibraryItem):
    def __init__(self, **kwargs):
        self.file_size = kwargs.pop('file_size', None)
        if self.file_size is None or self.file_size < 0:
            raise ValueError("File size must be non-negative.")
        super().__init__(**kwargs)

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.file_size} MB"


class DigitalBook(Book, DigitalItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.file_size} MB"


def main():
    try:
        # Valid DigitalBook creation
        db1 = create_digital_book(title="Python Essentials", year=2023, author="John Doe", file_size=50)
        print(db1)

        # Missing file_size
        db2 = create_digital_book(title="Python Basics", year=2023, author="Jane Doe")
    except ValueError as e:
        print(f"EXCEPTION: {e}")

    try:
        # Invalid file size
        db3 = create_digital_book(title="Python Pro", year=2022, author="Sam Smith", file_size=-10)
    except ValueError as e:
        print(f"EXCEPTION: {e}")

    try:
        # Missing author
        db4 = create_digital_book(title="Advanced Python", year=2021, file_size=40)
    except ValueError as e:
        print(f"EXCEPTION: {e}")


if __name__ == "__main__":
    main()
