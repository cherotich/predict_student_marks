######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
import joblib
import os

######################
# Page Title
######################



st.write("""
# Student marks prediction Web App
It predicts the percentage score of a student based on the no. of study hours
***
""")
def load_model():
    model = joblib.load('marks_prediction_model.pkl')
    return model
selected_model = load_model()
uploaded_file = st.file_uploader("Select a csv file containing the number of study hours")
if uploaded_file is not None:

    #  # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)
    #  # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    #  # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    number = st.number_input("Number of Rows to view max=10",5,10)
    st.dataframe(df.head(number))
    # st.write(dataframe)

# def file_selector(folder_path='./datasets'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox("Selecte a csv file containing the number of study hours ", filenames)
#     return os.path.join(folder_path,selected_filename)
                
# filename = file_selector()
# st.info("You have selected {}".format(filename))  

#     #Read data
# df = pd.read_csv(filename)

# first 10 rows
# number = st.number_input("Number of Rows to view max=10",5,10)
# st.dataframe(df.head(number))






    st.write(df.shape)
    data_dim = st.radio("Show Dimension By",("Rows","Columns"))
    if data_dim == 'Rows':
        st.text("Number of Rows")
        st.write(df.shape[0])
    if data_dim == 'Columns':
        st.text("Number of Columns")
        st.write(df.shape[1])
    else:
        st.write(df.shape)
                    
    st.write(""" Predicted results """)
    predicted = selected_model.predict(df[['Hours']])
    df['Predicted score value'] = predicted
    st.dataframe(df)


@st.cache
def convert_df(df):
    if uploaded_file  is not None:
        


    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
if uploaded_file  is not None: 
    
    

    csv = convert_df(df)

    st.download_button(
        label="Download predicted values as CSV",
        data = csv,
        file_name='large_df.csv',
        mime='text/csv',
 )

if st.checkbox("Use already existing sample dataset"):
    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select a csv file containing the number of study hours ", filenames)
        return os.path.join(folder_path,selected_filename)
    filename = file_selector()
    st.info("You have selected {}".format(filename))
    df = pd.read_csv(filename)
    number1 = st.number_input("Number of Rows to view maximum is 10",5,10)
    st.dataframe(df.head(number1))
    st.write(df.shape)
    data_dim = st.radio("Show Dimension By",("Rows","Columns"))
    if data_dim == 'Rows':
        st.text("Number of Rows")
        st.write(df.shape[0])
    if data_dim == 'Columns':
        st.text("Number of Columns")
        st.write(df.shape[1])
    else:
        st.write(df.shape)
                    
    st.write(""" Predicted results """)
    predicted = selected_model.predict(df[['Hours']])
    df['Predicted score value'] = predicted
    st.dataframe(df)
    # @st.cache

    # csv1 = df.to_csv().encode('utf-8')

    st.download_button(
            label="Download the predictions as CSV",
            data = df.to_csv().encode('utf-8'),
            file_name='large_df.csv',
            mime='text/csv',
    )
    #     st.info("You have selected ")
    # r = file_selector()
    # st.info(r)

    



# def file_selector(folder_path='./datasets'):

#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox("Select a csv file containing the number of study hours ", filenames)
#     return os.path.join(folder_path,selected_filename)
                    
# filename = file_selector()
# st.info("You have selected {}".format(filename))  

#         #Read data
# df = pd.read_csv(filename)

#     # first 10 rows
# number1 = st.number_input("Number of Rows to view max=10",5,10)
# st.dataframe(df.head(number1))
    
            
            
# number = st.number_input('Enter the number of study hours')
# st.write('The score of the student is ', number)

