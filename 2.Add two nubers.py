# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.l1=l1
        self.l2=l2
        i=0
        num1=0
        num2=0
        c1=self.l1
        c2=self.l2

        while (True):
            if (self.l1==None):
                break
            num1+=(self.l1.val)*(10**i)
            i+=1
            self.l1=self.l1.next
            

        i=0
        while (True):
            if (self.l2==None):
                break
            num2+=(self.l2.val)*(10**i)
            i+=1
            self.l2=self.l2.next
        
        num=num1+num2
        
        c=ListNode()
        temp=c
        i=len(str(num))
        k=0
        while(num>0):
            temp.val=num%10
            if(num/10 > 0):
                temp.next=ListNode()
                temp=temp.next
                num=num/10
            else :
                break
        return c


        