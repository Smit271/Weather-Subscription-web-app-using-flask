from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from form import RegistrationForm, Weather
from flask_sqlalchemy import SQLAlchemy
from Current_Weather_API import Weather_detail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdv1asdc91v9ads8vcs5xc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
db = SQLAlchemy(app)

class Subscribers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mail_id = db.Column(db.String(50), nullable=False)
    city_name = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f"{self.name} with {self.mail_id} for {self.city_name}"

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    form  = Weather()  
    if request.method == 'POST':
        city = request.form.get('city_name')
        weather = Weather_detail(str(city))
        details = weather.weather()
        #name = details[0]
        #temp = details[2]
        #discription = details[1]
        return render_template('main.html', form = form , result = details)
    return render_template('main.html', form = form)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    db.session.commit()

    if request.method == 'POST':
        name = request.form.get('name')
        mail_id = request.form.get('email')
        city_name = request.form.get('city')

        if city_name and mail_id:
            existing_user = Subscribers.query.filter(
                Subscribers.city_name == city_name or Subscribers.mail_id == mail_id
            ).first()
            if existing_user:
                flash(f'{mail_id} for  city {city_name}  already subscribed!', 'danger   ')
                return redirect(url_for('home'))
            new_user = Subscribers(
                name=name,
                mail_id=mail_id,
                city_name=city_name
            )  # Create an instance of the Subscribers class
            db.session.add(new_user)  # Adds new Subscribers record to database
            db.session.commit()  # Commits all changes
            redirect(url_for('home'))

            with open('subscribers.txt' , 'a') as f:
                f.write(f"{name}, {mail_id}, {city_name}")
            f.close()
        if form.validate_on_submit():
            flash(f'Subscribed for {form.name.data}!', 'success')
            return redirect(url_for('home'))

    return render_template('register.html', title = 'Register', form = form)


if __name__ == "__main__":
	app.run(debug = True)