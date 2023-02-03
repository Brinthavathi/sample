from flask import Flask, render_template

app =  Flask(__name__)
dic=[{"id":1,"name":"brindha","dept":"MCA","id":2,"name":"banu","dept":"CS","id":3,"name":"kavi","dept":"BCA","id":4,"name":"manju","dept":"prabha","id":5,"name":"kani","dept":"CC"},{"id":2,"name":"banu","dept":"MATHS"}]

@app.route("/<username>")

def hello_world(username):
   # return "<h1>hii iam Brintha</h1>"
   return render_template("index.html",data=username)

@app.route("/")

def hello_word():
   return render_template("index.html",data=dic[0]["name"],date=dic[1]["name"])

if __name__ == "__main__":
   app.run(debug=True)    