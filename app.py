import streamlit as st
import joblib

model = joblib.load("SVM_placement.pkl")
scaler = joblib.load("placement_scaler.pkl")


st.set_page_config(page_title="Placement Predictor", layout="centered")

st.title("🎓 Placement Prediction App")
st.write("Enter student details below:")


cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)
internships = st.number_input("Internships", 0, 10, 0)
projects = st.number_input("Projects", 0, 20, 1)
workshops = st.number_input("Workshops/Certifications", 0, 20, 0)

aptitude = st.number_input("Aptitude Test Score", 0, 100, 50)
softskills = st.number_input("Soft Skills Rating", 1, 10, 5)

extracurricular = st.selectbox("Extracurricular Activities", [0, 1])
placement_training = st.selectbox("Placement Training", [0, 1])

ssc = st.number_input("SSC Marks", 0, 100, 70)
hsc = st.number_input("HSC Marks", 0, 100, 70)


if st.button("Predict Placement"):


    academic_score = (cgpa * 10 + ssc + hsc) / 3

    experience_score = (
        internships * 3 +
        projects * 2 +
        workshops
    )

    profile_score = (
        cgpa * 10 +
        internships * 5 +
        projects * 3 +
        workshops * 2 +
        softskills * 5
    )

    training_effectiveness = placement_training * aptitude


    input_data = [
        cgpa,
        internships,
        projects,
        workshops,
        aptitude,
        softskills,
        extracurricular,
        placement_training,
        ssc,
        hsc,
        academic_score,
        experience_score,
        profile_score,
        training_effectiveness
    ]

    scaled_input = scaler.transform([input_data])


    prediction = model.predict(scaled_input)[0]


    if prediction == 1 or prediction == "Placed":
        st.success("✅ Student is Likely PLACED")
    else:
        st.error("❌ Student is Likely NOT PLACED")