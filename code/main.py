def swap(heap, pos, o, n):
    pos[heap[o]], pos[heap[n]] = n, o
    heap[o], heap[n] = heap[n], heap[o]

def up_heapify(heap, pos, i):
    while i > 0:
        p = (int)((i - 1) / 2)
        if heap[i][0] > heap[p][0]:
            swap(heap, pos, i, p)
            i = p
        else:
            break

def down_heapify(heap, pos, i):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if l >= len(heap):
           break
        if r >= len(heap):
            if heap[i][0] < heap[l][0]:
                swap(heap, pos, i, l)
            break
        if (heap[l][0] <= heap[i][0]) and (heap[r][0] <= heap[i][0]):
            break
        if heap[l][0] > heap[r][0]:
            swap(heap, pos, i, l)
            i = l
        else:
            swap(heap, pos, i, r)
            i = r
    return i

def insert(heap, pos, elem):
    heap.append(elem)
    pos[elem] = len(heap) - 1
    up_heapify(heap, pos, len(heap) - 1)

def pop(heap, pos, v):
    o = pos[v]
    if o == len(heap) - 1:
        pos[v] = None
        return heap.pop()
    n = heap.pop()
    pos[v] = None
    if len(heap) == 0:
        return v
    pos[n] = o
    heap[o] = n
    d = down_heapify(heap, pos, o)
    up_heapify(heap, pos, d)
    return v

def common(str1, str2):
    i = min(len(str1), len(str2))
    while i > 0:
        if str1[(len(str1) - i):] == str2[:i]:
            return i
        i = i - 1
    return i

def short_reads_reconstruct(s_list):
    i_set = set(range(0, len(s_list)))
    to_remove = set()
    for i in range(0, len(s_list)):
        for j in range(0, len(s_list)):
            if (i != j) and (s_list[j].find(s_list[i]) != -1):
                to_remove.add(i)
    for i in to_remove:
        i_set.remove(i)

    dist = list()
    pos = dict()
    entry = list(s_list)
    
    for j in i_set:
        entry[j] = list(s_list)
        for k in i_set:
            if j != k:
                entry[j][k] = (common(s_list[j], s_list[k]), j, k)
                insert(dist, pos, entry[j][k])
    
    while len(i_set) > 1:
        (max_common, max_index1, max_index2) = pop(dist, pos, dist[0])
        s_list[max_index1] += s_list[max_index2][max_common:]
        i_set.remove(max_index2)
        if len(i_set) == 1:
            break
        for j in i_set:
            if j != max_index1:
                elem = (entry[max_index2][j][0], max_index1, j)
                pop(dist, pos, entry[max_index1][j])
                entry[max_index1][j] = elem
                insert(dist, pos, elem)
                pop(dist, pos, entry[j][max_index2])
            pop(dist, pos, entry[max_index2][j])
    return s_list[min(i_set)]

def main():
    import sys
    s_list = sys.stdin.read().splitlines()
    t = short_reads_reconstruct(s_list)
    sys.stdout.write(t + "\n")

main()