from flask import Flask
from flask import render_template
from flask import request
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('/home/mustafa/PycharmProjects/flaskProject/voting_clf.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.form['text']
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([data])
    # Take the first value of prediction
    output = prediction[0]

    return render_template('index.html', prediction_text='The sentiment of the text is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)