import flask
import os


app = flask.Flask(__name__)


@app.route("/sensor")
def feed1():
    return flask.render_template("feed1.html")

@app.route("/feed2")
def feed2():
    return flask.render_template("feed2.html")

@app.route("/video")
def feed3():
    return flask.render_template("feed3.html")

@app.route("/science")
def feed4():
    return flask.render_template("feed4.html")


if __name__ == "__main__":
    # app.run(host = '192.168.43.51')
    app.run(debug=True)
