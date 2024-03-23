def find_winners(s):
    # Function to count vowels in a string
    def count_vowels(word):
        return sum(1 for char in word if char in 'aeiou')

    winners = []

    for word in s:
        # Count the total number of vowels in the string
        total_vowels = count_vowels(word)

        # Determine the winner based on the number of vowels
        if total_vowels % 2 == 0:
            winners.append("Chris")
        else:
            winners.append("Alex")

    return winners

# Test the function with the provided example
s = ["ljis", "lhr", "gms"]
print(find_winners(s))  # Expected output: ["Alex", "Chris", "Chris"]


def game_outcome(strings):
    # Function to count vowels in a string
    def count_vowels(word):
        return sum(char in 'aeiou' for char in word)

    results = []
    
    for word in strings:
        # Count the total number of vowels in the string
        vowel_count = count_vowels(word)

        # Determine the winner of the round
        if vowel_count % 2 == 1:
            results.append("Alex")  # Alex wins if odd number of vowels
        else:
            results.append("Chris")  # Chris wins if even number of vowels or no vowels

    return results

# Testing the function with the given example
s = ["ljis", "lhr", "gms"]
print(game_outcome(s))  # Expected output: ["Alex", "Chris", "Chris"]
print(float('inf'))



def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    nei = defaultdict(list)
    wordList.append(beginWord)
    
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + '*' + word[j+1:]
            nei[pattern].append(word)
    
    visit = set(beginWord)
    q = deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                for neiggbor in nei[pattern]:
                    if neiggbor not in visit:
                        visit.add(neiggbor)
                        q.append(neiggbor)
                    
    print(nei)
