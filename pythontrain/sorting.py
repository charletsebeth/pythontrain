def bubble_sort(items):

    '''Return array of items, sorted in ascending order

    Input variable: should be a list which user wants to be be sorted in ascending
    order.

    Return variable: The list sorted in ascended order

    '''

    for outer in range(len(items)-1,0,-1):
        for inner in range(outer):
            if items[inner]>items[inner+1]:
                temp = items[inner]
                items[inner] = items[inner+1]
                items[inner+1] = temp
    return items

def merge_sort(items):

    '''Implementation of merge sort algorithm in python
       Input variable: should be a list which user wants to be be sorted in ascending
       order. Return variable: The list sorted in ascended order
    '''

    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    return items
            
def quick_sort(items):

    '''Implementation of quick sort algorithm in python

    Input variable: should be a list which user wants to be be sorted in ascending
    order.

    Return variable: The list sorted in ascended order

       '''
    quickSortHelper(items,0,len(items)-1)

    return items

def quickSortHelper(items,first,last):
   if first<last:

       splitpoint = partition(items,first,last)

       quickSortHelper(items,first,splitpoint-1)
       quickSortHelper(items,splitpoint+1,last)


def partition(items,first,last):
   pivotvalue = items[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and items[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while items[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = items[leftmark]
           items[leftmark] = items[rightmark]
           items[rightmark] = temp

   temp = items[first]
   items[first] = items[rightmark]
   items[rightmark] = temp


   return rightmark
