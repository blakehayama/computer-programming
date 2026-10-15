# Blake Hayama
# Computer Programming Period 4
# Sub Assignment
# September 21, 2026
playlist = ["my", "name", "is", "Blake"]
new_song = input("Enter another song title:")
new_song = new_song.strip().title()
playlist.append(new_song)
print("\nPart 1: Playlist after adding your song")
print(playlist)
print("\nPart 2: Number of songs")
print("Number of songs:", len(playlist))
playlist.insert(0, "my")
print("\nAfter inserting a bonus song at the beginning:")
print(playlist)
playlist.remove("is")
print("\nAfter removing 'is':")
print(playlist)
del playlist[1]
print("\nAfter deleting the item at index 1:")
print(playlist)
print("\nSongs in alphabetical order (without changing the original list):")
print(sorted(playlist))
playlist.sort()
print("\nAfter sorting the playlist:")
print(playlist)
playlist.reverse()
print("\nAfter reversing the playlist:")
print(playlist)
print("\nPart 3: Is 'name' in the playlist?")
print("name" in playlist)
print("\nAll song titles in uppercase:")
for song in playlist:
    print(song.upper())
print("\nPart 4: Numbered tracklist")
for i in range(len(playlist)):
    print(i + 1, playlist[i])
print("\nStretch: Songs with the letter 'a' in the title")
for i in range(len(playlist)):
    if "a" in playlist[i].lower():
        print(i + 1, playlist[i])