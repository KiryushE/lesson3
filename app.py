from flask import Flask, render_template, url_for, redirect, abort

app = Flask(__name__)

max_score = 20
test_name = "Flask"


students = [
    {"id": 1, "name": "Andriy", "score": 10, "description": "asahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaks"},
    {"id": 2, "name": "Oleh", "score": 20, "description": "asahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaks"},
    {"id": 3, "name": "Artem", "score": 5, "description": "asahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaks"},
    {"id": 4, "name": "Dmytro", "score": 15, "description": "asahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaksasahkdjkhaks"}
]

books_list = [
    {"id": 1, "name": "Book1", "status": "🔍Читаю"},
    {"id": 2, "name": "Book2", "status": "🗑Кинув"},
    {"id": 3, "name": "Book3", "status": "🔍Читаю"},
    {"id": 4, "name": "Book4", "status": "📋В планах"},
]


@app.route("/")
def home_page():
    return render_template("home.html", owner="John")


@app.route("/max")
def max_score():
    return render_template("max.html", students=students)


@app.route("/sum")
def sum_score():
    return render_template("sum.html", students=students)


@app.route("/sorted")
def sorted_score():
    return render_template("sorted_score.html", students=students)


@app.route('/students/')
def home():
    print(url_for("home"))
    context = {
        "title": "Students",
        "students": students,
        "max_score": max_score,
        "test": test_name
    }
    return render_template('index.html', **context)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/books")
def books():
    return render_template("books.html", books_list=books_list)


@app.route("/books/<int:id>")
def book_id(id):
    if id > len(books_list):
        return redirect(url_for("home"))
    return render_template("book_detail.html", book_detail=books_list[id-1])


@app.route("/student/<int:id>")
def student(id):
    if id > len(students):
        return redirect(url_for("home"))
    elif id == 4:
        abort(403)
    return render_template("detail.html", student=students[id-1])


@app.errorhandler(404)
def error404(error):
    return render_template("error404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)

