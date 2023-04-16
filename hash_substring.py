def read_input():
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    pattern = input().rstrip()
    text = input().rstrip()

    # return both lines in one return
    return pattern, text

def print_occurrences(output):
    # print all the positions of the occurrences of P in T in the ascending order
    print(" ".join(map(str, output)))

def get_occurrences(pattern, text):
    # list to store indices of occurrences
    indices = []

    # compute hash of pattern
    pattern_hash = hash(pattern)

    # compute hash of the first window of text
    text_hash = hash(text[:len(pattern)])

    # iterate through the remaining windows of text
    for i in range(len(text) - len(pattern) + 1):
        # if the hashes match, check if the pattern matches the current window of text
        if pattern_hash == text_hash:
            if pattern == text[i:i+len(pattern)]:
                indices.append(i)
        # if the hashes don't match, update the text hash for the next window
        if i < len(text) - len(pattern):
            text_hash = hash(text[i+1:i+len(pattern)+1])

    # return the list of indices of occurrences
    return indices

# main function
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
