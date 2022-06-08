from flask import Flask, render_template
from controllers.bookstore_controller import bookstore_blueprint

app = Flask(__name__)

app.register_blueprint(bookstore_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
