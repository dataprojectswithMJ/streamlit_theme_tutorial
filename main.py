import streamlit as st

st.title('Streamlit custom theme tutorial')
st.subheader('Powered by @dataprojectswithMJ')

st.multiselect('Choose your favourite coding language(s)',
               options=['Python','Java','Golang','C++'])

st.radio('Choose your favourite operation system:',
         ['Windows','Linux','MacOS'])

st.date_input('Enter your date of birth')

st.text_area('About you:')