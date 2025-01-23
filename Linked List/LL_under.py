head = {'value':11,
        'next':{
            'value':22,
            'next':{
                'value':33,
                'next':{
                    'value':44,
                    'next':None
                    }
                }
            }
        }

print(head['next']['next']['value'])
# this is how a linked list is pointing to the next nodes, 
# just to make it easier to understand we used dicts to represent the working under the hood
# value is the value of the node and next is the pointer to the next node
# as we will be using a list...
# print(my_ll.head.next.next.value) will be our print syntax