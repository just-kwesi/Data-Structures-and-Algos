# connect nodes count




# songs chaining

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

def chaining(songs,starting_song):
    words = {song : (song.split()[0],song.split()[-1]) for song in songs}
    # print(words)

    graph = {song:[] for song in songs}
    
    for song in songs:
       last_word = words[song][1]
       for potential_next in songs:
           if potential_next != song and last_word == words[potential_next][0]:
               graph[song].append(potential_next)
    # print(graph)
    
    # helper to check for the longest chain
    def dfs(song, path):
        nonlocal longest_chain
        
        longest_chain = max(path,longest_chain,key=len)
        
        for next_song in graph[song]:
            if next_song not in path:
                path = path + [next_song]
                dfs(next_song,path)
        
    
    longest_chain = [starting_song]
    dfs(starting_song, [starting_song])
    print(longest_chain)
    return longest_chain
        
chaining(songs1,"Every Breath You Take")