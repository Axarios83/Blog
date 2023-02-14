from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def render_home():
    return render_template("index.html")

@app.route("/ich", methods=['GET'])
def render_ich():
    return render_template("./blogs/ich.html")

@app.route("/gsx600f", methods=['GET'])
def render_gsx600f():
    return render_template("./blogs/gsx600f.html")

@app.route("/mt09tracer", methods=['GET'])
def render_mt09tracer():
    return render_template("./blogs/mt09tracer.html")

if __name__=='__main__':
    app.run(debug=True)