import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# ------------------ Load Data ------------------
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")  # rename if needed
    return df

df = load_data()

# ------------------ Sidebar ------------------
st.sidebar.title("🎬 Netflix Dashboard")
st.sidebar.write("Interactive analysis of Netflix movies & TV shows.")

menu = st.sidebar.radio("Go to:", ["Overview", "Country Analysis", "Genres", "Release Trends"])

# ------------------ Dashboard Pages ------------------

# Overview
if menu == "Overview":
    st.title("🎬 Netflix Data Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Titles", len(df))
    col2.metric("Movies", df[df["type"]=="Movie"].shape[0])
    col3.metric("TV Shows", df[df["type"]=="TV Show"].shape[0])

    st.subheader("Top 10 Genres")
    top_genres = df["listed_in"].value_counts().head(10)
    st.bar_chart(top_genres)

# Country Page
elif menu == "Country Analysis":
    st.title("🌍 Country Distribution")

    country_counts = df["country"].value_counts().head(20)
    st.bar_chart(country_counts)

# Genres Page
elif menu == "Genres":
    st.title("🎭 Genre Breakdown")

    genre_counts = df["listed_in"].value_counts().head(15)
    plt.figure(figsize=(10,6))
    sns.barplot(y=genre_counts.index, x=genre_counts.values)
    st.pyplot(plt)

# Release Trends
elif menu == "Release Trends":
    st.title("📅 Release Year Trends")

    df_year = df["release_year"].value_counts().sort_index()
    st.line_chart(df_year)

# Footer
st.markdown("<hr><center>Made by <b>Arya Kshirsagar</b> — Netflix Analysis Dashboard</center>", 
            unsafe_allow_html=True)
