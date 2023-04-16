# python3

def read_input():
    with open('input.txt', 'r') as f:
        pattern = f.readline().strip()
        text = f.readline().strip()
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function finds the occurrences of pattern in text using Rabin-Karp algorithm
    p = 1000000007
    x = 1
    t_hash = 0
    p_hash = 0
    positions = []
    
    # calculate hash of pattern
    for i in range(len(pattern)):
        p_hash = (p_hash + ord(pattern[i]) * x) % p
        x = (x * 53) % p
    
    x = 1
    
    # calculate hash of first |pattern| characters of text
    for i in range(len(pattern)):
        t_hash = (t_hash + ord(text[i]) * x) % p
        x = (x * 53) % p
        
    # check for a match in each possible starting position of pattern in text
    for i in range(len(text) - len(pattern) + 1):
        if t_hash == p_hash:
            if text[i:i+len(pattern)] == pattern:
                positions.append(i)
        
        # calculate hash for next window in text
        if i < len(text) - len(pattern):
            t_hash = (53*(t_hash-ord(text[i])*x) + ord(text[i+len(pattern)])) % p
            if t_hash < 0:
                t_hash += p
        
    return positions

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
