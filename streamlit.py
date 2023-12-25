import streamlit as st
import requests

# Set up the API information
API_URL = "https://api-inference.huggingface.co/models/fajarkrisnajaya/Pemilu2024-BERT-Clickbait"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Function to convert label to "Clickbait" or "non-Clickbait"
def label_to_category(label):
    if label == "LABEL_1":
        return "Clickbait"
    elif label == "LABEL_0":
        return "non-Clickbait"
    else:
        return "Unknown"

def main():
    # Set the title of the web app
    st.title("BERT Clickbait Detection")

    # Text input for user
    user_input = st.text_input("Enter your text here")

    # Button to trigger model inference
    if st.button('Analyze'):
        if user_input:
            # Call the query function
            payload = {"inputs": user_input}
            output = query(payload)

            # Get the label with the highest score
            best_prediction = max(output[0], key=lambda x: x["score"])
            predicted_label = best_prediction["label"]

            # Map the label to "Clickbait" or "non-Clickbait"
            category = label_to_category(predicted_label)
            score = best_prediction["score"]

            # Display the result
            st.write(f"Prediction: {category} (Score: {score})")
        else:
            st.write("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
