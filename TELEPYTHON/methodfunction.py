from collections import defaultdict
from heapq import heappush, heappop, heapify
from bitarray import bitarray

def frequency_message (codingsend):
    
    freq_lib = defaultdict(int)    # Kütüphane oluşturuldu
    for ch in codingsend:      # Her harf frekansı tespit edilebilmesi için sayılıp kütüphaneye kayıt edilir. 
        freq_lib[ch] += 1
    
    
    

    return freq_lib

def huffman_tree (freq):
    
    heap = [[fq, [sym, ""]] for sym, fq in freq.items()]  
    
    
    return heap

def transform_huffman_to_heaptree (heap):
    
    heapify(heap) # transform the list into a heap tree structure
   
    
    return heap

def huffman_number (transformheap):
    
    while len(transformheap) > 1:
        right = heappop(transformheap)  
        
        left = heappop(transformheap)
        
    
        for pair in right[1:]:  
            pair[1] = '0' + pair[1]   
        for pair in left[1:]:  
            pair[1] = '1' + pair[1]   
        heappush(transformheap, [right[0] + left[0]] + right[1:] + left[1:])
        
    return right,left

def huffman_list (right,left):
    
    huffman_list = right[1:] + left[1:]
    
    return huffman_list

def huffman_dict (huffmanlist):
    
    huffman_dict = {a[0]:bitarray(str(a[1])) for a in huffmanlist}
    
    return huffman_dict

def huffman_encoding (encoded,message):
    
    encoded_message = bitarray()
    encoded_message.encode(encoded,message)
    
    return encoded_message

def calculate_prob (freqnew,lenghtofmessage):
    for i in range(1,len(freqnew),2):
    
        freqnew[i] = freqnew[i]/lenghtofmessage

        
    return freqnew

def newbitvalue (listwhichwillsort, freqprobselectlist ):
    
    sortedhuffmanlist =sorted(listwhichwillsort)
    
    newbit = 0
    lst = []
    lst1 = []
    for i in range(1,len(freqprobselectlist),2):
        
        lst.insert(i, freqprobselectlist[i])
        
    
    for i in range(0,len(sortedhuffmanlist)):
        lst1.insert(i, len(sortedhuffmanlist[i][1]))
        
    for i in range(0,len(lst)):
        
        new = lst[i]*lst1[i]
        
        newbit = newbit + new

    return newbit 

def calculateefficiency (normalbitsize, methodbitsize):
    
    result = methodbitsize/normalbitsize
    
    return result
    