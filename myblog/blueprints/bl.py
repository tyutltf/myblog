"""技术
"""
from flask import Blueprint, render_template, request

bl = Blueprint('bl', __name__, url_prefix="/bl")


# 技术主页
@bl.route('/jishu/', methods=['GET', 'POST'])
def jishu():
    if request.method == "GET":
        return render_template('bl_jishu.html')

# 项目主页


@bl.route('/project/', methods=['GET', 'POST'])
def project():
    if request.method == "GET":
        return render_template('bl_project.html')

# 荐书主页


@bl.route('/book/', methods=['GET', 'POST'])
def book():
    if request.method == "GET":
        return render_template('bl_book.html')
