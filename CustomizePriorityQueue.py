import heap


class CustomizeMinPriorityQueue(object):
    @classmethod
    def extract_min(cls, elements):
        length = len(elements)
        if length < 1:
            return ValueError('Invalid Heap')
        value = elements[1]
        elements[1] = elements[length - 1]
        elements.pop()
        heap.MinHeap().min_heapify(elements, len(elements) - 1, 1)
        return value
