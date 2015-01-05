class Solution:
    def rehashing(self, hashTable):
        newSize = len(hashTable) * 2
        newTable = [None for i in range(newSize)]
        for node in hashTable:
            cur = node
            while cur:
                tmp = ListNode(cur.val)
                hashcode = cur.val % newSize
                if newTable[hashcode] is None:
                    newTable[hashcode] = tmp
                else:
                    p = newTable[hashcode]
                    while p.next: p = p.next
                    p.next = tmp
                cur = cur.next
        return newTable
