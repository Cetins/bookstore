from flask import Flask, render_template
from repositories import author_repository, book_repository
from models.author import Author
from models.book import Book

from flask import Blueprint

bookstore_blueprint = Blueprint("bookstore", __name__)

@bookstore_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)