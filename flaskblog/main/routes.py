from flask import render_template, request, Blueprint, abort, url_for, send_from_directory,jsonify
from flaskblog.models import Post,User,Stock
from flask import current_app
from flask_login import login_required
from PIL import Image
from flaskblog.users.utils import save_picture
import os
import datetime

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')



@main.route("/category/<category_name>")
def get_category_post(category_name):
    category_list = ['daily','test','tech']
    if category_name not in category_list:
        abort(404)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category=category_name).order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('category_post.html', category_name=category_name, posts=posts, title=category_name)


@main.route('/files/<path:filename>')
def uploaded_files(filename):
    path = os.path.join(current_app.root_path,'static/profile_pics')
    return send_from_directory(path, filename)

@login_required
@main.route('/upload', methods=['POST'])
def upload():
    # 获取上传图片文件对象 getlist获取多个
    f = request.files.get('upload')  
    # 最大5m
    # maxSize = 5242880  
    # if f.size > maxSize:
    #     return upload_fail(message="maxsize 5M")
    # 验证文件类型示例
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']: 
        return jsonify(message='Image only!') 
    picture_file = save_picture(f)
    url = url_for('main.uploaded_files', filename=picture_file)
    return jsonify(filename='',uploaded=1,url=url)



@main.route("/stock")
def getStock():
    one_day_ago = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    stocks = Stock.query.filter(Stock.ctime>one_day_ago).order_by(Stock.hot.desc()).limit(20).all()
    # stocks = Stock.query.distinct(Stock.code).all()
    return render_template('stock.html', stocks=stocks)