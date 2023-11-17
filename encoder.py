
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

def binary_pair_encoder(data: str):
    data_dict = frequencies(set(data), data)
    last = False
    while last != data_dict:
        last = data_dict.copy()
        most_occuring = sorted(data_dict, key=data_dict.get, reverse=True)[:2]
        new_pattern = "".join(most_occuring)
        data_dict[new_pattern] = data.count(new_pattern)
        data_dict[most_occuring[0]] -= data_dict[new_pattern]
        data_dict[most_occuring[1]] -= data_dict[new_pattern]

    return {k:v for k,v in data_dict.items() if v}






