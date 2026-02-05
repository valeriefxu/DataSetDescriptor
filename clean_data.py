import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/spotify_long_hits_raw.csv")

# Inspect the data
print(df.head())
print(df.info())

# Basic cleaning
df = df.rename(columns={
    "track_name": "title",
    "artist_name": "artist"
})

# Remove rows with missing release year
df = df.dropna(subset=["release_year"])
df["release_year"] = df["release_year"].astype(int)

# Save clean dataset
df.to_csv("data/spotify_long_hits_clean.csv", index=False)

print("Clean dataset saved successfully.")
