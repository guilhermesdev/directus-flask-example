from flask import Flask, render_template
import directus

app = Flask(__name__)


@app.get("/")
def home():
    global_data = directus.get_global_data()

    return render_template(
        "home.html", title=global_data["title"], description=global_data["description"]
    )
