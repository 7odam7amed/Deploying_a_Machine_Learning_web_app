import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Multi_Disease_Prediction")

# loading the saved models

diabetes_model = pickle.load(open('diabetes.sav', 'rb'))

heart_model = pickle.load(open('heart.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons.sav', 'rb'))



# sidebar for negative

with st.sidebar:

    selected = option_menu('Multiple Diseases Prection System',
                           
                           ['Diabetes Prediction',
                            'Heart Diseases Prediction',
                            'Parkinsons Prediction'],

                            icons=['bandaid','clipboard2-pulse', 'person-walking'],
                            
                            default_index = 0)
    


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        SkinThickness = st.text_input("Skin Thickness value")
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")

    with col2:
        Glucose = st.text_input("Glucose Level")
        Insulin = st.text_input("Insulin Level")
        Age = st.text_input("Age of Person")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
        BMI =  st.text_input("BMI Value")

    dia_diagnosis = ''

    # create button for prediction
    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    
        user_input = [float(x) for x in user_input]
        
        dia_pred = diabetes_model.predict([user_input])
        
        if (dia_pred[0] == 0):
            dia_diagnosis = 'The person is not diabetic'
        else:
            dia_diagnosis = 'The person is diabetic'
        
    st.success(dia_diagnosis)




# Heart Prediction Page
if (selected == 'Heart Diseases Prediction'):

    # page title
    st.title('Heart Diseases Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic results')
        oldpeak = st.text_input('ST depression induced by exercise')
        thal = st.text_input('thal\n\n'
                             '(0 = normal, 1 = fixed, 2 = reversable)')


    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        slope = st.text_input('Slope of the peak exercise ST segment')


    with col3:
        cp = st.text_input('Chest Pain types')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        exang = st.text_input('Exercise Induced Angina')
        ca = st.text_input('Major vessels colored by flourosopy')


    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)




# Parkinsons Prediction
if (selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Prediction')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        RAP = st.text_input('MDVP: RAP')
        APQ3 = st.text_input('Shimmer: APQ3')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')


    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        PPQ = st.text_input('MDVP: PPQ')
        APQ5 = st.text_input('Shimmer: APQ5')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')


    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        DDP = st.text_input('Jitter: DDP')
        APQ = st.text_input('MDVP: APQ')
        DFA = st.text_input('DFA')


    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        Shimmer = st.text_input('MDVP: Shimmer')
        DDA = st.text_input('Shimmer: DDA')
        spread1 = st.text_input('spread1')


    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')


    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)