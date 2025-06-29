# Movie-Recommender-system
 A content-based movie recommender system built with Streamlit. It suggests similar movies  and fetches real-time thumbnails

🌐 **Live Demo**: [Click here to try it](https://your-username.streamlit.app/)  
📽️ **Created by**: Sachin Kumar Tanti
---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **ML Logic**: Content-based filtering using cosine similarity
- **Data**: Precomputed similarity matrix and movie metadata (Pickle)
- **API**: OMDb API for fetching posters
---

## 🧠 How It Works

1. User selects a movie from the dropdown.
2. App retrieves top 30 similar movies using cosine similarity on movie vectors.
3. OMDb API fetches movie thumbnails in real-time.
4. Displays movies in a beautiful, responsive layout.

## 📦 Setup Instructions
 Clone the repo
cd movie-recommender
Install dependencies
pip install -r requirements.txt
Run the app
streamlit run app.py

📁 Project Structure
movie-recommender/
├── app.py                # Main Streamlit app
├── similarity.pkl        # Precomputed similarity matrix
├── movie_dict.pkl        # Dictionary of movie data
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
