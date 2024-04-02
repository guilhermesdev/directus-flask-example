from flask import Flask, render_template, render_template_string
import directus

app = Flask(__name__)


@app.get("/")
def home():
    global_data = directus.get_global_data()

    return render_template(
        "home.html", title=global_data["title"], description=global_data["description"]
    )


@app.get("/<slug>")
def dynamic_page(slug):
    page = directus.get_page_by_slug(slug)

    if not page:
        return render_template_string(
            "{% extends 'base.html' %}{% block content %}This page does not exists{% endblock %}"
        )

    return render_template(
        "dynamic-page.html", title=page["title"], content=page["content"]
    )


@app.get("/blog")
def blog_page():
    posts = directus.get_posts()

    return render_template("blog.html", posts=posts)


@app.get("/blog/<slug>")
def post_page(slug):
    post = directus.get_post_by_slug(slug)

    return render_template("post.html", post=post)
