from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        required = Counter(c.lower() for c in licensePlate if c.isalpha())

        answer = None

        for word in words:
            count = Counter(word)

            if all(count[c] >= required[c] for c in required):
                if answer is None or len(answer) > len(word):
                    answer = word

        return answer