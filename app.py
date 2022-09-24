import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
from PIL import Image
from main import *

import database as db


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Mentor Analysis", page_icon=":bar_chart:", layout="wide")

# --- DEMO PURPOSE ONLY --- #
placeholder = st.empty()
placeholder.info("INFO | username: root ; password: ********")
# ------------------------- #

# --- USER AUTHENTICATION ---
users = db.fetch_all_users()

usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    placeholder.empty()

    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    page = st.sidebar.selectbox("Choose a page",
                                ["All mentors", "Data Science", 'Full Stack', 'Software Engineer'])
    if page == 'All mentors':
        all_bar_all()
        img = Image.open('image/all_plots.png')
        new_image = img.resize((12000, 5000))
        st.image(new_image, caption='Barcha mentorlar analitikasi')
        # REPORT DATE
        d_start = st.date_input(
            " Select the beginning of the reporting period", datetime.date(2022, 1, 1))

        d_finish = st.date_input(
            "Select the end of the reporting period")
            #datetime.date(2019, 7, 6))
        left = datetime.datetime(d_start.year, d_start.month, d_start.day)
        right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
        all_bar_all(left=left, right=right)
        img = Image.open('image/all_plots.png')
        new_image = img.resize((12000, 5000))
        st.image(new_image, caption='Barcha mentorlar analitikasi')




    # DATA SCIENCE
    elif page == 'Data Science':
        options_es = st.sidebar.checkbox('Umumiy analitika', )
        options_com = st.sidebar.checkbox('Aniq analitika')
        options_date = st.sidebar.checkbox('Vaqt boycha analitika')
        mentors_ds = st.sidebar.radio('Choose a mentor',
                              ['Arslanova Nodira', 'Alimbayeva Asalbonu', "Orifjonov Abdulaziz"])
        st.title("Data Exploration")

        if mentors_ds == 'Arslanova Nodira':
            st.markdown('Arslanova Nodira')
            if options_es:
                pie('Arslanova Nodira')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Arslanova Nodira')
            if options_com:
                koment_bar('Arslanova Nodira')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Arslanova Nodira')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Arslanova Nodira',left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Arslanova Nodira')

                koment_bar('Arslanova Nodira',left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Arslanova Nodira')


        elif mentors_ds == 'Alimbayeva Asalbonu':
            st.markdown('Alimbayeva Asalbonu')
            if options_es:
                pie('Alimbayeva Asalbonu')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Alimbayeva Asalbonu')
            if options_com:
                koment_bar('Alimbayeva Asalbonu')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Alimbayeva Asalbonu')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Alimbayeva Asalbonu', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Alimbayeva Asalbonu')

                koment_bar('Alimbayeva Asalbonu', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Alimbayeva Asalbonu')

        elif mentors_ds == 'Orifjonov Abdulaziz':
            st.markdown('Orifjonov Abdulaziz')
            if options_es:
                pie('Orifjonov Abdulaziz')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Orifjonov Abdulaziz')
            if options_com:
                koment_bar('Orifjonov Abdulaziz')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Orifjonov Abdulaziz')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Orifjonov Abdulaziz', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Orifjonov Abdulaziz')

                koment_bar('Orifjonov Abdulaziz', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Orifjonov Abdulaziz')

    elif page == 'Full Stack':
        options_es = st.sidebar.checkbox('Umumiy analitika', )
        options_com = st.sidebar.checkbox('Aniq analitika')
        options_date = st.sidebar.checkbox('Vaqt boycha analitika')
        mentors_ds = st.sidebar.radio('Choose a mentor',
                              ["Rasulov Rahmatulloh", "Shomurodov Sarvarbek", "Shukurov Jasur", "Azizova Aziza"])
        st.title("Data Exploration")

        if mentors_ds == 'Rasulov Rahmatulloh':
            st.markdown('Rasulov Rahmatulloh')
            if options_es:
                pie('Rasulov Rahmatulloh')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Rasulov Rahmatulloh')
            if options_com:
                koment_bar('Rasulov Rahmatulloh')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Rasulov Rahmatulloh')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Rasulov Rahmatulloh', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Rasulov Rahmatulloh')

                koment_bar('Rasulov Rahmatulloh', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Rasulov Rahmatulloh')

        elif mentors_ds == 'Shomurodov Sarvarbek':
            st.markdown('Shomurodov Sarvarbek')
            if options_es:
                pie('Shomurodov Sarvarbek')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Shomurodov Sarvarbek')
            if options_com:
                koment_bar('Shomurodov Sarvarbek')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Shomurodov Sarvarbek')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Shomurodov Sarvarbek', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Shomurodov Sarvarbek')

                koment_bar('Shomurodov Sarvarbek', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Shomurodov Sarvarbek')

        elif mentors_ds == 'Shukurov Jasur':
            st.markdown('Shukurov Jasur')
            if options_es:
                pie('Shukurov Jasur')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Shukurov Jasur')
            if options_com:
                koment_bar('Shukurov Jasur')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Shukurov Jasur')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Shukurov Jasur', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Shukurov Jasur')

                koment_bar('Shukurov Jasur', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Shukurov Jasur')

        elif mentors_ds == 'Azizova Aziza':
            st.markdown('Azizova Aziza')
            if options_es:
                pie('Azizova Aziza')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Shukurov Jasur')
            if options_com:
                koment_bar('Azizova Aziza')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Azizova Aziza')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Azizova Aziza', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Azizova Aziza')

                koment_bar('Azizova Aziza', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Azizova Aziza')


    elif page == 'Software Engineer':
        options_es = st.sidebar.checkbox('Umumiy analitika', )
        options_com = st.sidebar.checkbox('Aniq analitika')
        options_date = st.sidebar.checkbox('Vaqt boycha analitika')
        mentors_ds = st.sidebar.radio('Choose a mentor',
                              ['Azodov Sarvar', 'Olloyorov Sirojiddin'])
        st.title("Data Exploration")

        if mentors_ds == 'Azodov Sarvar':
            st.markdown('Azodov Sarvar')
            if options_es:
                pie('Azodov Sarvar')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Azodov Sarvar')
            if options_com:
                koment_bar('Azodov Sarvar')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Azodov Sarvar')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Azodov Sarvar', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Azodov Sarvar')

                koment_bar('Azodov Sarvar', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Azodov Sarvar')

        elif mentors_ds == 'Olloyorov Sirojiddin':
            st.markdown('Olloyorov Sirojiddin')
            if options_es:
                pie('Olloyorov Sirojiddin')
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Olloyorov Sirojiddin')
            if options_com:
                koment_bar('Olloyorov Sirojiddin')
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Olloyorov Sirojiddin')
            if options_date:
                d_start = st.date_input(
                    " Select the beginning of the reporting period", datetime.date(2022, 1, 1))
                # datetime.date(2019, 7, 6))
                d_finish = st.date_input(
                    "Select the end of the reporting period")

                left = datetime.datetime(d_start.year, d_start.month, d_start.day)
                right = datetime.datetime(d_finish.year, d_finish.month, d_finish.day)
                pie('Olloyorov Sirojiddin', left=left, right=right)
                img = Image.open('image/mentor_pie_plot.png')
                st.image(img, caption='Olloyorov Sirojiddin')

                koment_bar('Olloyorov Sirojiddin', left=left, right=right)
                img = Image.open('image/mentor_barh_plot.png')
                st.image(img, caption='Olloyorov Sirojiddin')
