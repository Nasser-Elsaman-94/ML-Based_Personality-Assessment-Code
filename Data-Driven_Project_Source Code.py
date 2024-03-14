import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
from pickle import GET, load
from forms_datadriven import DD_Form
from flask import Flask, render_template, url_for, redirect, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load the machine learning model
model = load(open("/home/nasserElsaman/mysite/model.pkl", "rb"))

# Set up credentials for Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/nasserElsaman/mysite/gspread-stuff/zeta-bonfire-407806-440e2251df97.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheets spreadsheet by title
spreadsheet = gc.open('PythonAnywhere ML Personality Assessment User Data')

app = Flask(__name__)
app.config ["SECRET_KEY"] = "use_your_secret_key_here!!!"


@app.route('/data-driven', methods=["GET", "POST"])
def datadrivenfunc():
    form = DD_Form()
    formValues_list = []  # Initialize the list
    prediction= None
    predicted_label = None
    formatted_accuracy = None

    if form.validate_on_submit():
        integer_list = []  # Initialize the list
        for i in range(1, 51):
            question_data = request.form.get(f"question{i}")
            formValues_list.append(int(question_data))

        # Reshape formValues_list to a 2D array
        formValues_list_2d = np.array(formValues_list).reshape(1, -1)


        labels = ['Agreeableness', 'Conscinciousness', 'Extroversion', 'Nuorticism', 'Openness']
        # Initialize the LabelEncoder
        label_encoder = LabelEncoder()
        # Fit and transform the labels to numerical values
        encoded_labels = label_encoder.fit_transform(labels)
        # Create a mapping of original labels to encoded values
        label_to_encoded = {labeling: encoded for labeling, encoded in zip(labels, encoded_labels)}

        label_predicted = model.predict(formValues_list_2d)

        encoded_to_label = {encoded: label for label, encoded in label_to_encoded.items()}
        predicted_label = encoded_to_label.get(int (label_predicted[0]), "Unknown")

        # Access the first worksheet (assuming one sheet in the spreadsheet)
        sheet = spreadsheet.sheet1

        # Append data to the sheet
        data_to_append = formValues_list + [predicted_label]
        sheet.append_row (data_to_append)
        return render_template('assessmentresult.html', form=form, formValues_list=formValues_list, predicted_label=predicted_label)
        
    return render_template('datadriven.html', form=form)

# Rest of your Flask app code

@app.route('/', methods= ["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/rule-based')
def first_wave():
    return render_template("rulebased.html")

@app.route('/data-driven')
def second_wave():
    return render_template ("datadriven.html")

@app.route('/assessment-result')
def results():
    return render_template ("assessmentresult.html")

@app.route('/gpt')
def third_wave():
    return render_template ("gpt.html")



if __name__ == '__main__':
    app.run(debug=True)
