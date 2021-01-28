from flask import Flask, render_template
app = Flask(__name__)

#to edit content inside chrome, type in the console
#document.body.contentEditable=true
#then download the html with the changes

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)