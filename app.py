from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

def bot(msg):
    msg = msg.lower()

    if "fee" in msg:
        return "Fees: 60,000 - 1,20,000 per year"
    elif "course" in msg:
        return "Courses: AI, IT, CSE, Mechanical, Civil"
    elif "placement" in msg:
        return "Placement: 3-6 LPA average"
    else:
        return "Ask about fees, courses, placement, admission"

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    session["user"] = request.form["username"]
    return redirect("/chat")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        msg = request.form["message"]
        reply = bot(msg)

        messages = [
            {"role": "user", "text": msg},
            {"role": "bot", "text": reply}
        ]

        return render_template("index.html", messages=messages)

    return render_template("index.html", messages=[])


    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)