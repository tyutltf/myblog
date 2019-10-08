"""后台管理
"""
from flask import Blueprint, render_template, redirect, url_for, request

mg = Blueprint('mg', __name__, url_prefix="/mg")

# 主页
@mg.route('/main/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        if username == 'admin' and password == 123456:
            return render_template('um_main.html', message='欢迎您~')
        else:
            return render_template('admin.html', error='抱歉,用户名或密码错误！')
