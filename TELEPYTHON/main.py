from standartmessage import standartmessagecoding
from methodfunction import *


message = "abcccabacabcabcbaaaa"

asil = standartmessagecoding(message)

lenofmessage = len(message)


freq = frequency_message(message)


heap = huffman_tree(freq)
heaptransform = transform_huffman_to_heaptree(heap)

huffmannumberright,huffmannumberleft = huffman_number(heaptransform)

huffmanlist = huffman_list(huffmannumberright, huffmannumberleft)
huffmandict = huffman_dict(huffmanlist)

methodcode = huffman_encoding(huffmandict, message)

freqlist = list(freq.items())

freqnew = []

freqnew = [item for sub in freqlist for item in sub]

calculatedfreqprob = calculate_prob(freqnew, lenofmessage)

newbit = newbitvalue(huffmanlist, calculatedfreqprob)
b = str(methodcode)
b1 = len(b)-12
sonuc = calculateefficiency(len(asil), b1)
print("normal gönderilecek mesaj :  " + message)
print("normal gönderilecek mesaj bitleri:  " + asil)
print("normal gönderilecek mesaj :  " + message)
print("method gönderilecek mesaj bitleri:  " + b)

result = open("telecomresult.txt", "w")

result.write(asil)
result.write("\n")
result.write(b)
result.close()