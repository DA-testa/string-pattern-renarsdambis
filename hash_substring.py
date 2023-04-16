# Rabin-Karp algorithm for string matching

# function to find all occurrences of pattern in text
def rabin_karp(pattern, text):
    # length of pattern and text
    m, n = len(pattern), len(text)
    
    # initialize prime number and d (number of characters in the alphabet)
    prime = 101
    d = 256
    
    # initialize hash values for text and pattern
    p_hash = 0  # hash value for pattern
    t_hash = 0  # hash value for text
    
    # h is the value of d^(m-1) with modulus prime
    h = pow(d, m-1) % prime
    
    # calculate the hash value of pattern and the first window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime
    
    # slide the pattern over the text one by one and check for a match
    occurrences = []
    for i in range(n-m+1):
        # check if hash values of the current window of text and pattern match
        if p_hash == t_hash:
            # check if characters in the window and pattern match
            j = 0
            while j < m and text[i+j] == pattern[j]:
                j += 1
            if j == m:
                occurrences.append(i)
        
        # calculate the hash value of the next window of text
        if i < n-m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i+m])) % prime
            if t_hash < 0:
                t_hash = t_hash + prime
    
    return occurrences

# function to read input from keyboard or file
def read_input():
    # read two lines of input: pattern and text
    pattern = input().rstrip()
    text = input().rstrip()
    
    return pattern, text

# function to print occurrences of pattern in text
def print_occurrences(occurrences):
    print(' '.join(map(str, occurrences)))

# main function
if __name__ == '__main__':
    # read input
    pattern, text = read_input()
    
    # find occurrences of pattern in text using Rabin-Karp algorithm
    occurrences = rabin_karp(pattern, text)
    
    # print occurrences
    print_occurrences(occurrences)