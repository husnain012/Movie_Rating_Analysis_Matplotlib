import pandas as pd
import matplotlib.pyplot as plt

print("="*50)
print("MOVIE RATINGS ANALYSIS")
print("="*50)
print("\n")

# Load Data
data = pd.read_csv("movies_dataset.csv")
print("------------ Data Overview ------------")
print("\n")
print(data.head())
print("\n")

# 1) Top 5 Highest Rated Movies
high_rated = data.sort_values(by="rating", ascending=False)
top_5 = high_rated.head(5)
print("------------ Top 5 Highest Rated Movies ------------")
print("\n")
print(top_5)
print("\n")

# 2) Average Rating Per Genre
avg_rating = data.groupby("genre")["rating"].mean()
print("------------ Average Rating Per Genre ------------")
print("\n")
print(avg_rating)
print("\n")

# 3) Count of Movies Released Each Year
movies_count = data.groupby("release_year")["movie_name"].count()
print("------------ Count of Movies Released Each Year ------------")
print("\n")
print(movies_count)
print("\n")

# 4) Movies with rating > 8.0 and votes > 50000
highly_rated_popular_movies = data[(data["rating"] > 8.0) & (data["votes"] > 50000)]
print("------------ Movies with rating > 8.0 and votes > 50000 ------------")
print("\n")
print(highly_rated_popular_movies)
print("\n")

# 5) Genre with the Highest Average Votes
h_avg_rating = data.groupby("genre")["votes"].mean().idxmax() 
print("------------ Genre with the Highest Average Votes ------------")
print("\n")
avg_votes = data.groupby("genre")["votes"].mean()
print(h_avg_rating, ":", avg_votes[h_avg_rating])
print("\n")

# 6) Longest Movie by Duration
long_movie = data.loc[data["duration"].idxmax()]
print("------------ Longest Movie by Duration ------------")
print("\n")
print(long_movie)
print("\n")

# 7) Bar Chart — Genre vs Average Rating

print("------------ Bar Chart — Genre vs Average Rating ------------")
print("\n")
plt.style.use("ggplot")
plt.figure(figsize=(8, 4))
avg_rating = data.groupby("genre")["rating"].mean()
plt.bar(avg_rating.index, avg_rating.values, color="lightblue", edgecolor="black")
plt.title("Average Rating Per Genre")
plt.xlabel("Genre")
plt.ylabel("Rating")

# Display values over bars
for i, v in enumerate(avg_rating.values):
    plt.text(i, v + 0.05, round(v, 2), ha='center')

plt.savefig("Visualization/genre_avg_rating.png")
plt.show()
print("\n")

# 8) Line Plot — Movies Released Per Year
print("------------ Line Plot — Movies Released Per Year ------------")
print("\n")
movies_count = data.groupby("release_year")["movie_name"].count()

plt.figure(figsize=(14, 6))
plt.plot(movies_count.index, movies_count.values, marker="o", color="green", linewidth=2, alpha=0.6, linestyle="--")
plt.title("Movies Released Per Year", fontsize=16)
plt.xlabel("Years", fontsize=12)
plt.ylabel("Movies", fontsize=12)

# Display values over bars
for i, v in enumerate(movies_count.values):
    plt.text(movies_count.index[i], v + max(movies_count.values)*0.01, str(v), ha="center")

plt.savefig("Visualization/movies_per_year.png")
plt.show()