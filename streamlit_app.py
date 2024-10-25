import streamlit as st
import time

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

st.image("arnold.jpg")
st.title('Giga tłumacz')
st.write('')
st.write('')
st.write('')

st.subheader('angielski - niemiecki')
st.write('Wybierz opcję tłumaczenia tekstu, a następnie wpisz tekst do przetłumaczenia')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Tłumaczenie tekstu",
        "Wydźwięk emocjonalny tekstu (eng)",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
if option == "Tłumaczenie tekstu":
    text = st.text_area(label="Wpisz tekst")
    if st.button('Przetłumacz'):
        if text:
            translator = pipeline("translation_en_to_de")
            try:
                with st.spinner('Tłumaczenie w toku...'):
                    progress_bar = st.progress(0)
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(percent_complete + 1)
                answer = translator(text).pop().get('translation_text')
                st.write('')
                st.markdown(f'### {answer}')
                st.markdown('🏋️‍♂️')
            except Exception as e:
                st.error(f'Error: {e}')


st.write('')
st.write('')
st.write('')
st.write('')
st.write('s24645')

