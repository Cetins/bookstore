DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    author_id INT REFERENCES authors(id)
);

INSERT INTO authors (first_name, last_name) VALUES ("Santa", "Montefiore");
INSERT INTO authors (first_name, last_name) VALUES ("Elly", "Griffiths");
INSERT INTO authors (first_name, last_name) VALUES ("Lee", "Child");

INSERT INTO books (title, genre, author_id) VALUES ("Better Off Dead", "Novel", 3);
INSERT INTO books (title, genre, author_id) VALUES ("The Midnight Hour", "Mystery", 2);
INSERT INTO books (title, genre, author_id) VALUES ("Distant Shores", "Thriller", 1);
