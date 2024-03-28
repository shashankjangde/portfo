from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<string:page_name>")
def navigator(page_name="index.html"):
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # delimiter is the seperator, we used "," to seperate. We can also use " "
        # quotechar means whenever if there is a need to use quote, what should be used, here we used double quotes
        # csv.QUOTE_MINIMAL means use the quotechar only when its necessary
        csvwriter = csv.writer(database, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def form_submitted():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        print(data)
        name = data["email"].split("@")[0]
        print(name)
        return render_template("thankyou.html", name=name)
        # return redirect("thankyou.html")
        # in the thankyou.html we need to remove the variable i.e. the curly bracket(templating engine)
        # redirect is a method from Flask module which will redirect the user to the mentioned page
    else:
        return "Something went wrong please try again!"
