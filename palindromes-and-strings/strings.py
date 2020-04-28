#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    res_data = []
    # check for string
    if pattern == "":
        return True

    for index in range(0, len(text)):
        if text[index] == pattern[0]:   # check if text character aligns with its' index
            store_index = index   
            for a in range(len(pattern)):
                if store_index > len(text) - 1 or pattern[a] != text[store_index]:
                    break
                if a == len(pattern) - 1:
                    res_data.append(index)
                store_index += 1
    return len(res_data) != 0

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    res_data = []
    # check for string
    if pattern == "":
        return 0
    
    for index in range(0, len(text)):
        if text[index] == pattern[0]:   # check if text character aligns with its' index
            store_index = index   
            for a in range(len(pattern)):
                if store_index > len(text) - 1 or pattern[a] != text[store_index]:
                    break
                if a == len(pattern) - 1:
                    return index
                
                store_index += 1
    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    res_data = []
    # check length
    length = len(text)
    
    for index in range(0, len(text)):
        if len(pattern) == 0:
            for a in range(0, len(text)):
                res_data.append(a)
            break
        if text[index] == pattern[0]: # if index of text starts at the beginnning
            store_index = index
            for a in range(len(pattern)):
                if store_index > len(text) - 1 or pattern[a] != text[store_index]:
                    break
                if a == len(pattern) - 1:
                    res_data.append(index)
                store_index += 1
    return res_data


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
