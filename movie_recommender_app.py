import streamlit as st
import pandas as pd
import pickle

# ---------------- Load Preprocessed Files ----------------
with open('subset.pkl', 'rb') as f:
    subset = pickle.load(f)

with open('cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

with open('indices.pkl', 'rb') as f:
    indices = pickle.load(f)

# ---------------- Utility Functions ----------------
def recommend(title, cosine_sim=cosine_sim, df=subset, indices=indices, top_n=10):
    if title not in indices.index:
        return pd.DataFrame([{'title': f"'{title}' not found in the dataset."}])
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx].flatten()))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores if i[0] < len(df)]
    return df[['title', 'genres','user_avg_rating']].iloc[movie_indices]

def search_by_column(term, column, df=subset, top_n=10):
    term = term.lower()
    result = df[df[column].apply(lambda items: any(term == item.lower() for item in items))]
    if result.empty:
        return pd.DataFrame([{'title': f"No match for '{term}'"}])
    return result[['title', 'genres','crew', 'cast', 'user_avg_rating']].head(top_n)

def search_by_keyword(term, df=subset, top_n=10):
    term = term.lower()
    result = df[df['movie_profile'].str.lower().str.contains(term) | df['title'].str.lower().str.contains(term)]
    if result.empty:
        return pd.DataFrame([{'title': f"No match for '{term}'"}])
    return result[['title', 'genres','user_avg_rating']].head(top_n)

# ---------------- Streamlit App Layout ----------------
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommendation System")

st.markdown("""
Welcome to the Movie Recommendation App! 
This app suggests movies based on different input methods such as a movie title, actor name, director, or keywords/genres.
Select how you'd like to search, type your input, and get instant recommendations with average ratings.
""")

st.header("Choose a method to recommend movies")

# ---------------- User Options ----------------
option = st.radio("Select method:", ["By Movie Title", "By Keyword or Genre", "By Director", "By Actor"])

query = st.text_input(f"Enter the {option.split()[-1].lower()}:")

if st.button("Search"):
    if option == "By Movie Title":
        results = recommend(query)
    elif option == "By Keyword or Genre":
        results = search_by_keyword(query)
    elif option == "By Director":
        results = search_by_column(query, 'crew')
    elif option == "By Actor":
        results = search_by_column(query, 'cast')
    else:
        results = pd.DataFrame([{'title': 'Invalid selection'}])

    st.write("### Recommended Movies")
    st.dataframe(results)