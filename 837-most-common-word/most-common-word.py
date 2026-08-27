from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        extra = ".!@#$%^&*()_-+=[]{}\"';:.,<>?/"

        for i in extra:
            paragraph = paragraph.replace(i, " ")
        count = Counter(paragraph.lower().split())

        for word,frequency in count.most_common():
            if word not in banned:
                return word
            