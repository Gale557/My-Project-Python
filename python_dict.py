import json
Best_song_Artist = {
    "Shawn Mendes": "Treat You Better",
    "Justin Bieber": "Love yourself",
    "Ed Sheeran": "Thingking Out Loud",
    "Charlie Puth": "Marvin gaye",
    "Taylor Swift": "Blank Space",
    "The Weekend": "Blinding Light",
    "Bruno Mars": "Lazy Song"
}
print(Best_song_Artist)
print(type(Best_song_Artist))
result = json.dumps(Best_song_Artist)
print(result)
print(type(result))
