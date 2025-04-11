from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'sfsguiabfug'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)