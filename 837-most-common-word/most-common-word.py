from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        word = re.findall(r"[a-z]+",paragraph.lower())
        count = Counter(word)

        for word, freqency in count.most_common():
            if word not in banned:
                return word