"""用户管理
"""
from flask import Blueprint, render_template, request

um = Blueprint('um', __name__, url_prefix="/um")


# 主页
@um.route('/main/', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        return render_template('um_main.html')

# 生活


@um.route('/life/', methods=['GET', 'POST'])
def life():
    if request.method == "GET":
        return render_template('um_life.html')

# 总结


@um.route('/zongjie/', methods=['GET', 'POST'])
def zongjie():
    if request.method == "GET":
        return render_template('um_zongjie.html')

# 关于我


@um.route('/about/', methods=['GET', 'POST'])
def about():
    if request.method == "GET":
        return render_template('um_about.html')
