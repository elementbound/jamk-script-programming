# 4-5) Simulate the shop queue
#
# Add new persons to the queue from the list and serve them
# in "shop queue":
#
# # initialize list with the values
# clients=['first', 'second', "third", "fourth", "fifth"]
# queue=[]
# # to do - serve a client and then remove them from the queue
# add new client into the queue

import random

def main():
    clients=['first', 'second', "third", "fourth", "fifth"]

    # Create queue from clients
    queue = []
    for client in clients:
        # Prepend clients one by one
        queue = [client] + queue

    # Serve them
    while queue:
        print('Served', queue.pop())
    print()

    # Recreate queue, now with random priorities
    queue = []
    random.seed()

    for client in clients:
        priority = random.randrange(0,10)
        queue.append((priority, client))

    # Sort clients, always serve the one with highest priority
    queue = sorted(queue)
    while queue:
        priority, client = queue.pop()
        print('Serving', client, 'with priority', priority)

if __name__ == "__main__":
    main()
