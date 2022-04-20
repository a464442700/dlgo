import time
from multiprocessing import Process
def Merge(A,low,mid,high):
    B=A[low:high+1]
    i=low
    j=mid+1
    k=i
    while(i<=mid and j<=high):
        if B[i-low]<=B[j-low]:
            A[k]=B[i-low]
            i=i+1
        else:
            A[k]=B[j-low]
            j=j+1
        k=k+1
    if i<=mid:
        A[k:k+mid-i+1]=B[i-low:mid+1-low]
    if j<=high:
        A[k:k+high-j+1]=B[j-low:high+1-low]
def MergeSort(A,low,high):
    if(low<high):
        mid=int((low+high)/2)
        MergeSort(A,low,mid)
        MergeSort(A, mid+1, high)
        Merge(A,low,mid,high)

class MergeSortC(Process):
    def __init__(self, A,low,high):
        self.A=A
        self.low = low
        self.high = high
        super().__init__()

    def run(self):
        MergeSort(self.A,self.low,self.high)

if __name__=="__main__":
    start = time.process_time()
    n = 10
    A = [n - x for x in range(0, n)]
    print(A)
    mid = int(n/2)
    A1=A[0:mid+1]
    print(A1)
    A2=A[mid+1:n]
    p1 = MergeSortC(A1, 0, len(A1)-1)
    p2 = MergeSortC(A2, 0, len(A2)-1)
    p1.start()
    #p2.start()
    p1.join()
    #p2.join()
    print(A1)
    A=A1+A2
    Merge(A, 0, 5, n - 1)
    end = time.process_time()
    print(A)
    print("程序运行时间：", end - start, "秒")
