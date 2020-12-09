import streamlit as st
import gpt_2_simple as gpt2
from PIL import Image
import copy


# cache = {}

# @st.cache
def loader():
    # if 'sess' not in cache:
    #     cache['sess'] = gpt2.start_tf_sess()
    #     gpt2.load_gpt2(cache['sess'], checkpoint_dir='./gpt_2/checkpoint', run_name='run1')
    # return cache['sess']
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, checkpoint_dir='../assets/gpt_2/checkpoint', run_name='run1')
    return sess

# cloned = copy.deepcopy(loader())

def to_markdown(text):
    text = text.replace('\n', ' <br> ')
    return text

def main():

    st.title('Seinfeld Script Generator')
    st.markdown('by _Cloudy Liu_')
    image = Image.open('../img/gpt2_app.jpg')
    st.image(image, use_column_width=True)

    # set sidebar variables
    title = st.sidebar.text_input('Who to start', '')
    length = st.sidebar.slider('How Long', 50, 1000, 200, 50)
    temperature = st.sidebar.slider("how creative", 0.1, 2.0, 0.9, 0.1)
    gen_button = st.sidebar.button('Generate!')

    if gen_button:
        st.markdown('**Generating Script...**')

        if title:
            # sess = gpt2.start_tf_sess()
            # gpt2.load_gpt2(sess, checkpoint_dir='./gpt_2/checkpoint', run_name='run1')
            sess = loader()
            text = gpt2.generate(sess, checkpoint_dir='../assets/gpt_2/checkpoint', length=length, temperature=temperature, prefix=title.upper(), nsamples=1, batch_size=1, return_as_list=True)[0]
        else: 
            # sess = gpt2.start_tf_sess()
            # gpt2.load_gpt2(sess, checkpoint_dir='./gpt_2/checkpoint', run_name='run1')
            sess = loader()
            text = gpt2.generate(sess, checkpoint_dir='../assets/gpt_2/checkpoint', length=length,  temperature=temperature, nsamples=1, batch_size=1, return_as_list=True)[0]
        
        st.markdown(to_markdown(text), unsafe_allow_html=True)

    option = st.sidebar.selectbox('See some past examples?', ('Jerry', 'Elaine', 'George', 'Kramer', 'Fun'))
    go = st.sidebar.button('Go!')

    if go:
        path = '../generated_texts/best_'+option.lower()+'.txt'
        generated = open(path, 'r').read()
        st.markdown(to_markdown(generated), unsafe_allow_html=True)
        st.text_area('', to_markdown(generated))

main()