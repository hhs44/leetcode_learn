

from typing import List



class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        fenzi =1
        fenmu =cont[-1]
        del cont[-1]
        count= 0
        for x in cont[::-1]:
            count+=1
            if count==len(cont) and fenzi%fenmu!=0:
                fenzi+=x*fenmu
                for i in range(1,min(fenmu,fenzi)+1):
                    if ((fenzi%i==0))and (fenmu%i==0):
                            h=i
                return [int((fenzi)/h),int((fenmu)/h)]
            elif count==len(cont)and fenzi%fenmu==0:
                return [int(fenzi/fenmu+x),int(1)]
            fenzi+=x*fenmu
            t=fenmu
            fenmu=fenzi
            fenzi=t

        # a =0
        # count= 0
        # for x in cont[::-1]:
        #     count+=1
        #     if count==len(cont) and (x+a)%1!=0:
        #         a=float.as_integer_ratio(x+a)
        #         return float.as_integer_ratio(x+a)
        #     if count==len(cont) and (x+a)%1!=0:
        #         return [x+a,1]
        #     a=1/(a+x)
        # while (fen[0] % fen[1] == 0 & & fen[1] != 1)
        #     {
        #         fen[0] /= fen[0] / fen[1];
        #     fen[1] /= fen[0] / fen[1];
        #     }
if __name__ == '__main__':
    cont = [10,0,0,3]
    print(Solution().fraction(cont))