import sys, re

#sys.argv is the list of command-line arguments
#sys.argv[0] is the name of the program itself
#sys.argv[1] will be the regex specified at the command line
# regex = sys.argv[1]

#for every line passed into the script
# for line in sys.stdin:
#     #if it matches the regex, write it to stdout
#     if re.search(regex, line):
#         sys.stdout.write(line)
# count = 0
# for line in sys.stdin:
#     count += 1
# print count

from collections import Counter
try:
    num_words = int(sys.argv[1])
except:
    print "usage: most_common_words.py num_words"
    sys.exit(1)

counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in line.strip().split()
                  if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")