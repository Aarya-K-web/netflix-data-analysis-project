import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- Streamlit Page Config ----
st.set_page_config(page_title="Netflix Dashboard", page_icon="🎬", layout="wide")

# ---- Load Data ----
@st.cache_data
def load_data():
    df = pd.read_csv("mymoviedb.csv")   # <-- Your correct dataset name
    return df

df = load_data()

# ---- Sidebar Navigation ----
st.sidebar.title("🎬 Netflix Dashboard")
st.sidebar.write("Interactive analysis of Netflix movies & TV shows.")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Go to section:",
    ["Overview", "Country Analysis", "Genres", "Release Trends"]
)

# ---- Dashboard Pages ----

# 1. Overview
if menu == "Overview":
    st.title("🎬 Netflix Data Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Titles", len(df))
    col2.metric("Movies", df[df["type"] == "Movie"].shape[0])
    col3.metric("TV Shows", df[df["type"] == "TV Show"].shape[0])

    st.subheader("Top 10 Genres")
    top_genres = df["listed_in"].value_counts().head(10)
    st.bar_chart(top_genres)

# 2. Country Analysis
elif menu == "Country Analysis":
    st.title("🌍 Country Distribution")

    country_count = df["country"].value_counts().head(20)
    st.bar_chart(country_count)

# 3. Genre Breakdown
elif menu == "Genres":
    st.title("🎭 Genre Breakdown")

    genre_count = df["listed_in"].value_counts().head(15)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=genre_count.index, x=genre_count.values, ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Genre")
    st.pyplot(fig)

# 4. Release Trends
elif menu == "Release Trends":
    st.title("📅 Release Year Trends")

    release_years = df["release_year"].value_counts().sort_index()
    st.line_chart(release_years)

# ---- Footer ----
st.markdown(
    """
    <br><hr>
    <p style='text-align:center; font-size:13px; color:gray;'>
        Built by <b>Arya Kshirsagar</b> — Netflix Analysis Dashboard (AIML)
    </p>
    """,
    unsafe_allow_html=True
)

