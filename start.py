import os
import re 
from collections import defaultdict
import socket

# List files in /home/data
files = os.listdir("/home/data")
#print(files)

# Read text files 
if_text = open('/home/data/IF.txt').read()
limerick_text = open('/home/data/Limerick-1.txt').read()

# Count words in each file
if_words = len(if_text.split())
limerick_words = len(limerick_text.split())
total_words = if_words + limerick_words

#print("\n Total No Of words in IF.txt "+str(if_words))
#print("\n Total No of words in Limerick.txt "+str(limerick_words))

# Get top words in IF.txt
if_word_counts = defaultdict(int)
for word in if_text.split():
    if_word_counts[word] += 1
    
if_top_3 = sorted(if_word_counts, key=if_word_counts.get, reverse=True)[:3]
#print("\n Top3 words in IF.txt are: ")
#for word in if_top_3:
 #   print(f"{word}: {if_word_counts[word]}")

#print("\n Host IP address: " + str(socket.gethostbyname('host.docker.internal')))
#print("\n Total number of words: " + str(total_words)) 

print("writing into a file")
# Write output to file
with open('/home/output/result.txt', 'w') as f:
    f.write(str(files))
    f.write("\n Total No Of words in IF.txt "+str(if_words))
    f.write("\n Total No of words in Limerick.txt " +str(limerick_words))
    f.write("\n Total number of words:  " + str(total_words)) 
    f.write("\nTop words in IF.txt: ")
    for word in if_top_3:
        f.write(f"\n{word}: {if_word_counts[word]}")
    f.write("\nHost IP address: " + str(socket.gethostbyname('host.docker.internal')))

#print("done")

# Read from the file after writing into it
print("\nReading from the file...")
with open('/home/output/result.txt', 'r') as f:
    file_contents = f.read()
    print("File contents:")
    print(file_contents)
print("Done")