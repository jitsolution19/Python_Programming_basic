from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ingredients_input = ["gobi", "namak","pyaaz"]

# Sample recipes
recipes = [   
    {"title": "Aalu Sabji", "ingredients":"boiled aalu	oil	hing namak	haldi rai jeera	green chilli pyaaz"},
    {"title": "Raw Aalu Tomato Sabji", "ingredients": "raw aalu oil hing namak haldi rai jeera green chilli tomato"},
    {"title": "Bhandare Aalu Tomato Sabji", "ingredients": "boiled aalu oil hing namak haldi rai jeera green chilli tomato khade masale"},
    {"title": "Aalu Tomato Sabji","ingredients":"boiled aalu oil hing namak	haldi rai jeera	green chilli tomato"},
    {"title": "Lauki Sabji", "ingredients":"lauki oil hing namak haldi green chilli tomato"},
    {"title": "Bhindi Sabji", "ingredients":"bhindi oil hing namak haldi green chilli pyaaz"},
    {"title": "Bharma Bhindi Sabji","ingredients":"Bhindi oil hing namak	haldi green chilli pyaaz dahi tomato"},
    {"title": "Aalu Gobi Dry Sabji","ingredients":"Aalu Gobi oil hing namak haldi jeera	green chilli Khade masale"}	
]

# Vectorize
corpus = [r["ingredients"] for r in recipes]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus + [" ".join(ingredients_input)])

# Compute similarity
similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
best_match = recipes[similarity.argmax()]
least_match = recipes[similarity.argmin()]
print("Suggested Dinner:", best_match["title"])
print("Least Suggested Dinner:", least_match["title"])
