import pandas as pd

df = pd.read_csv("spotify_long_tracks_2014_2024.csv")

print(df.head())
print(df.info())

df = df.rename(columns={
    "Name": "title",
    "Duration (Minutes)": "duration",
    "Artists": "artist"
})

df = df.dropna(subset=["title", "duration", "artist"])

df.to_csv("spotify_long_hits_clean.csv", index=False)

print("Cleaned CSV saved with", len(df), "rows.")
