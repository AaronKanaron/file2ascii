import math


array = [[" ", 0], [".", 8], [":", 16], ["^", 20], ["~", 25], ["!", 30], ["7", 37], ["?", 44], ["J", 50], ["Y", 55], ["5", 60], ["P", 68], ["G", 75], ["B", 80], ["&", 86], ["#", 90], ["@", 100]]

# if Lumen <= i[in][1]

lumen = 120

def incremental(arr):
    val = ""    
    def to_percent(num, total):
        return (num/100)*total

    for i in range(len(arr)):
        if lumen >= to_percent(arr[i][1], 255): val = arr[i][0]
    return val

chars = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", "."]

# chars = [" ", ".", "'", "`", "^", "\"", ",", ":", ";", "I", "l", "!", "i", ">", "<", "~", "+", "_", "-", "?", "]", "[", "}", "{", "1", ")", "(", "|", "/", "t", "f", "j", "r", "x", "n", "u", "v", "c", "z", "X", "Y", "U", "J", "C", "L", "Q", "0", "O", "Z", "m", "w", "q", "p", "d", "b", "k", "h", "a", "o", "*", "#", "M", "W", "&", "8", "%", "B", "@", "$"]

def gen_code(arr):
    max = 255
    each = max / len(chars)
    for idx, i in enumerate(chars):
        print(f'elif lumin <= {math.floor(each * idx)}: result += "{i}"')


gen_code(chars)
print(incremental(array))