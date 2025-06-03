# Movie Recommendation System

This is a Streamlit-based movie recommendation system that allows users to search for movies based on:
- Movie Title
- Actor Name
- Director Name
- Keyword or Genre

The app suggests movies with their cast, crew, and average user rating.

---

## Project Overview
This project demonstrates how content-based filtering can be used to build a recommendation engine using text-based features. It was implemented using Python, with preprocessing and modeling done in a Jupyter Notebook (Google Colab), and deployed using Streamlit.

### Tools Used
- **Python**
- **Pandas** for data manipulation
- **Scikit-learn** for feature extraction and cosine similarity
- **Streamlit** for the interactive frontend
- **Google Colab** for development and preprocessing

---

## Dataset
This project uses [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) from Kaggle.

Download these files from Kaggle:
- `movies_metadata.csv`
- `credits.csv`
- `keywords.csv`
- `ratings.csv`
- `links.csv`

Place all files in the working directory before running the notebook.

---

## How It Works
1. Data is preprocessed and merged from various files.
2. A `movie_profile` feature is created by combining genres, cast, crew, and keywords.
3. Cosine similarity is calculated using `CountVectorizer` to measure similarity between movies.
4. The similarity matrix and helper mappings are saved as `.pkl` files.
5. A Streamlit app loads these `.pkl` files to provide real-time recommendations.

---

## Why Pickle Files Are Not Included
GitHub has a strict file size limit of **100 MB**, and the `cosine_sim.pkl` file exceeded **1.7 GB**. To avoid pushing large files, they were excluded using `.gitignore`. You will need to generate them locally using the notebook.

---

## Steps to Run This Project

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/MovieRecommendationSystem.git
cd MovieRecommendationSystem
```

### 2. Download Dataset
From [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset), download the required CSV files and place them in this folder.

### 3. Run the Notebook
Open `movie_recommender_notebook.ipynb` and run all cells to:
- Clean and preprocess the data
- Generate cosine similarity and feature subsets
- Save them as `.pkl` files:

```python
import pickle
with open('subset.pkl', 'wb') as f:
    pickle.dump(subset, f)
with open('cosine_sim.pkl', 'wb') as f:
    pickle.dump(cosine_sim, f)
with open('indices.pkl', 'wb') as f:
    pickle.dump(indices, f)
```

### 4. Run the Streamlit App
```bash
streamlit run movie_recommender_app.py
```

You’ll be able to:
- Choose a search method (title, actor, etc.)
- Type a query
- View 10 recommended movies with ratings

---

## Folder Structure
```
MovieRecommendationSystem/
├── movie_recommender_app.py             # Streamlit app
├── movie_recommender_notebook.ipynb     # Colab notebook for preprocessing
├── .gitignore                           # Ignores pickle files
└── README.md                            # This file
```

---

## Future Enhancements
- Add poster images using TMDB API
- Deploy to Streamlit Cloud or Hugging Face Spaces
- Add fuzzy matching for better name resolution

---