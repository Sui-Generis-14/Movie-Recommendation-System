# Movie Recommendation System 🎬

This is a Streamlit-based movie recommendation system that suggests movies based on any of the following inputs:

- 🎥 Movie Title
- 🎭 Actor Name
- 🎬 Director Name
- 🔑 Keyword or Genre

## 🔍 How it works
The system uses a content-based filtering approach. It calculates cosine similarity between movies using a combined feature vector (`movie_profile`) built from:
- Genres
- Cast
- Crew (Director)
- Keywords

You can search for movies using one of the four options, and the system returns a list of similar movies along with:
- Movie Title
- Cast
- Crew
- Average User Rating

## 💾 Files Used
- `movie_recommender_app.py`: The main Streamlit app
- `subset.pkl`: Cleaned and subsetted dataset
- `cosine_sim.pkl`: Cosine similarity matrix
- `indices.pkl`: Mapping of movie titles to DataFrame indices

## 🚀 How to Run Locally
1. Install required libraries:
```bash
pip install streamlit pandas scikit-learn
```
2. Run the app:
```bash
streamlit run movie_recommender_app.py
```
3. Open the browser at `http://localhost:8501`

## 📂 Folder Structure
```
movie_recommender/
├── movie_recommender_app.py
├── subset.pkl
├── cosine_sim.pkl
├── indices.pkl
└── README.md
```

## ✅ Features
- Search movies by various attributes
- Displays top 10 results
- Shows genre, director, and ratings
- Interactive Web Page

## ✨ Future Improvements
- Add support for fuzzy matching
- Include movie posters and overviews
- Deploy to Streamlit Cloud