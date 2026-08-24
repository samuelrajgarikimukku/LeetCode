class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        k = set()
        for word in words:
            code = ""
            for ch in word:
                code += morse_code[ord(ch)-97]
            k.add(code)
        return len(k)