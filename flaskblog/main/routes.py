from flask import render_template, request, Blueprint, abort
from flaskblog.models import Post,User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
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
    posts = Post.query.filter_by(category=category_name).order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('home.html', title=category_name, posts=posts)




