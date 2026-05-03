class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = 0
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
            most_freq = max(most_freq, counter[n]) 
        freq_to_num = [[] for _ in range(most_freq+1)]

        for num,freq in counter.items():
            freq_to_num[freq].append(num)
        
        res = []
        for i in range(len(freq_to_num)-1, 0, -1):
            if len(res) < k and len(freq_to_num[i]) > 0:
                res = res + freq_to_num[i]
                
        return res