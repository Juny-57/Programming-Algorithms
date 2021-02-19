#1

class Solution(object):
    def twoSum(self, nums, target):

        ary = []
        for i in range(0,len(nums)) :
            for j in range(i+1,len(nums)) :
                if (nums[i]+nums[j] == target) :
                    ary.append(i)
                    ary.append(j)
                    return ary

#2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        result = ListNode(99999) #아무 숫자 상관없음.
        result_tail = result #result의 엔드노드
        carry = 0
        
        while l1!=None or l2!=None or carry!=0 : # l1이나 l2가 None이 아니거나 carry도 0이 아닐 때까지 와일문을 돌음.
            
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            
            carry,r = divmod (val1+val2+carry,10) #몫과 나머지 저장
            result_tail.next = ListNode(r)
            result_tail = result_tail.next # 엔드노드를 옮김
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next