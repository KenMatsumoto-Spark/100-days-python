from flask import Flask, render_template, request
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
data = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        data = request.form
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", message="Message Sent!")

    return render_template("contact.html", message="Contact Me")

# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route('/post/<int:id>')
def post(id):
    return render_template("post.html", post=data[id-1])

if __name__ == ("__main__"):
    app.run(debug=True)