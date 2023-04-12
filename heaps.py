import heapq

H= [21,1,45,78,3,5]

# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

#Inserting into heap

H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H,8)
print(H)

H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)
print(H)

# Replacing in a Heap

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)