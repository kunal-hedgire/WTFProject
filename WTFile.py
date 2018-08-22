from flask import Flask, render_template, request, flash
from ContactForm import Contactform
     #class name        functions name
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contactform()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')

            return render_template('contact.html', form=form)
        else:
            print(request.form)
            return render_template('regSuccess.html',msg = "Form submitted Successfully..!",result=request.form)
    elif request.method == 'GET':
            return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)