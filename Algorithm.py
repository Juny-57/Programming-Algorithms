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

#2@
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



#3 중벅여부 탐색 with dictionary + in 
# O(1)
#탐색과 확인이 필요한 작업에 set 혹은 dictionary와 in을 사용하면 효율적이다. 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        dct = {} # dct는 알파벳이 키, 인덱스가 밸류
        max_so_far = temp_max = start = 0 #start는 중복되지 않는 조합의 첫번째 원소를 가르킴. 

        for index, i in enumerate(s) :
            if i in dct and dct[i]>=start : #dict의 in은 key에 한해서 작동함.
                #굳이 매번 for문 돌려서 확인하는 것보다 in을 사용하면 간단하게 해결.
                max_so_far = max(max_so_far,temp_max) #같은게 있다면 우선 temp값과 비교해서 최대값을 갱신하고
                temp_max = index - dct[i] # temp값에 지금 현재 인덱스와 중복되는 알파벳 사이의 간격을 넣는다.
                start = dct[i]+1 # 포인터값 이동
            else :
                temp_max +=1
            dct[i] = index

        return max(max_so_far,temp_max)


#4 중앙값찾기 (만족도 - 하)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_arr = []
        sum = 0
        count = 0
        
        for i in range(len(nums1)) :
            merged_arr.append(nums1[i])

        for i in range(len(nums2)) :
            merged_arr.append(nums2[i])

        merged_arr.sort()
        
        for i in range (len(merged_arr)) :
            if ( len(merged_arr)%2 == 0 and (i+1 == len(merged_arr)/2) or 
               (i+1 == len(merged_arr)/2+1)) :
                sum += merged_arr[i]
                count+=1
            elif ( len(merged_arr)%2!=0 and (i+1 == len(merged_arr)/2 +1) ) :
                sum+=merged_arr[i]
                count+=1
                
        return float(sum)/count
        
#5
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        dct = {}
        temp_answer = ''
        answer = ''

        
        for index, i in enumerate(s):
            if i in dct and index>dct[i]:
                temp_answer+=i
        
                answer = temp_answer if len(temp_answer) > len(answer) else answer
                temp_answer=''
                
            else :
                temp_answer+=i
                
            dct[i] = index
        
        
        return temp_answer if len(temp_answer) > len(answer) else answer