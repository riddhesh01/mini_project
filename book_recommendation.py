import pandas as pd
import sklearn
import numpy as np
import pickle
import streamlit as st
import re

book_dict = pickle.load(open('book_title_list.pkl', 'rb'))

book = pd.DataFrame(book_dict)

book_ten = book['title'].head(50000)

st.header('Books Recommender System')
liked_b = st.multiselect('What is your favorite books', book_ten)
liked_books = []


if st.button('Recommend'):
    st.write(liked_b)
