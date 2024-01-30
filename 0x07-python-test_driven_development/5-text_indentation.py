#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Validate text input
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize flag to track if a newline is needed
    new_line_needed = False

    # Iterate through each character in the text
    for char in text:
        # Check if the character is one of ., ? or :
        if char in [".", "?", ":"]:
            # Print a newline and update the flag
            print("\n\n", end="")
            new_line_needed = False
        else:
            # Print the character without leading or trailing spaces
            if char != " " or not new_line_needed:
                print(char, end="")
            # Update the flag if a space is encountered
            if char == " ":
                new_line_needed = True
