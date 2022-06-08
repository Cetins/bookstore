from flask import Flask, redirect, render_template, request
from flask import Blueprint
from repositories import author_repository, book_repository
from models.author import Author
from models.book import Book


bookstore_blueprint = Blueprint("bookstore", __name__)

@bookstore_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    authors = author_repository.select_all()
    
    return render_template("books/index.html", books=books, authors=authors)

@bookstore_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@bookstore_blueprint.route("/books", methods=["POST"])
def add_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    
    book = Book(title, genre, author_id)
    book_repository.save(book)
    
    return redirect("/books")

@bookstore_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors=authors)
    