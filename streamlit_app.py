import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Giga tłumacz')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

#st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

#st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

#st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

#st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

#st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

#with st.echo():
#    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

#df = pd.read_csv("DSP_4.csv", sep = ';')
#st.dataframe(df)
# musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.subheader('angielski - niemiecki')

st.write('Wybierz opcję tłumaczenia tekstu, a następnie wpisz tekst do przetłumaczenia')

import streamlit as st
from transformers import pipeline
from transformers import FSMTForConditionalGeneration, FSMTTokenizer
import sacremoses
import torch
model_name = "facebook/wmt19-en-de"
tokenizer = FSMTTokenizer.from_pretrained(model_name)
model = FSMTForConditionalGeneration.from_pretrained(model_name)


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
    if text:
        try:
            with st.spinner('Tłumaczenie w toku...'):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(percent_complete + 1)
                inputs = tokenizer.encode(text, return_tensors="pt")
                outputs = model.generate(inputs)
                translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.write(translated_text)
        except Exception as e:
            st.error(f'Error: {e}')



#st.subheader('Zadanie do wykonania')
st.write('s24645')
# st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
# st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
# st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
# st.write('🐞 Na końcu umieść swój numer indeksu')
# st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
# st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
