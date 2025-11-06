import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load the dataset
data = pd.read_csv("fertilizer_recommendation.csv")

# Preprocess dataset values to lowercase
data['Soil Type'] = data['Soil Type'].str.lower()
data['Crop Type'] = data['Crop Type'].str.lower()
# Label encoding for categorical features
le_soil = LabelEncoder()
data['Soil Type'] = le_soil.fit_transform(data['Soil Type'])
le_crop = LabelEncoder()
data['Crop Type'] = le_crop.fit_transform(data['Crop Type'])



# Splitting the data into input and output variables
X = data.iloc[:, :8]
y = data.iloc[:, -1]

# Training the Decision Tree Classifier model
dtc = DecisionTreeClassifier(random_state=0)
dtc.fit(X, y)

# Saving the model to a file
joblib.dump(dtc, 'fertilizer_model.pkl')

# Function to predict fertilizer based on user input
# Function to predict fertilizer based on user input
# Function to predict fertilizer based on user input
def predict_fertilizer(input_list):
    jsont, jsonh, jsonsm, jsonsoil, jsoncrop, jsonn, jsonp, jsonk = input_list
    
    
    
    # Convert input values to lowercase
    jsonsoil = jsonsoil.lower()
    jsoncrop = jsoncrop.lower()
    
    if "clay" in jsonsoil:
        jsonsoil = "clayey"
    # Encoding categorical input
    soil_enc = le_soil.transform([jsonsoil])[0]
    crop_enc = le_crop.transform([jsoncrop])[0]

    # Get the user inputs and store them in a numpy array
    user_input = [[jsont, jsonh, jsonsm, soil_enc, crop_enc, jsonn, jsonp, jsonk]]

    # Predict the fertilizer name
    fertilizer_name = dtc.predict(user_input)[0]

    # Return the prediction as a string
    return str(fertilizer_name)


# # Sample user input list (you can replace these values with your own)
# input_list = [26, 52, 38, 'clay', 'Maize', 37, 0, 0]

# # # # Call the function to predict fertilizer based on the sample user input list
# prediction = predict_fertilizer(input_list)

# # # # Print the prediction
# print(prediction)

# # Sample user input (you can replace these values with your own)
# jsonn = 37
# jsonp = 0
# jsonk = 0
# jsont = 26
# jsonh = 52
# jsonsm = 38
# jsonsoil = 'Sandy'
# jsoncrop = 'Maize'

# # Encoding categorical input
# soil_enc = le_soil.transform([jsonsoil])[0]
# crop_enc = le_crop.transform([jsoncrop])[0]

# # Get the user inputs and store them in a numpy array
# user_input = [[jsont, jsonh, jsonsm, soil_enc, crop_enc, jsonn, jsonk, jsonp]]

# # Predict the fertilizer name
# fertilizer_name = dtc_loaded.predict(user_input)

# # Return the prediction as a string
# print(str(fertilizer_name[0]))
