import os
import tempfile
import heapq
import sys
import asyncio
import time


class heapnode:

    def __init__(self,item,fileHandler,):
        self.item = item
        self.fileHandler = fileHandler

sortedTempFileHandlerList = []

def getCurrentDir():
    cwd = os.getcwd()

def iterateSortedData(sortedCompleteData):
    for no in sortedCompleteData:
        print (no)

def heapify(arr,i,n,):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left].item < arr[i].item:
        smallest = left
    else:
        smallest = i

    if right < n and arr[right].item < arr[smallest].item:
        smallest = right

    if i != smallest:
        (arr[i], arr[smallest]) = (arr[smallest], arr[i])
        heapify(arr, smallest, n)

def construct_heap(arr):
    l = len(arr)
    mid = l // 2
    while mid >= 0:
        heapify(arr, mid, l)
        mid -= 1

def mergeSortedtempFiles_low_level():
    list = []
    sorted_output = []
    for tempFileHandler in sortedTempFileHandlerList:
        item = int(tempFileHandler.readline().strip())
        list.append(heapnode(item, tempFileHandler))

    construct_heap(list)
    while True:
        min = list[0]
        if min.item == sys.maxsize:
            break
        sorted_output.append(min.item)
        fileHandler = min.fileHandler
        item = fileHandler.readline().strip()
        if not item:
            item = sys.maxsize
        else:
            item = int(item)
        list[0] = heapnode(item, fileHandler)
        heapify(list, 0, len(list))
    return sorted_output

async def sortOneFile(file_no):
    unsorted_file_name = "unsorted_" + str(file_no) + ".txt"
    test_file = open(unsorted_file_name, "r")
    lines = test_file.readlines()
    lines = [int(i) for i in lines]

    lines.sort()
    sorted_file_name = "sorted_" + str(file_no) + ".txt"
    with open(sorted_file_name, "w") as f:
        for item in lines:
            f.write("%s\n" % item)

def getFinalResult():
    mergeresult = mergeSortedtempFiles_low_level()
    mergeresult = [int(i) for i in mergeresult]
    with open("async_ext_merge_sort_result.txt", "w") as f:
        for item in mergeresult:
            f.write("%s\n" %item)

async def main():
    # start = time.time()
    await asyncio.gather(
        sortOneFile(1),
        sortOneFile(2),
        sortOneFile(3),
        sortOneFile(4),
        sortOneFile(5),
        sortOneFile(6),
        sortOneFile(7),
        sortOneFile(8),
        sortOneFile(9),
        sortOneFile(10),
    )

    # end = time.time()
    # print(f'Time: {end-start:.4f} sec')

    for x in range(1,11):
        sorted_file_name = "sorted_" + str(x) + ".txt"
        tempFile = open(sorted_file_name, "r")
        sortedTempFileHandlerList.append(tempFile)
    #print (mergeSortedtempFiles_low_level())
    getFinalResult()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

