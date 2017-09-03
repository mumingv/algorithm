import random
import copy
 
def reservoirSampling(seq, k):
    localSeq = copy.deepcopy(seq)
    N = len(localSeq)   
    for i in xrange(k, N):
        M = int(random.uniform(0, i))
        if M < k :
            temp = copy.deepcopy(localSeq[M])
            localSeq[M] = copy.deepcopy(localSeq[i])
            localSeq[i] = temp
    return localSeq[0:k]

def main():
    a = range(100)
    k = 5
    print reservoirSampling(a, k)

if __name__ == '__main__':
    main()
