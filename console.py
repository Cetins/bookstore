import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


author_1 = Author("Santa Montefiore")
author_repository.save(author_1)
author_2 = Author("Elly Griffiths")
author_repository.save(author_2)
author_3 = Author("Lee Child")
author_repository.save(author_3)


book_1 = Book("Better Off Dead", "Novel",15)
book_repository.save(book_1)
book_2 = Book("The Midnight Hour", "Mystery", 14)
book_repository.save(book_2)
book_3 = Book("Distant Shores", "Thriller", 13)
book_repository.save(book_3)
