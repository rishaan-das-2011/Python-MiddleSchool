"""
LESSON: 4.1 - Lists
TECHNIQUE 4: Strings as Lists
PRACTICE 2
"""

phrase = input("Enter a word or phrase (without spaces or punctuation): ")

done = True
palindrome = True
start = 0

# Find the last index in phrase
end = len(phrase) -1

while start < len(phrase):

    # Check whether the phrase's symbol at the start
    # is the same as the phrase's symbol at the end,
    # and set palindrome to False if it's not
    if phrase[start] != phrase[end]:
        palindrome = False
        break
    start += 1
    end -= 1

if palindrome:
    print("That is a palindrome!")
else:
    print("That is not a palindrome.")


# Turn in your Coding Exercise.
