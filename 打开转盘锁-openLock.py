import collections
from _ast import List
from queue import Queue




class Solution(object):
    def openLock( deadends, target):

        q = Queue()
        q.put("0000")
        visited = set("0000")
        count = 0
        deadend = set(deadends)
        if (target in deadend) or ("0000" in deadend): return -1
        while q:
            count += 1
            size = q.qsize()
            for i in range(size):
                site = q.get()
                a=int(site)%10
                b=int((int(site)/10)%10)
                c=int((int(site)/100)%10)
                d=int((int(site)/1000)%10)
                res = [None]*8
                res[0]=str(d*1000+c*100+b*10+(a+10-1)%10).zfill(4)
                res[1]=str(d*1000+c*100+b*10+(a+1)%10).zfill(4)
                res[2]=str(d*1000+c*100+((b+10-1)%10)*10+a).zfill(4)
                res[3]=str(d*1000+c*100+((b+1)%10)*10+a).zfill(4)
                res[4]=str(d*1000+((c+10-1)%10)*100+b*10+a).zfill(4)
                res[5]=str(d*1000+((c+1)%10)*100+b*10+a).zfill(4)
                res[6]=str(((d+10-1)%10)*1000+c*100+b*10+a).zfill(4)
                res[7]=str(((d+1)%10)*1000+c*100+b*10+a).zfill(4)
                for k in range(8):
                    if site == target or res[k]==target:
                        return count
                    if res[k] in visited or res[k] in deadend:
                        continue
                    q.put(res[k])
                    visited.add(res[k])
        return -1
que = collections.deque()

if __name__ == '__main__':
    # deadends = ["0201", "0101", "0102", "1212", "2002"]
    # target = "0202"
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    a = Solution.openLock(deadends,target)
    print(a)

