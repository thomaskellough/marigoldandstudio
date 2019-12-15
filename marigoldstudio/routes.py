from flask import Flask, render_template, url_for, flash, redirect
from marigoldstudio import app
from marigoldstudio.forms import RegistrationForm
import smtplib
import os

company_name = "Marigold & Studio"
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', company=company_name)


@app.route('/services')
def services():
    return render_template('services.html', title='Services', company=company_name)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = RegistrationForm()

    if form.validate_on_submit():

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(os.environ.get('MARIGOLD_EMAIL'), os.environ.get('MARIGOLD_PASS'))
        from_address = os.environ.get('MARIGOLD_EMAIL')
        to_address = os.environ.get('MARIGOLD_TOEMAIL')
        if form.phone.data:
            phone = form.phone.data
        else:
            phone = 'Not provided'
        message = f"Name - {form.name.data}\nEmail - {form.email.data}\nPhone - {phone}\nMessage - {form.text.data}"
        smtpObj.sendmail(from_addr=from_address, to_addrs=to_address, msg=message)
        smtpObj.quit()

        flash(f'Thank you for your message, {form.name.data}. You should hear back from me soon!', 'success')
        return redirect(url_for('home'))
    elif form.errors:
        flash(f'Please correct the errors and resubmit the form.', 'danger')
        return render_template('contact.html', title='Contact Me', company=company_name, form=form)
    return render_template('contact.html', title='Contact', company=company_name, form=form)


@app.route('/treatments-json')
def treatments_json():
    return render_template('treatments.json')


@app.route('/notifications-json')
def notifications_json():
    return render_template('notifications.json')


if __name__ == '__main__':
    app.run()
