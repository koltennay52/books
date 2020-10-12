from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/browse")
def browse():
    return render_template("browse.html")

#routes for category main pages 
@app.route("/browse/fantasy")
def fantasy():
    return render_template("fantasy.html")

@app.route("/browse/sciencefiction")
def sciencefiction():
    return render_template("sciencefiction.html")

@app.route("/browse/sports")
def sports():
    return render_template("sports.html")

#routes for fantasy books
@app.route("/browse/fantasy/seaofstars")
def seaofstars():
    return render_template("./fantasybooks/seaofstars.html")

@app.route("/browse/fantasy/piranesi")
def piranesi():
    return render_template("./fantasybooks/piranesi.html")

@app.route("/browse/fantasy/deadlyeducation")
def deadlyeducation():
    return render_template("./fantasybooks/deadlyeducation.html") 

#routes for science fiction books 
@app.route("/browse/sciencefiction/earlydepartures")
def earlydepartures():
    return render_template("./sfbooks/earlydepartures.html")

@app.route("/browse/sciencefiction/hench")
def hench():
    return render_template("./sfbooks/hench.html")

@app.route("/browse/sciencefiction/skyhunter")
def skyhunter():
    return render_template("./sfbooks/skyhunter.html")

#routes for sports books
@app.route("/browse/sports/farfromnormal")
def farfromnormal():
    return render_template("./sportsbooks/farfromnormal.html")

@app.route("/browse/sports/theinsomniacs")
def theinsomniacs():
    return render_template("./sportsbooks/theinsomniacs.html")

@app.route("/browse/sports/furia")
def furia():
    return render_template("./sportsbooks/furia.html")   