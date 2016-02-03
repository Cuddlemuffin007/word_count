# tiy day 3 exercise - word frequency program
from sys import argv, exit

IGNORE = ['a', 'able', 'about', 'across', 'after', 'all',
          'almost', 'also', 'am', 'among', 'an', 'and', 'any',
          'are', 'as', 'at', 'be', 'because', 'been', 'but',
          'by', 'can', 'cannot', 'could', 'dear', 'did', 'do',
          'does', 'either', 'else', 'ever', 'every', 'for', 'from',
          'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers',
          'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into',
          'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely',
          'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no',
          'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other',
          'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should',
          'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them',
          'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too',
          'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where',
          'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet',
          'you', 'your'
          ]

filename = None

if len(argv) > 1:
    filename = argv[1]
else:
    print("No file provided.")
    exit(0)

with open(filename) as my_file:
    contents = my_file.read()

no_nos = ".,;:\"?!-"

for no_no in no_nos:
    contents = contents.replace(no_no, '').lower()

unique_words = set(contents.split())
unique_words -= set(IGNORE)

word_freq = {word: contents.count(word) for word in unique_words}

ordered_result = []
for word in sorted(word_freq, key=word_freq.get, reverse=True):
    ordered_result.append((word, word_freq[word]))

for i in range(20):
    print((i+1), ordered_result[i][0], ordered_result[i][1])
