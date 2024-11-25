from flask import Flask, render_template, request
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load your pre-trained model (replace 'model.pkl' with your model file)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")  # HTML file should be named 'index.html' and in the templates folder

@app.route("/process", methods=["POST"])
def process_form():
    try:
        # Collect all inputs from the form
        age = int(request.form["age"])
        gender = request.form["sex"]  # Updated to "sex" from "gender" to match the form
        cp = int(request.form["cp"])
        trestbps = int(request.form["trestbps"])
        chol = int(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = int(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])
        thal = int(request.form["thal"])

        # Encode gender
        gender_encoded = 0 if gender == "0" else 1  # Gender "0" for Female, "1" for Male

        # Create input array for the model
        input_features = np.array([[age, gender_encoded, cp, trestbps, chol, fbs, restecg,
                                    thalach, exang, oldpeak, slope, ca, thal]])

        # Predict with the model
        prediction = model.predict(input_features)
        prediction_text = "Heart Disease Risk: High" if prediction[0] == 1 else "Heart Disease Risk: Low"

        return render_template("index.html", prediction_text=prediction_text)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
