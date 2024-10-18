from flask import Flask, render_template, request, make_response
from pipeline_predict import pipeline_predict

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page with empty prediction and user input
    response = make_response(render_template('index.html', prediction_text='', user_input=''))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['user_input_text']
    # Call the prediction pipeline
    prediction = pipeline_predict(user_input).lower()

    # Update the prediction text based on the prediction result
    prediction_text = 'این نظر مثبته :)' if prediction == 'happy' else 'این نظر منفیه :('
    
    # Render the template with the prediction and user input
    return render_template('index.html', prediction_text=prediction_text, user_input=user_input)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
