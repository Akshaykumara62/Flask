from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_restful import Resource, Api
from forms import PostForm
from model import blog_detail13, db, app
# app = Flask(__name__)
api = Api(app)
@app.route("/image")
def image1():
    return render_template('image.html')

posts =[{
    'Name':'Akshay kumar',
    'Organisation': 'Cognitivzen technologies',
    'DOJ': '04-Apr-2022',
    'DOE': '23-Mar-2023'
}]

@app.route("/display", methods=['GET', 'POST'])
def dis():
    posts = blog_detail13.query.all()
    return render_template('display.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post1():
    form = PostForm(request.form)
    if form.validate():
        post1 = blog_detail13(form.title.data, form.content.data)
        db.session.add(post1)
        db.session.commit()
        return redirect(url_for('dis'))
    


    return render_template('create_post.html', form=form, legend = "Write Post Today")
@app.route('/json/<id>',methods=['GET', 'POST'])
def jsondata(id):
    data = blog_detail13.query.filter_by(blogid=id).first()
    print(data)
    return jsonify ({
        id:str(data)
    })

class Data1(Resource):
    def get(self, id):
        data = blog_detail13.query.filter_by(blogid=id).first()
        return {'about':str(data)}

api.add_resources(Data1, "/rest/<int:id>")


if __name__=="__main__":
    app.run()