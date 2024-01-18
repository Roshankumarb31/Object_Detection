# import streamlit as st

# # Title and description
# st.title('Progress Bar Example')
# st.write('Change the value to see the progress bar update.')

# # User input for progress
# progress_value = st.slider('Select a value:', min_value=0, max_value=100)

# # Display the progress bar
# st.progress(progress_value / 100.0)  # Normalize the value to be between 0 and 1

import streamlit as st

# Title and description
st.title('Dynamic Progress Bar Example')
st.write('Enter a value between 0 and 100 to change the progress level.')

# User input for progress level
progress_text = st.text_input('Enter progress level (0-100):')

try:
    progress_value = int(progress_text)
    if 0 <= progress_value <= 100:
        # Display the progress bar
        st.progress(progress_value / 100.0)  # Normalize the value to be between 0 and 1
    else:
        st.write('Please enter a valid value between 0 and 100.')
except ValueError:
    st.write('Please enter a valid number between 0 and 100.')