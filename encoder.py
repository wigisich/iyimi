# Function for merging the list of strings into a single, long string with ending sequences
def flatten(dataset: list[str]) -> str:
    data_flat = [ [word + "</w>" for word in sentence.split(" ")] for sentence in dataset]
    data_flat = "".join([ word for sentence in data_flat for word in sentence ])
    return data_flat

# Count frequencies in a string or a list of strings
def frequencies(patterns: list[str] | set[str], data: str | list[str]) -> dict:
    freq = dict.fromkeys(patterns, 0)
    for pattern in patterns:
       freq[pattern] += data.count(pattern)
    return freq

def huffman_encoding(data: str):






