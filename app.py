from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the model
model = pickle.load(open('Box_Office_Revenue_Prediciton.pkl', 'rb'))

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return {'status': 'ok'}, 200

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([np.array(features)])
        return render_template('index.html', prediction_text=f'Predicted Revenue: ${prediction[0]:,.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {e}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
