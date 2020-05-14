from typing import List


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        newx,newy=0,0
        u_num = command.count("U")
        r_num = command.count("R")
        r = x/r_num
        u = y/u_num
        if r*u_num >y or u*r_num>x:
            while True:
                for i in command:
                    if i=="U":
                        newy+=1
                    if i=="R":
                        newx+=1
                    if [newx,newy] in obstacles:
                        return False
                    if newx>x and newy>y:
                        return False
                    if newx==x and newy==y:
                        return True



if __name__ == '__main__':
    c = "URR"
    o =[[4,2]]
    x=3
    y=2
    print(Solution().robot(c,o,x,y))