"""Count words in file."""


# put your code here.
input_file = open('twain.txt')
word_count = {}

for line in input_file:
    word_list = line.split(' ')
    for word in word_list:
        word_count[word] = word_count.get(word,0) + 1
        
for word, count in word_count.items() :
    print(word,count)