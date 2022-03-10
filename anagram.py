def are_anagrams(s1, s2):
    s1 = input('Enter a word: ')
    s2 = input('Enter another word: ')
    if len(s1) != len(s2):
        print('They\'re not anagram!')
        return False
    freq1 = {}
    freq2 = {}
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            print('They\'re not anagram!')
            return False
    print('they\'re anagram')
    return True
