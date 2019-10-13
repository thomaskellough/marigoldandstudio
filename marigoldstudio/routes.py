from flask import Flask, render_template, url_for


app = Flask(__name__)

company_name = "Marigold & Studio"
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', company=company_name)


@app.route('/home2')
def home2():
    return render_template('home2.html', title='Home', company=company_name)


@app.route('/services')
def services():
    return render_template('services.html', title='Services', company=company_name)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', company=company_name)


if __name__ == '__main__':
    app.run()
