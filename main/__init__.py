import os
from flask import Flask, render_template, redirect, url_for, abort, request
from .check_form import LoanCheckForm
from .ml_backend import loan_approval_predict, convert_to_dict
import json
import traceback


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='hieunt mse ddm501 project')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = LoanCheckForm()
        if form.validate_on_submit():
            data = json.dumps(convert_to_dict(form))
            return redirect(url_for('.check_approval', data=data))
        return render_template('index.html', form=form)

    @app.route('/result')
    def check_approval():
        try:
            data = json.loads(request.args['data'])
            name = data['name']
            age = data['age']
            gender = data['gender']
            status_pred, confidence = loan_approval_predict(data)
            print(f'Status: {status_pred}\nConfidence: {confidence}')
            return render_template('result.html', name=name, age=age,
                                   gender=gender, status=status_pred)
        except Exception as ex:
            print(traceback.format_exc())
            return abort(404)

    @app.errorhandler(404)
    def handle_bad_request(e):
        return render_template('404.html')

    return app
