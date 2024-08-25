from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your model using joblib
try:
    model = joblib.load('weather_prediction_model.pkl')
except Exception as e:
    print(f"Error loading the model: {e}")
    exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get data from request
        features = np.array(data['features']).reshape(1, -1)  # Reshape for single prediction
        prediction = model.predict(features)[0]  # Predict
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)