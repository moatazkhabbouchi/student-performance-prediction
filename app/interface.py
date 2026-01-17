import streamlit as st
import pickle
st.set_page_config(layout="wide")


st.title("Student Performance Prediction")
st.write(
"""
    ### This is a student performance prediction application based on a linear regression model.
"""
)
col1, col2 = st.columns(2, vertical_alignment="bottom", gap="large")
filename = 'performance_model.pkl'
model = pickle.load(open(filename, 'rb'))

with col1:
    st.image('https://images.unsplash.com/photo-1571260899304-425eee4c7efc?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')

with col2:
    hours_studied = st.slider("Number of Hours Studied", 1, 10)
    previous_score = st.number_input("Previous score", min_value=0.0    , max_value=100.0, value=50.0, step=1.0)
    extracurricular_activities	= st.radio('Extracurricular Activities', ['Yes', 'No'])
    sleep_hours =  st.slider("Number of Sleep Hours", 0, 12)
    number_of_sample_papers =  st.slider("Number of Sample Question Paper Practiced", 0, 12)
    extracurricular_activities = 1 if extracurricular_activities == 'Yes' else 0


    input = [[hours_studied, previous_score, extracurricular_activities, sleep_hours, number_of_sample_papers]]

    def predict(input):
        return model.predict(input)

    @st.dialog("🔥 Predict Student Performance")
    def on_predict(pred):
        st.write(f"Predicted Performance Index: {pred[0]:.2f}")
        if st.button("close"):
            st.rerun()

    if st.button("Predict"):
        value = predict(input)
        on_predict(value)
        

