from flask import Flask, render_template
import requests
URL = " https://api.npoint.io/674f5423f73deab1e9a7"

app = Flask(__name__)
response = requests.get(url=URL)
posts_data = response.json()

@app.route('/')
def home():

 return render_template('index.html',posts=posts_data)

@app.route('/about')
def about():
 return render_template('about.html')

@app.route('/post/<int:id>')
def get_post(id):
 new_post = {}
 for post in posts_data:
   if post["id"] == id:
     new_post = post
 
 return render_template('post.html',post=new_post)

@app.route('/contact')
def contact():
 return render_template('contact.html')




if __name__ == "__main__":
    app.run(debug=True)
