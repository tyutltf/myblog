"""用户管理
"""
from flask import Blueprint, render_template, redirect, url_for, request

um = Blueprint('um', __name__, url_prefix="/um")


# 主页
@um.route('/main/', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        return render_template('um_main.html')
