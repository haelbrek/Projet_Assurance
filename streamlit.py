import streamlit as st
import pickle
import pandas as pd
st.title("_:red[Assur']aimant_")

sex = st.radio(
    "Quel est votre genre?",
    ('Femme', 'Homme'))

if sex == 'Femme':
    sex = 'female'
else:
    sex = 'male'




children = st.selectbox(
    "Combien d'enfants avez-vous?",
    ('0',"1","2","3","4","5"))

st.write('Vous avez ', children, 'enfant(s)')

age = st.slider('How old are you?', 18,120)
st.write("I'm ", age, 'years old')

poids = st.number_input('Quel est votre est poids?')
st.write('Vous pesez  ', poids, 'Kgs')

taille = st.number_input('Quel est votre est taille ?')
st.write('Vous mesurez  ', taille, "m")


if taille != 0: 
    bmi = poids / ((taille)*(taille))
    st.write("Votre bmi est de ", bmi)

smoker = st.radio(
    "Est-ce-que vous fumez?",
    ('Oui', 'Non'))

if smoker== 'Oui':
    smoker = 'yes'
else:
    smoker = 'no'

option = st.selectbox(
    "De quel region venez-vous",
    ('nord-est', 'sud-est', 'sud-ouest', 'nord-ouest'))

pickle_in = open('modelelastic.pkl', 'rb') 
modelelastic =pickle.load(pickle_in)

input_data = {"sex": sex, "children": children, "smoker": smoker, "bmi": bmi, "age": age, }


input_df = pd.DataFrame(input_data, index=[0])

# Remplacer 'bmi' par le nom de votre colonne de BMI et 'df' par le nom de votre DataFrame
bmi = input_df['bmi']

# Définissez les bornes de chaque catégorie de BMI
bins = [0, 18.5, 25, 30, 35, 40, float('inf')]

# Utilisez la fonction 'cut' pour transformer les valeurs de BMI en catégories
bmi_categories = pd.cut(bmi, bins, labels=['Underweight', 'Normal weight', 'Overweight', 'Obese Class I', 'Obese Class II', 'Obese Class III'])

# Ajoutez la colonne de catégories de BMI à votre DataFrame
input_df['bmi'] = bmi_categories

prediction = modelelastic.predict(input_df)
if st.button('Prédire'):
    st.write("Votre prime d'assurance serait de :",prediction[0].round(2))



