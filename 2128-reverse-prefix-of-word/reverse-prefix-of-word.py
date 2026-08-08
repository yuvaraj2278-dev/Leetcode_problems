class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        p_index = word.index(ch)

        prefix = word[:p_index + 1]
        word = word[p_index + 1:]

        return prefix[::-1] + word