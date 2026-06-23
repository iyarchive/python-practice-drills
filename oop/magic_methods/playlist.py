class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)
    
    def __eq__(self, other):
        return len(self.songs) == len(other.songs)
    
    def __str__(self):
        return f"{self.name} = {len(self.songs)} songs"
    

taylor_swift = Playlist("Taylor Swift")

taylor_swift.add_song("Better Than Revenge")
taylor_swift.add_song("Style")
taylor_swift.add_song("So Long, London")
taylor_swift.add_song("Epiphany")
taylor_swift.add_song("Should've Said No")

sabrina_carpenter = Playlist("Sabrina Carpenter")

sabrina_carpenter.add_song("Espresso")
sabrina_carpenter.add_song("House Tour")
sabrina_carpenter.add_song("Lie to Girls")
sabrina_carpenter.add_song("Sue Me")
sabrina_carpenter.add_song("Nonsense")

print(len(taylor_swift))
print(len(sabrina_carpenter))

print(taylor_swift == sabrina_carpenter)

print(sabrina_carpenter)
print(taylor_swift)
