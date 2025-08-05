import pandas as pd
import streamlit as st
st.markdown("""
    <meta name="google-site-verification" content="eh014-cE05gLeX9mKDZUJryq4FIElEvAZBYnA6NEzR0" />
""", unsafe_allow_html=True)

#st.text("google-site-verification: eh014-cE05gLeX9mKDZUJryq4FIElEvAZBYnA6NEzR0")
# Read Excel file
# IMPORTANT: It's better to use a relative path. Place the Excel file in the same folder as the script.
try:
    colleges = pd.read_excel('Final_College_list.xlsx', header=None)
except FileNotFoundError:
    st.error("Error: 'Final_College_list.xlsx' not found. Please make sure the Excel file is in the same directory as this script.")
    st.stop() # Stop the app if the file is not found

colleges.columns = ['COLLEGE RANK', 'CODE', 'COLLEGE NAME', 'TYPE', 'REGION', 'DISTRICT', 'PLACE',
                    'COED', 'AFFILIATED TO', 'ESTABLISHED YEAR', 'STUDENT REGION', 'BRANCH',
                    'OC BOYS', 'OC GIRLS', 'SC BOYS', 'SC GIRLS', 'ST BOYS', 'ST GIRLS',
                    'BC-A BOYS', 'BC-A GIRLS', 'BC-B BOYS', 'BC-B GIRLS', 'BC-C BOYS', 'BC-C GIRLS',
                    'BC-D BOYS', 'BC-D GIRLS', 'BC-E BOYS', 'BC-E GIRLS', 'OC(EWS) BOYS', 'OC(EWS) GIRLS',
                    'COLLEGE FEE']

# Fill missing values
colleges = colleges.ffill()

# Streamlit UI
st.set_page_config(page_title="College Predictor", page_icon="🎓", layout="wide")

# --- Custom CSS for Colours and Styles ---
st.markdown("""
<style>
/* Main title style with gradient background */
.big-font {
    font-size: 48px !important;
    font-weight: bold;
    color: white;
    background-image: linear-gradient(to right, #4CAF50, #2196F3); /* Green to Blue Gradient */
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 20px;
}

/* Custom subheader style */
.subheader-font {
    font-size: 28px !important;
    font-weight: bold;
    color: #1A5276; /* Dark Blue */
}

/* Custom style for the note box */
.note-box {
    background-color: #EBF5FB; /* Light blue background */
    border-left: 6px solid #2196F3; /* Blue left border */
    padding: 15px;
    border-radius: 5px;
    margin-top: 20px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)


# Use markdown for the styled title
st.markdown('<p class="big-font">🎓 2025 EAPCET College Predictor Tool</p>', unsafe_allow_html=True)

st.info("""
**Welcome!** This app helps students predict which colleges they may be eligible for based on their rank and preferences.
Use the sidebar to **view eligible colleges** (this page) or **learn about different engineering branches**.
""")

st.markdown('<p class="subheader-font">📝 Student Details (Mandatory)</p>', unsafe_allow_html=True)

# Using columns for a cleaner layout
col1, col2, col3, col4 = st.columns(4)
with col1:
    rank = st.number_input("Enter your rank:", min_value=1, max_value=200000)
with col2:
    casteGender = st.selectbox('Choose your Category:', ['--Select--','OC BOYS','OC GIRLS','SC BOYS','SC GIRLS','ST BOYS','ST GIRLS', 'BC-A BOYS', 'BC-A GIRLS','BC-B BOYS', 'BC-B GIRLS','BC-C BOYS', 'BC-C GIRLS', 'BC-D BOYS', 'BC-D GIRLS','BC-E BOYS', 'BC-E GIRLS','OC(EWS) BOYS', 'OC(EWS) GIRLS'])
with col3:
    region = st.selectbox("Your Region:", ["--Select--", "AU", "SVU"])
with col4:
    branch = st.selectbox("Preferred Branch:", ['--Select--','AGR','CAI','CIV','CSD','CSE','ECE','EEE','MEC','MIN','AID','CSM','INF','AIM','PET','CIC','CIT','CS','DS','CHE','CSC','CSO','EIE','CAD','CBA','ECA','EVT','BIO','GIN','IST','MET','NAM','PHM','AI','CN','CSBS','CSW','EBM','EII','MAU','MII','MMM','FDT','BDT','AUT','CSG','IOT','MRB','FDE','PEE','ASE','CSS','CST','CSER','CSB','ECT','CCC','CIA','CSEB','RBT','CBC','CDA','ECES','ECV','MAD','SWE','ECM','MMT','GDT'])

st.markdown('<p class="subheader-font">🏛️ College Preferences (Optional)</p>', unsafe_allow_html=True)

# Using columns for optional preferences
col5, col6, col7, col8 = st.columns(4)
with col5:
    district = st.selectbox("District:", ['PKS','EG','CTR','SKL','NLR','KDP','KRI','ATP','GTR','VSP','VZM','KNL','WG'], index=None, placeholder="Any District")
with col6:
    col_region = st.selectbox("College Region:", ["SVU", "AU","SW"], index=None, placeholder="Any Region")
with col7:
    col_type = st.selectbox("College Type:", ['PVT','PU','SF','UNIV','SS'], index=None, placeholder="Any Type")
with col8:
    edu_type = st.selectbox("Education Type:", ["COED", "GIRLS"], index=None, placeholder="Any Campus")


show = st.radio("Show Colleges", ["Top 20", "All"], horizontal=True)

# Button to trigger prediction
if st.button("🚀 Find Eligible Colleges"):
    if casteGender == "--Select--" or region == "--Select--" or branch == "--Select--":
        st.error("Please enter all the mandatory details (Rank, Category, Region, and Branch).")
    else:
        # Filtering based on mandatory inputs
        x = colleges[
            (colleges[casteGender] >= rank) &
            (colleges["BRANCH"] == branch) &
            (colleges["STUDENT REGION"] == region)
        ]

        # Applying optional filters
        if district:
            x = x[x["DISTRICT"] == district]
        if col_region:
            x = x[x["REGION"] == col_region]
        if col_type:
            x = x[x["TYPE"] == col_type]
        if edu_type:
            x = x[x["COED"] == edu_type]

        display_columns = ['CODE', 'COLLEGE NAME', 'TYPE', 'REGION', 'DISTRICT', 'PLACE', 'COED',
                           'AFFILIATED TO', 'ESTABLISHED YEAR', 'STUDENT REGION', 'BRANCH', 'COLLEGE FEE']
        x = x.sort_values(by="COLLEGE RANK", ascending=True)

        if not x.empty:
            if show == "Top 20":
                top_20 = x[display_columns].head(20).reset_index(drop=True)
                top_20.index += 1
                st.success(f"Here are the top {len(top_20)} eligible colleges based on your criteria:")
                st.dataframe(top_20, use_container_width=True)
            else:
                all_choices = x[display_columns].reset_index(drop=True)
                all_choices.index += 1
                st.success("Here are all the eligible colleges based on your criteria:")
                st.dataframe(all_choices, use_container_width=True)
        else:
            st.warning("We are sorry, no eligible colleges were found for the given criteria. Try removing some optional preferences.")

        # Using the custom styled note box for the disclaimer
        st.markdown("""
        <div class="note-box">
            <strong>Dear student, please note:</strong><br>
            The results displayed above are based on previous years' cutoff data. The ranking of colleges is provided based on college placements and other public sources. Neither the owner nor the website takes responsibility for any grievances. We strongly advise you to personally verify the details of each college before adding it to your web options list.
            <br><strong>Thank you.</strong>
        </div>
        """, unsafe_allow_html=True)
