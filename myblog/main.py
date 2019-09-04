from flask import Flask, redirect, render_template, url_for
from myblog.blueprints import um

app = Flask(__name__)
app.register_blueprint(um.um)


@app.route('/')
def index():
    # 主页路由
    return redirect(url_for("um.main"))


def run_server():
    app.run(host='127.0.0.1', port=8000, debug=True)


if __name__ == "__main__":
    run_server()
