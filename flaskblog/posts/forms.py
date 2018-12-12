from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[('daily','随笔'),('test','测试'),('tech','技术')])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
