from flask import Flask, redirect, render_template, url_for
from myblog.blueprints import um, bl, mg

app = Flask(__name__)
app.register_blueprint(um.um)
app.register_blueprint(bl.bl)
app.register_blueprint(mg.mg)


@app.route('/')
def index():
    # 主页路由
    return redirect(url_for("um.main"))


@app.route('/login')
def login():
    # 登录后台管理
    return render_template("admin.html")


def run_server():
    app.run(host='127.0.0.1', port=647, debug=True)


if __name__ == "__main__":
    run_server()
