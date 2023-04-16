def read_input():
    # read two lines: pattern and text
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    # print the occurrences
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # implementation of Rabin-Karp algorithm to find occurrences of pattern in text
    p = 10**9 + 7  # prime number for hash calculation
    x = 263  # base for hash calculation
    
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern, p, x)
    text_hashes = precompute_hashes(text, m, p, x)
    
    occurrences = []
    for i in range(n-m+1):
        if pattern_hash != text_hashes[i]:
            continue
        if text[i:i+m] == pattern:
            occurrences.append(i)
    return occurrences
    
def hash(s, p, x):
    h = 0
    for c in reversed(s):
        h = (h*x + ord(c)) % p
    return h

def precompute_hashes(text, m, p, x):
    n = len(text)
    h = [0] * (n-m+1)
    s = text[n-m:]
    h[n-m] = hash(s, p, x)
    y = 1
    for i in range(m):
        y = (y*x) % p
    for i in range(n-m-1, -1, -1):
        h[i] = (x*h[i+1] + ord(text[i]) - y*ord(text[i+m])) % p
    return h
    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
