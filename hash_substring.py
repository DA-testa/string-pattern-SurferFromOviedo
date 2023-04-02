def read_input():
    source = input()
    if "F" in source:
        filename = input()
        with open("tests/" + filename, 'r', encoding = "utf-8") as f:
            pattern = f.readline()
            text = f.readline()
    elif "I" in source:
        pattern = input().rstrip()
        text = input().rstrip()
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


