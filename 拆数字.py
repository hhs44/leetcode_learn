from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0
        for x,y in enumerate(guess):
            if y==answer[x]:
                count+=1
