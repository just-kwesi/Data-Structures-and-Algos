def chaining(songs, start_song):
    # Extract first and last words of each song for easy comparison
    words = {song: (song.split()[0], song.split()[-1]) for song in songs}
    print(words)

    # Build the graph
    graph = {song: [] for song in songs}
    for song in songs:
        last_word = words[song][1]
        for potential_next in songs:
            if potential_next != song and words[potential_next][0] == last_word:
                graph[song].append(potential_next)

    # Helper function for DFS
    def dfs(song, path):
        nonlocal longest_chain
        longest_chain = max(longest_chain, path, key=len)  # Update longest chain if current path is longer
        for next_song in graph[song]:
            if next_song not in path:
                dfs(next_song, path + [next_song])

    longest_chain = [start_song]
    dfs(start_song, [start_song])
    return longest_chain

# Test cases
songs1 = [
    "Down By the River",
    "River of Dreams",
    "Take me to the River",
    "Dreams",
    "Blues Hand Me Down",
    "Forever Young",
    "American Dreams",
    "All My Love",
    "Cantaloop",
    "Take it All",
    "Love is Forever",
    "Young American",
    "Dreamship",
    "Every Breath You Take",
]
song1_1 = "Every Breath You Take"
# Uncomment to test
print(chaining(songs1, song1_1))

songs2 = [
    "Bye Bye Love",
    "Nothing at All",
    "Money for Nothing",
    "Love Me Do",
    "Do You Feel Like We Do",
    "Bye Bye Bye",
    "Do You Believe in Magic",
    "Bye Bye Baby",
    "Baby Ride Easy",
    "Easy Money",
    "All Right Now",
]
song2_1 = "Bye Bye Bye"
# Uncomment to test
print(chaining(songs2, song2_1))

songs3 = [
    "Love Me Do",
    "Do You Believe In Magic",
    "Magic You Do",
    "Magic Man",
    "Man In The Mirror"
]
song3_1 = "Love Me Do"
# Uncomment to test
print(chaining(songs3, song3_1))


# All Test Cases:
# chaining(songs1, song1_1) => ['Every Breath You Take', 'Take it All', 'All My Love', 'Love is Forever', 'Forever Young', 'Young American', 'American Dreams', 'Dreams']
# chaining(songs1, song1_2) => ['Dreams']
# chaining(songs1, song1_3) => ['Blues Hand Me Down', 'Down By the River', 'River of Dreams', 'Dreams']
# chaining(songs1, song1_4) => ['Cantaloop']
# chaining(songs2, song2_1) => ['Bye Bye Bye', 'Bye Bye Baby', 'Baby Ride Easy', 'Easy Money', 'Money for Nothing', 'Nothing at All', 'All Right Now']
# chaining(songs2, song2_2) => ['Bye Bye Love', 'Love Me Do', 'Do You Feel Like We Do', 'Do You Believe in Magic']
# chaining(songs3, song3_1) => ['Love Me Do', 'Do You Believe in Magic', 'Magic Man', 'Man In The Mirror']
 