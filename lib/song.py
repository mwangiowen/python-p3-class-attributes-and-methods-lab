class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count of songs
        Song.add_song_to_count()

        # Add genre to the list and update genre count
        self.add_to_genres()

        # Add artist to the list and update artist count
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        # Increment the count of songs
        cls.count += 1

    def add_to_genres(self):
        # Add genre to the list
        Song.genres.append(self.genre)

        # Update genre count
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists(self):
        # Add artist to the list
        Song.artists.append(self.artist)

        # Update artist count
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1




