from flask import Flask, request, render_template
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "Box_Office_Revenue_Prediciton.pkl")
model = pickle.load(open(model_path, 'rb'))

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
