class Solution:

    def encode(self, strs: List[str]) -> str:
        self.word_length = [0]*len(strs)
        res = ""
        for index,s in enumerate(strs):
            res = res + s
            self.word_length[index] = len(s)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        for i in range(len(self.word_length)):
            res.append(s[start:start+self.word_length[i]])
            start = start+self.word_length[i]
            print(self.word_length[i])
            # print(res)
        return res
                
