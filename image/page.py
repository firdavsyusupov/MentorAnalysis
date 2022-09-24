import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from PIL import Image
from main import *


page = st.sidebar.selectbox('Choose a page', ["All mentors", "Data Science", 'Full Stack', 'Software Engineer'])

if page == 'All mentors':
    # st.markdown('Barcha mentorlar analitikasi')
    # st.pyplot(all_bar_all())
    # plt.close()
    img = Image.open('image/all_plots.png')
    new_image = img.resize((12000, 5000))
    st.image(new_image, caption='Barcha mentorlar analitikasi')

# page = st.sidebar.selectbox("Choose a page",
#                             ["All mentors", "Data Science", 'Full Stack', 'Software Engineer'])
# if page == "All mentors":
#     # st.markdown('Barcha mentorlar analitikasi')
#     # st.pyplot(all_bar_all())
#     # plt.close()
#     img = Image.open('image/all_plots.png')
#     new_image = img.resize((12000, 5000))
#     st.image(new_image, caption='Barcha mentorlar analitikasi')
#
elif page == "Data Science":
    options_es = st.sidebar.checkbox('Umumiy analitika', )
    options_com = st.sidebar.checkbox('Aniq analitika')
    mentors_ds = st.sidebar.radio('Choose a mentor',
                                  ['Arslanova Nodira', 'Alimbayeva Asalbonu', "Orifjonov Abdulaziz"])

    st.title("Data Exploration")
    if mentors_ds == 'Arslanova Nodira':
        st.markdown('Arslanova Nodira')
        if options_es:
            # st.markdown('Umumiy analitika')
            # st.pyplot(pie('Arslanova Nodira'))
            # plt.close()
            pie('Arslanova Nodira')
            img = Image.open('image/mentor_pie_plot.png')
            st.image(img, caption='Arslanova Nodira')
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Arslanova Nodira'))
            plt.close()
    elif mentors_ds == 'Alimbayeva Asalbonu':
        st.markdown('Alimbayeva Asalbonu')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Alimbayeva Asalbonu'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Alimbayeva Asalbonu'))
            plt.close()
    elif mentors_ds == 'Orifjonov Abdulaziz':
        st.markdown('Orifjonov Abdulaziz')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Orifjonov Abdulaziz'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Orifjonov Abdulaziz'))
            plt.close()

elif page == "Full Stack":
    mentors_fs = st.sidebar.radio('Choose a mentor',
                                  ["Rasulov Rahmatulloh", "Shomurodov Sarvarbek", "Shukurov Jasur",
                                   "Azizova Aziza"])
    options_es = st.sidebar.checkbox('Umumiy analitika', )
    options_com = st.sidebar.checkbox('Aniq analitika')
    st.title("Data Exploration")
    if mentors_fs == 'Azizova Aziza':
        st.markdown('Azizova Aziza')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Azizova Aziza'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Azizova Aziza'))
            plt.close()
    elif mentors_fs == 'Rasulov Rahmatulloh':
        st.markdown('Rasulov Rahmatulloh')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Rasulov Rahmatulloh'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Rasulov Rahmatulloh'))
            plt.close()
    elif mentors_fs == 'Shomurodov Sarvarbek':
        st.markdown('Shomurodov Sarvarbek')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Shomurodov Sarvarbek'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Shomurodov Sarvarbek'))
            plt.close()
    elif mentors_fs == 'Shukurov Jasur':
        st.markdown('Shukurov Jasur')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Shukurov Jasur'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Shukurov Jasur'))
            plt.close()

elif page == "Software Engineer":
    options_es = st.sidebar.checkbox('Umumiy analitika', )
    options_com = st.sidebar.checkbox('Aniq analitika')
    mentors_fs = st.sidebar.radio('Choose a mentor', ["Azodov Sarvar", "Olloyorov Sirojiddin"])
    st.title("Data Exploration")
    if mentors_fs == "Azodov Sarvar":
        st.markdown('Azodov Sarvar')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Azodov Sarvar'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Azodov Sarvar'))
            plt.close()
    elif mentors_fs == '"Olloyorov Sirojiddin"':
        st.markdown('Olloyorov Sirojiddin')
        if options_es:
            st.markdown('Umumiy analitika')
            st.pyplot(pie('Olloyorov Sirojiddin'))
            plt.close()
        if options_com:
            st.markdown('Aniq korsatilgan analitika')
            st.pyplot(koment_bar('Olloyorov Sirojiddin'))
            plt.close()