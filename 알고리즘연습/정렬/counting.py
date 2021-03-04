data = [7, 6, 8, 3, 1]
counts = [0]*(max(data)+1)
temp = [0]*len(data)

for idx in data:
    counts[idx] += 1
print(counts)

for i in range(1, len(counts)):
    counts[i] += counts[i-1]

print(counts)

for i in range(len(data) - 1, -1, -1):
    temp[counts[data[i]]-1] = data[i]
    counts[data[i]] -= 1
print(temp)
