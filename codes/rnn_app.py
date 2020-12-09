import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.preprocessing import text
from tensorflow.keras.preprocessing.sequence import pad_sequences
from PIL import Image
import json

@st.cache(allow_output_mutation=True)
def loader():
    model = load_model('../assets/lstm1/rnn')

    with open('../assets/lstm1/rnn_tokenizer.json') as f:
        data = json.load(f)
        tokenizer = text.tokenizer_from_json(data)
    return model, tokenizer

def main():
    st.title('Seinfeld Script Generator')
    st.markdown('by _Cloudy Liu_')
    image = Image.open('../img/rnn_app.jpg')
    st.image(image, use_column_width=True)

main()


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)   # fine tune preds, included temperature

def to_markdown(text):
    text = text.replace('\n', ' <br> ')
    return text

def uppercase_char(generated):
    formatted = ''
    lines = generated.split('\n')
    for line in lines:
        char_line = line.split(':')
        if len(char_line) == 2:
            formatted_line = char_line[0].upper()+': '+char_line[1].strip().capitalize()+'\n'
            formatted_line = char_line[0].upper()+': '+char_line[1].strip().capitalize()+'\n'
        else:
            formatted_line = char_line[0].capitalize()+'\n'
        formatted += formatted_line
    return formatted

def generate_text(seed_text, next_words, model, max_len, temperature):
    
    generated = ''
    if seed_text:
        generated += seed_text.lower() + ' :'
    else:
        characters = ['JERRY', 'GEORGE', 'ELAINE', 'KRAMER', 'NEWMAN', 'MORTY', 'HELEN',
       'FRANK', 'SUSAN', 'ESTELLE', 'PETERMAN', 'WOMAN', 'PUDDY', 'MAN',
       'JACK', 'UNCLE LEO', 'MICKEY', 'STEINBRENNER', 'DOCTOR', 'CLERK']
        seed_text = np.random.choice(characters)
        generated += seed_text.lower() + ' :'
    
    for i in range(next_words):
        token_list = tokenizer.texts_to_sequences([generated])[0]
        token_list = pad_sequences([token_list], maxlen=max_len)
        predicted = model.predict(token_list, verbose=0)[0]

        next_index = sample(predicted, temperature)
        next_word = tokenizer.index_word[next_index]

        generated += " " + next_word

    # format the generated texts
    generated = generated.replace('<newline>', '\n')

    punc1 = ['.', ':', '!', ';', ')', ']', '?', ',', '%']
    for i in punc1:
        generated = generated.replace(' '+i, i)
    punc2 = ['[', '(', '$']    
    for i in punc2:
        generated = generated.replace(i+' ', i)
    punc3 = ["'", '-']    
    for i in punc3:
        generated = generated.replace(' '+i+' ', i)
    
    generated = uppercase_char(generated)
    
    return generated

title = st.sidebar.text_input('Who to start', '')
length = st.sidebar.slider('How Long', 50, 1000, 200, 50)
temperature = st.sidebar.slider("how creative", 0.1, 2.0, 0.9, 0.1)
gen_button = st.sidebar.button('Generate!')

if gen_button:
    st.write('Generating Script...')
    model, tokenizer = loader()
    text = generate_text(title, length, model, 60, temperature)
    st.markdown(to_markdown(text), unsafe_allow_html=True)