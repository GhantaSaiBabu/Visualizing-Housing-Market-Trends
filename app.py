from flask import Flask, send_file, abort
import os

app = Flask(__name__)

# Helper: safely return file from project root
def serve_root_file(filename: str):
    filepath = os.path.join(app.root_path, filename)
    if os.path.exists(filepath):
        return send_file(filepath)
    else:
        abort(404)

@app.route("/")
def index():
    return serve_root_file("index.html")

@app.route("/about")
def about():
    return serve_root_file("about.html")

@app.route("/dashboard")
def dashboard():
    return serve_root_file("dashboard.html")

@app.route("/story")
def story():
    return serve_root_file("story.html")

# (Optional) If you keep assets in /static,
# Flask will serve them automatically:  url_for('static', filename='logo.webp')

if __name__ == "__main__":
    # Use host="0.0.0.0" for Docker or external access
    app.run(debug=True)
