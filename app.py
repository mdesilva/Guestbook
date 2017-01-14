from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql9153699:TMcPuWiXcf@sql9.freemysqlhosting.net/sql9153699'

db = SQLAlchemy(app)

#create table with name and comment in database
class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))

@app.route("/")
def index():
	results = Comments.query.all()
	return render_template("index.html", results=results)

@app.route("/sign")
def sign():
	return render_template("sign.html")

@app.route("/process", methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	signature = Comments(name=name, comment=comment) #create new row 
	db.session.add(signature) #add data to database
	db.session.commit() #save changes
	return redirect(url_for('index')) #redirect to index page upon submit


#run app 
if __name__=='__main__':
	app.run(debug=True)
