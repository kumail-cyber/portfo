from flask import Flask, render_template, request, redirect
import os
import csv
app = Flask(__name__)


@app.route('/<string:page_name>')
def login_func(page_name=None):
    return render_template(page_name)


def write_to_csv(data):
    database_file = open('database.csv', mode='a', newline='')
    email = data['email']
    message = data['message']
    subject = data['subject']
    writer = csv.writer(database_file, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

    writer.writerow([email, subject, message])


@app.route('/submit_func', methods=['POST', 'GET'])
def submit_func():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
