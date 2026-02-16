from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "todo.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    """)
    db.commit()
    db.close()


@app.route("/")
def home():
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    db.close()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title:
        db = get_db()
        db.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, 0))
        db.commit()
        db.close()
    return redirect(url_for("home"))


@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    db = get_db()
    task = db.execute("SELECT done FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if task is not None:
        new_done = 0 if task["done"] == 1 else 1
        db.execute("UPDATE tasks SET done = ? WHERE id = ?", (new_done, task_id))
        db.commit()
    db.close()
    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    db.close()
    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)