from wtforms import Form,StringField, validators, TextAreaField, SubmitField

class PostForm(Form):
    title= StringField('Name', validators=[validators.DataRequired()])
    content = TextAreaField('Organisation', validators=[validators.DataRequired()])
    submit = SubmitField('Post')
