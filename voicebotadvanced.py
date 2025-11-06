import speech_recognition as sr
import pyttsx3
import joblib
from fertiliserrecommend import predict_fertilizer
import difflib

# Define a dataset of questions and answers
qa_dataset = {
    "Can you provide more detail about PM Kissan Samman Yojna?": "PM Kisan Samman Nidhi Yojana is a scheme launched by the Government of India in 2019 to provide financial assistance to small and marginal farmers across the country. Under this scheme, eligible farmers receive a direct cash transfer of Rs. 6,000 per year in three equal installments of Rs. 2,000 each. The scheme aims to provide income support to farmers and help them meet their expenses related to agriculture and allied activities.To be eligible for the scheme, farmers must have cultivable land in their name and should be the owner of the land. The scheme is applicable to all farmers, including those who belong to the SC/ST category, and those who have taken loans from banks. The scheme is implemented by the Ministry of Agriculture and Farmers Welfare, Government of India.",
    
    "What is organic farming?": """Organic farming is a method of crop and livestock production that involves using natural inputs and techniques to minimize pollution, conserve water and soil, and promote biodiversity. Organic farmers do not use synthetic fertilizers, pesticides, or genetically modified organisms (GMOs). Instead, they rely on crop rotation, green manure, compost, and biological pest control to maintain soil fertility and control pests.""",

    "How can I improve soil fertility?": """To improve soil fertility, you can use organic matter such as compost, manure, and crop residues. These organic materials provide essential nutrients to the soil and improve its structure. You can also practice crop rotation and cover cropping to enhance soil health. Additionally, reducing tillage and avoiding the use of synthetic fertilizers and pesticides can help maintain soil fertility in the long run.""",

    "What are the benefits of drip irrigation?": "Drip irrigation saves water, improves plant health, controls weeds, enhances fertilizer efficiency, and reduces labor costs.",

    "What are the major pests affecting crops in India?": "Major pests affecting crops in India include bollworms, aphids, whiteflies, armyworms, and brown plant hoppers.",

    "What are the key components of organic farming?": "Key components of organic farming include soil management, pest management, weed management, crop diversity, and avoidance of synthetic inputs.",

    "How can I prevent pests and diseases in my paddy?": "You can prevent pests and diseases in your paddy by practicing crop rotation, using resistant varieties, maintaining proper water management, and timely application of organic or chemical pesticides.",

    "When is the right time to harvest my cotton?": "The right time to harvest cotton depends on the variety and local climate conditions. Generally, cotton is ready for harvest when bolls have fully matured and burst open. It's important to monitor your crop closely and harvest when the fiber quality is at its best.",

    "Which is the latest subsidy for Animal husbandry by Government?": "The latest subsidy for animal husbandry by the government includes schemes such as the Dairy Entrepreneurship Development Scheme (DEDS), National Livestock Mission (NLM), and the Rashtriya Gokul Mission, which aim to promote dairy farming and livestock development.",
    "What are some major government schemes  for the welfare of farmers?": "Some government schemes are : Pradhan Mantri Fasal Bima Yojana (PMFBY),Pradhan Mantri Kisan Samman Nidhi (PM-KISAN),Soil Health Card Scheme,National Agriculture Market(e-NAM),Rashtriya Krishi Vikas Yojana (RKVY)",
    "Pradhan Mantri Fasal Bima Yojana (PMFBY)": "PMFBY is a crop insurance scheme providing financial support in case of crop failure due to natural calamities, pests, or diseases.",
    "Pradhan Mantri Kisan Samman Nidhi (PM KISAN)": " PM-KISAN is  direct income support scheme offering eligible farmers Rs. 6,000 per year in three equal installments.",
    "pm kisan scheme":"PM-KISAN is  direct income support scheme offering eligible farmers Rs. 6,000 per year in three equal installments.",
    "Soil Health Card Scheme": "Soil Health Card Scheme aims to provide soil health cards to farmers, containing information on soil nutrient status and recommendations for nutrient application.",
    "National Agriculture Market (e-NAM)": "National Agriculture Market (e-NAM) is an online trading platform for agricultural commodities to create a unified national market for farmers.",
    "Rashtriya Krishi Vikas Yojana (RKVY)": "A scheme for agriculture and allied sector development, providing financial assistance to states for activities like crop diversification and infrastructure development.",
    "what is temperature for cotton crop?":"21 to 37°C temperature is required.",
    "what are the conditons for growing wheat? ":"The optimum growing temperature is about 25°C.It needs a lot of sunshine, especially when the grains are filling. It grows best when the soil pH is between 6.0 and 7.0.",
    "which condition is suitable for sugercane crop?":"It grows well in hot and humid climate with a temperature of 21°C to 27°C",
    "condition for rice crop":"It is best suited to regions which have high humidity, prolonged sunshine and an assured supply of water. The average temperature required throughout the life period of the crop ranges from 21 to 37º C.",
    "what is temperature for rice crop?":"the average temperature is between 21 to 37ºC",
    "condition for rice crop":"Rice crop needs a hot and humid climate.Rice grows on a variety of soils like silts, loams and gravels.It is best suited to regions which have high humidity, prolonged sunshine and an assured supply of water.The average temperature required throughout the life period of the crop ranges from 21 to 37º C",
    "condition for rice crop":"Rice crop needs a hot and humid climate.Rice grows on a variety of soils like silts, loams and gravels.It is best suited to regions which have high humidity, prolonged sunshine and an assured supply of water.The average temperature required throughout the life period of the crop ranges from 21 to 37º C",
    "How to know the right time to harvest vegetables":"Vegetables should be harvested when they are fully mature but before they become overripe. You can determine the maturity of the vegetable by checking its size, color, and texture. For example, tomatoes should be harvested when they are fully red and slightly soft to the touch.",
    "How to understand right time to harvest fruits":"Fruits should be harvested when they are fully ripe. You can determine the ripeness of the fruit by checking its color, texture, and smell. For example, mangoes should be harvested when they are fully yellow and have a sweet aroma."
     
    # Add more questions and answers as needed
}

# Load the trained models
crop_model = joblib.load('cropmodel.pkl')
fertilizer_model = joblib.load('fertilizer_model.pkl')

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
print(voices)
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)

# Function to match a user input to a question pattern
def match_question(input_text):
    for question, _ in qa_dataset.items():
        if question.lower() in input_text.lower():
            return True
    return False


# Function to handle user queries
def handle_query(user_input):
    max_similarity = 0
    best_match = None
    for question, answer in qa_dataset.items():
        similarity = difflib.SequenceMatcher(None, user_input.lower(), question.lower()).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = answer
    if max_similarity >= 0.6:  # Adjust the threshold as needed
        return best_match
    return None



# Function to get voice input with error handling and timeout
def get_voice_input(timeout=10):
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.record(source, duration=timeout)
                return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("Timeout exceeded. Stopping listening.")
            speak("Time over")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you please repeat?")
        except sr.RequestError:
            speak("Sorry, I'm having trouble accessing the speech recognition service. Please try again later.")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle fertilizer recommendation input
def get_fertilizer_input():
    input_values = {}
    input_names = ["Temperature", "Humidity", "Soil Moisture", "Soil Type", "Crop Type", "Nitrogen", "Potassium", "Phosphorus"]
    for name in input_names:
        attempts=0
        speak(f"Please provide the value for {name}")
        while True:
            try:
                value = get_voice_input(5)
                if name in ["Soil Type", "Crop Type"]:
                    input_values[name] = str(value)
                else:
                    input_values[name] = float(value)
                break
            except ValueError:
                attempts+=1
                if attempts>2:
                    speak(f"Please provide the value for {name} as text.")
                    value=input(f"Please provide the value for {name} as text: ")
                    if name in ["Soil Type", "Crop Type"]:
                      input_values[name] = str(value)
                    else:
                      input_values[name] = float(value)
                    break
                speak("Sorry, I didn't understand that. Please provide a numeric value.")
                


        # Display the input value as text on the screen
        print(f"{name}:", input_values[name])
    return input_values

# Function to handle crop recommendation input
def get_crop_recommendation_input():
    input_values = {}
    input_names = ["Nitrogen", "Phosphorus", "Potassium", "Temperature", "Humidity", "pH", "Rainfall"]
    for name in input_names:
        attempts=0
        speak(f"Please provide the value for {name}")
        while True:
            try:
                value = get_voice_input(5)
                input_values[name] = float(value)
                break
            except ValueError:
                attempts+=1
                speak("Sorry, I didn't understand that. Please provide a numeric value.")
                if attempts>2:
                    speak(f"Please provide the value for {name} as text.")
                    value=input(f"Please provide the value for {name} as text: ")
                    input_values[name] = float(value)
                    break

        # Display the input value as text on the screen
        print(f"{name}:", input_values[name])
    return input_values

# Get input from the farmer
# Main function to determine the type of recommendation
def main():
    # Get input from the farmer
    speak("How can I assist you today?")
    
    while True:
        user_input = get_voice_input()
        
        # Display the user's input
        print("User input:", user_input.lower())

        # Check if the user wants a crop recommendation
        crop_keywords = ["recommend crop", "crop recommendation", "what to grow", "suggest crop","crops","which crop","what crop","recommend me a crop","grow here"]
        fertilizer_keywords = ["recommend fertilizer", "fertilizer recommendation", "what fertilizer to use", "suggest fertilizer","recommend a fertilizer"]
        temperature_keywords = ["what is the current temperature","temperature now"]
        humidity_keywords = ["what is the current humidity level","humidity now"]
        weather_keywords = ["what is the weather now","current weather conditions"]
        if user_input.lower() == "exit":
            speak("Goodbye!")
            break
        if any(word in user_input.lower() for word in crop_keywords):
            input_values = get_crop_recommendation_input()

            # Pass the inputs to your crop recommendation model and get the recommendation
            input_list = [input_values[name] for name in input_values.keys()]
            recommended_crop = crop_model.predict([input_list])[0]

            # Convert the recommended crop to speech
            output_text = f"Based on these conditions, I recommend you to grow {recommended_crop}"
            speak(output_text)
            print("Recommended crop:", recommended_crop)
            speak("Do you have any other queries? Say 'exit' to exit.")

        # Check if the user wants a fertilizer recommendation
        elif any(word in user_input.lower() for word in fertilizer_keywords):
            input_values = get_fertilizer_input()

            # Pass the inputs to your fertilizer recommendation model and get the recommendation
            input_list = [input_values[name] for name in input_values.keys()]
            # Call the predict_fertilizer function from fertilizerrecommend.py
            recommended_fertilizer = predict_fertilizer(input_list)

            # Convert the recommended fertilizer to speech
            output_text = f"Based on these conditions, I recommend you to use {recommended_fertilizer} fertilizer"
            speak(output_text)
            print("Recommended fertilizer:", recommended_fertilizer)
            speak("Do you have any other queries? Say 'exit' to exit.")

        else:
            answer = handle_query(user_input)
            if answer:
                speak(answer)
            else:
                speak("Sorry, I don't have an answer for that question.")
            speak("Do you have any other queries? Say 'exit' to exit.")

# Call the main function
if __name__ == "__main__":
    main()

