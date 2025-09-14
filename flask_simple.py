# flask_app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake DB
books = {
    1: {"id": 1, "title": "Clean Code"},
    2: {"id": 2, "title": "Pragmatic Programmer"}
}
next_id = 3

# Get all books
@app.get("/books")
def get_books():
    return jsonify(list(books.values()))

# Get one book
@app.get("/books/<int:book_id>")
def get_book(book_id):
    return jsonify(books.get(book_id, {"error": "Not found"}))

# Create book
@app.post("/books")
def create_book():
    global next_id
    data = request.json
    new_book = {"id": next_id, "title": data["title"]}
    books[next_id] = new_book
    next_id += 1
    return jsonify(new_book), 201

# Update book
@app.put("/books/<int:book_id>")
def update_book(book_id):
    data = request.json
    if book_id not in books:
        return {"error": "Not found"}, 404
    books[book_id]["title"] = data["title"]
    return jsonify(books[book_id])

# Delete book
@app.delete("/books/<int:book_id>")
def delete_book(book_id):
    if book_id not in books:
        return {"error": "Not found"}, 404
    del books[book_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
