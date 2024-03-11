import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle



data = pd.read_csv ("data-final.csv", sep = "\t")

data.drop(data.columns[50:], axis=1, inplace=True)

# Filter rows where all values in the first 50 columns are less than or equal to 5
data = data[data.apply(lambda row: all(row.astype(float) <= 5), axis=1)]

# Select the first 50 columns
data = data.iloc[:, :50]

data["Extroversion"] = 20 + data["EXT1"] - data["EXT2"] + data["EXT3"] - data["EXT4"] + data["EXT5"] - data["EXT6"] + data["EXT7"] - data["EXT8"] + data["EXT9"] - data["EXT10"]
data["Agreeableness"] = 14 - data["AGR1"] + data["AGR2"] - data["AGR3"] + data["AGR4"] - data["AGR5"] + data["AGR6"] - data["AGR7"] + data["AGR8"] + data["AGR9"] + data["AGR10"]
data["Conscientiousness"] = 14 + data["CSN1"] - data["CSN2"] + data["CSN3"] - data["CSN4"] + data["CSN5"] - data["CSN6"] + data["CSN7"] - data["CSN8"] + data["CSN9"] + data["CSN10"]
data["Neuroticism"] = 38 - data["EST1"] + data["EST2"] - data["EST3"] + data["EST4"] - data["EST5"] - data["EST6"] - data["EST7"] - data["EST8"] - data["EST9"] - data["EST10"]
data["Openness"] = 8 + data["OPN1"] - data["OPN2"] + data["OPN3"] - data["OPN4"] + data["OPN5"] - data["OPN6"] + data["OPN7"] + data["OPN8"] + data["OPN9"] + data["OPN10"]

# List of Big Five personality traits columns
big_five_columns = ["Extroversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"]

# Calculate the maximum value for each row among the Big Five personality traits
data["label"] = data[big_five_columns].idxmax(axis=1)

columns_reorder= ["EXT1", "AGR1", "CSN1", "EST1", "OPN1", "EXT2", "AGR2", "CSN2", "EST2", "OPN2", "EXT3", "AGR3", "CSN3", "EST3", "OPN3", "EXT4", "AGR4", "CSN4", "EST4", "OPN4",
"EXT5", "AGR5", "CSN5", "EST5", "OPN5", "EXT6", "AGR6", "CSN6", "EST6", "OPN6", "EXT7", "AGR7", "CSN7", "EST7", "OPN7", "EXT8", "AGR8", "CSN8", "EST8", "OPN8",
                  "EXT9", "AGR9", "CSN9", "EST9", "OPN9", "EXT10", "AGR10", "CSN10", "EST10", "OPN10", "label"]
data = data [columns_reorder]

data.dropna(inplace=True)

array = data.values
x = array [:, 0:50]
y = array [:, 50]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size = 0.2, random_state = 7)

name = "LR_Modified"
model = (LogisticRegression(multi_class='multinomial'))
model.fit(x_train, y_train)
y_predicted = model.predict(x_test)

accuracy = accuracy_score(y_test, y_predicted) * 100
formatted_accuracy = f"{accuracy:.3f}%"

labels = data ["label"]
# Initialize the LabelEncoder
label_encoder = LabelEncoder()
# Fit and transform the labels to numerical values
encoded_labels = label_encoder.fit_transform(labels)
# Create a mapping of original labels to encoded values
label_to_encoded = {labeling: encoded for labeling, encoded in zip(labels, encoded_labels)}
x_test = np.array([[2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4,4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1,1,1,1,1,1,1,1,1,1]])  # Make sure to provide the same number of features (columns) as x_train
y_predicted2 = model.predict(x_test)


encoded_to_label = {encoded: label for label, encoded in label_to_encoded.items()}
predicted_label = encoded_to_label.get(int (y_predicted2[0]), "Unknown")

pickle.dump (model, open ("model.pkl", "wb"))
