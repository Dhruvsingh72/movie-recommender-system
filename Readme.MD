🎬 Movie Recommender System (Content-Based)

This is a Content-Based Movie Recommendation System built using Python, Streamlit, and The Movie Database (TMDb) API.
It recommends movies similar to the selected movie and displays their posters.

🚀 Features

🔍 Select a movie and get Top 5 similar movie recommendations

🧠 Uses Cosine Similarity for recommendation

🎭 Fetches movie posters using TMDb API

⚡ Fast response & clean UI

🌐 Deployable on Streamlit Cloud / Render / HuggingFace Spaces

🗂️ Project Structure
movie_recommender_system/
│── app.py
│── movies.pkl
│── similarity.pkl
│── requirements.txt
│── README.md
└── .gitignore

🛠️ Technologies Used

Python

Pandas

Streamlit

TMDb API

Pickle (for models & metadata)

scikit-learn (similarity matrix)

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/Dhruvsingh72/movie-recommender-system.git
cd movie-recommender-system

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the App Locally
streamlit run app.py


Your app will open in the browser at:
🔗 http://localhost:8501

🎨 How It Works

Select a movie from the dropdown

The model finds similar movies using a precomputed similarity matrix

Movie posters are fetched from TMDb API

Recommendations with posters are shown in a 5-column layout

🔑 TMDb API Setup

Replace your API key inside fetch_poster():

'https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY&language=en-US'

🚀 Deployment

Can be deployed on:

Streamlit Cloud (easiest)

Render

HuggingFace Spaces

Vercel (with streamlit-edge)

Just upload:

✔ app.py
✔ movies.pkl
✔ similarity.pkl
✔ requirements.txt
✔ README.md

📄 License

This project is created for learning purposes.
Feel free to use or modify it.
