from flask import render_template, jsonify
from app import app, forms, predict

@app.route('/')
def index():
    return 'Hello Loh(Sanya)'


@app.route('/iris', methods=['GET', 'POST'])
def predict_iris():
    form = forms.IrisForm()
    if form.validate_on_submit():
        pl, pw, sl, sw = form.petal_length.data, form.petal_width.data, form.sepal_length.data, form.sepal_width.data
        result = predict.predict([pl, pw, sl, sw])
        return jsonify({'predicted_class': int(result)})
    return render_template('iris.html', form=form, result='oops')