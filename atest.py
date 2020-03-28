"""
input  int n
output res
"""
#
# class Solution:
#     def atest(self,n):
#         arr = str(n)
#         l = len(arr)
#         for x in range(l):
#             for j in range(0,l-1-1):
#                 if int(arr[j])>int(arr[j+1]):
#                     arr[j],arr[j+1]=arr[j+1],arr[j]
#         return  int(arr[::-1])%10
#
# if __name__ == '__main__':
# a=123
#
#     print(Solution().atest(a))
n = input()
a=str(n)
l = len(n)
for x in range(l):
  for j in range(0,l-1-1):
    if int(n[j])>int(n[j+1]):
      n[j],n[j+1]=n[j+1],n[j]
print((int(n[::-1])-int(a))%10)

