import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
# import

# Load Zephyr model and tokenizer
model_name = "stabilityai/stablelm-zephyr-3b"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Streamlit UI
st.title("Zephyr Chatbot")

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Tokenize user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt")

    # Generate response from the model
    with st.spinner("Generating response..."):
        bot_output = model.generate(input_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2)

    # Decode and display the model's response
    bot_response = tokenizer.decode(bot_output[0], skip_special_tokens=True)
    st.text_area("Zephyr:", bot_response, height=100)

# Note: Adjust the generation parameters as needed based on your requirements
