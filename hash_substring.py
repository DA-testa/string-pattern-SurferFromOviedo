def read_input():
    input_type = input().rstrip()

    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        filename = input()
        with open("test/" + filename, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    output = []

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            output.append(i)

        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+p_len+1])

    return output

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

