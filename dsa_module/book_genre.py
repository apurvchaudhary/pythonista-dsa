# List of books, list of Genre of books and book ratings was given, all list were of equal length.
# book[], genre[], rating[] of equal length n
#
# Now there were 2 methods which we need to implement,
# 1. getHighestRatingBookByGenre("Genre_name") If same rating books then lexographical order
# 2. updateBookRatingbyBookName("book_name", int rating)


class BookManager:
    def __init__(self, book, genre, rating):
        self.book = book
        self.genre = genre
        self.rating = rating
        self.book_index = {}
        self.genre_highest_rating = {}
        count = 0
        for genre, book, rating in zip(self.genre, self.book, self.rating):
            if genre in self.genre_highest_rating:
                if rating > self.genre_highest_rating[genre][1]:
                    self.genre_highest_rating[genre] = (book, rating)
                elif rating == self.genre_highest_rating[genre][1]:
                    if book < self.genre_highest_rating[genre][0]:
                        self.genre_highest_rating[genre][0] = book
            else:
                self.genre_highest_rating[genre] = [book, rating]
            self.book_index[book] = count
            count += 1

    def get_highest_rating_book_by_genre(self, genre: str) -> str:
        if genre in self.genre_highest_rating:
            return self.genre_highest_rating[genre][0]
        raise KeyError(f"{genre} not found")

    def update_book_rating_by_book_name(self, book, rating):
        if book not in self.book_index:
            raise KeyError(f"{book} not found")
        book_index = self.book_index[book]
        self.rating[book_index] = rating
        if rating > self.genre_highest_rating[self.genre[book_index]][1]:
            self.genre_highest_rating[self.genre[book_index]] = [book, rating]


# Example usage:
books = ["Book1", "Book2", "Book3", "Book4", "Apart"]
genres = ["Genre1", "Genre2", "Genre1", "Genre2", "Genre1"]
ratings = [4.1, 3.8, 4.1, 4.0, 4.1]

book_manager = BookManager(books, genres, ratings)

print(book_manager.get_highest_rating_book_by_genre("Genre1"))
