import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open("G:\ML Project\Loan Prediction\myproject\loan\Scripts\loan1.pkl",'rb'))

def run():
    img1= Image.open('bank.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Bank Loan Prediction using Machine Learning")

    #account no
    account_no = st.text_input("Account Number")

    #full name
    fn = st.text_input("Full Name")

    #gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    #maritial status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    #number of dependants
    dep_display = ('No', 'One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependants", dep_options, format_func=lambda x: dep_display[x])

    #for edu
    edu_display = ('Graduate', 'Not Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

    # employment status
    emp_display = ('Job', 'Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

    #property status
    prop_display = ('Rural', 'Urban','Semi-Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

    #credit score
    cred_display = ('Between 300 to 500', 'Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

    #applicant monthly income
    mon_income = st.number_input("Applicant Monthly Income",value=0)

    #co applicant monthly income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income",value=0)

    #loan amount
    loan_amt = st.number_input("Loan Amount",value=0)

    #loan duration
    dur_display = ['2 Month','6 Month','8 Month','1Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    if st.button("submit"):
        duration=0
        if dur ==0:
            duration=60
        if dur ==1:
            duration = 180
        if dur==2:
            duratiom=240
        if dur==3:
            duration=360
        if dur ==4:
            duration=480

        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)

        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans ==0:
            st.error(
                "Hello: "+ fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you will not get the loan from Bank'

            )

        else:
            st.success(
                "Hello: " + fn + " || "
                "Account number: " + account_no + ' || '
                'Congratulations!! you will get the loan from Bank'

            )


run()




