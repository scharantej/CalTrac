
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meals.db'
db = SQLAlchemy(app)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    calories = db.Column(db.Integer)
    date = db.Column(db.Date)

    def __repr__(self):
        return '<Meal %r>' % self.name

@app.route('/')
def index():
    meals = Meal.query.all()
    return render_template('index.html', meals=meals)

@app.route('/add_meal', methods=['POST'])
def add_meal():
    name = request.form['name']
    calories = request.form['calories']
    date = request.form['date']
    meal = Meal(name=name, calories=calories, date=date)
    db.session.add(meal)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
