'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    count = 0

    if not word or len(word) < 2:
        return 0
    else:
        if list(word)[0] == 't' and list(word)[1] == 'h':
            count += 1
        return count + count_th(word[1:])

# string = 'ththththththththththththththth'
# print(count_th(string))

    # pass
