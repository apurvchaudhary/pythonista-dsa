from singly_linked_list import LinkedList, Node

node = Node(10)
lla = LinkedList()
lla.append(7)
lla.append(1)
lla.append(6)
lla.append_node(node)

llb = LinkedList()
llb.append(9)
llb.append(9)
llb.append(2)
llb.append_node(node)


def intersection(llA: LinkedList, llB: LinkedList):
    if llA.tail is not llB.tail:
        return False

    lenA = llA.length
    lenB = llB.length

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = longer.length - shorter.length
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode


print(lla)
print(llb)

print(intersection(lla, llb))
