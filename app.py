# app.py

import streamlit as st
import pandas as pd
from analysis import preprocessing, performance_analysis, visualizations

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📊 Student Performance Analysis App")

uploaded_file = st.file_uploader("📂 Upload Student Result CSV", type=["csv"])

if uploaded_file:
    df, subjects = preprocessing.load_and_clean_data(uploaded_file)
    
    st.success("✅ Data successfully loaded and preprocessed.")
    
    with st.expander("📈 View Raw Data"):
        st.dataframe(df)

    # Overall Statistics
    st.subheader("🔍 Subject-wise Statistics")
    stats = performance_analysis.calculate_overall_statistics(df, subjects)
    st.json(stats)

    # Visualization: Average Marks
    st.subheader("📊 Average Marks per Subject")
    visualizations.plot_average_marks(df, subjects)

    # Visualization: Heatmap
    st.subheader("🔥 Subject-wise Heatmap")
    visualizations.plot_heatmap(df, subjects)

    # Individual Student View
    st.subheader("👤 Individual Student Performance")
    usn = st.text_input("Enter USN:")
    if usn:
        visualizations.plot_individual_student(df, subjects, usn)

    # SGPA Calculation
    st.subheader("🎓 SGPA Calculation")
    df['SGPA'] = performance_analysis.calculate_sgpa(df, subjects)
    st.dataframe(df[['USN', 'Name', 'SGPA']].sort_values(by='SGPA', ascending=False))
