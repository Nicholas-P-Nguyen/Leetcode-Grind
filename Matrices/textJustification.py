def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    output = []
    currentLine = []
    # Length of current line without the spaces
    length = 0
    i = 0

    while i < len(words):
        # Line is complete, compute the extra space and distribute it 
        if length + len(currentLine) + len(words[i]) > maxWidth:

            # How much extra space there are 
            extraSpace = maxWidth - length
            # How much space between each word excluding the last word. Get the max so we never divide by 1
            spacesBetween = extraSpace // max(1, len(currentLine) - 1)
            # If the spaces between are not equal we favor the left side
            remainder = extraSpace % max(1, len(currentLine) - 1)

            # Add the spaces to the words in current line, excluding last word
            for j in range(max(1, len(currentLine) - 1)):
                currentLine[j] += " " * spacesBetween
                    # If there is a remainder we favor left side, and decrement remainder
                if remainder:
                    currentLine[j] += " "
                    remainder -= 1

            output.append("".join(currentLine))
            # Reset currentLine and length 
            currentLine = []
            length = 0

        # Line is not complete, so we append to currentLine, increase length, and increment i
        currentLine.append(words[i])
        length += len(words[i])
        i += 1
    
    # Handle last line because, last line be less than maxWidth, so it won't enter if statement
        
    # add a space inbetween each word, excluding the last word
    lastLine = " ".join(currentLine)
    trailingSpace = maxWidth - len(lastLine)
    output.append(lastLine + " " * trailingSpace)

    return output