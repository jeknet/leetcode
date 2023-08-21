# https://leetcode.com/problems/split-strings-by-separator/submissions/1028112335/
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return list(self.processWords(separator.join(words), separator))
        
    def processWords(self, words, separator):
        partial = ""
        for letter in words:
            if letter != separator:
                partial += letter
            elif len(partial)>0:
                yield partial
                partial = ""
        if len(partial)>0:
            yield partial
