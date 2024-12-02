#out of list of scores, find the runner-up (second highest score)

links = [2,4,5,6,6,1]
n = len(links)
links.sort(reverse=True)
print(links)

# max_val = max(links)
# prin)t(max_val

for i in links:

    if i == max(links):
        continue
    else:
        print(i , "is runner-up")
        break



