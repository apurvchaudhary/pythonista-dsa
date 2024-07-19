from singly_linked_list import LinkedList

lla = LinkedList()
lla.append(7)
lla.append(1)
lla.append(6)
llb = LinkedList()
llb.append(9)
llb.append(9)
llb.append(2)


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.append(int(result % 10))
        carry = result / 10

    return ll


print(lla)
print(llb)
print(sumList(lla, llb))
