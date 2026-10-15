file_name=input("enter a file name:")
f=open(file_name,"r")
text=f.read()
text=text.lower()
words=text.split()
word_freq={}
for word in words:
    if word in word_freq:
            word_freq[word]+=1
else:
    word_freq[word]=1
sorted_words=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
print("\n top 10 most frequent words")
for words,freq in sorted_words[:10]:
    print(f"{word}:{freq}")
f.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    
