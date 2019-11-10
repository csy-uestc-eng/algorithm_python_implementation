class Solution(object):
    alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        if len(words) == 0:
            return 0
        if len(words) == 1:
            return 1
        enc_word_set = set()
        for word in words:
            if word == "":
                continue
            enc_word = self.encode(word)
            enc_word_set.add(enc_word)
        return len(enc_word_set)

    def encode(self, word):
        enc_word = ""
        for c in word:
            enc_word += self.alpha[ord(c)-ord('a')]
        return enc_word

