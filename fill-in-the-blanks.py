# easy; empty fill-in-the-blank and its corresponding answers.
easy_fib = ["We're off to see the", "___1___", "The wonderful",
            "___2___", "of Oz, we", "___3___", "we hear he is a ",
            "___4___", "of a wiz, If there ever was If",
            "___5___", ", oh ever there was "
            "your life!"]
easy_answers = ["wizard", "wizard", "hear", "whiz", "ever"]

# medium; empty fill-in-the-blank and its corresponding answers.
medium_fib = ["The wizard of ", "___1___", "is one", "___2___", "___3___",
            "___4___", "___5___", "Because of the,", "___6___",
            "thing he does.", "We're off to see the, The Wonderful", "___7___",
            "of Oz!"]
medium_answers = ["oz", "because", "because", "because", "because",
            "wonderful", "wizard"]

# hard; empty fill-in-the-blank and its corresponding answers.
hard_fib = ["Follow the", "___1___", "___2___", " the ", "___3___",
            "Follow the", "___4___", "who", "___5___", "a", "___6___",
            "Follow follow follow follow follow " "___7___", "___8___",
            "brick road!"]
hard_answers = ["rainbow", "over", "stream", "fellow", "follows", "dream",
            "the", "yellow"]


def load_fib_difficulty():
    """Asks the user for a difficulty level and loads that difficulty.

    Args:
        none.
    Returns:
        (list of str): empty fill-in-the-blank.
        (list of str): answer key.
        (str): difficulty level.
    """
    level = raw_input("\nPlease select a difficulty level for Wizard of Oz "
                      "fill-in-the-blank quiz (easy, medium, or hard): ")
    if level.lower() == "easy":
        return easy_fib, easy_answers, "easy"
    if level.lower() == "medium":
        return medium_fib, medium_answers, "medium"
    if level.lower() == "hard":
        return hard_fib, hard_answers, "hard"
    else:
        print "You didn't select difficulty level! Try Again"
        return load_fib_difficulty()


def remove_spaces_before_punc(fib_string):
    """Removes spaces before punctuation.

    Removes the spaces after blanks and before punctuation (i.e. ___n___ .)
    that are created by " ".join(fib).

    Args:
        fib_string (str): the concatenated fill-in-the-blank with the unwanted
        spaces.
    Returns:
        (str): the same string without the unwanted spaces.
    """
    fib_string = fib_string.replace(" .", ".")
    fib_string = fib_string.replace(" !", "!")
    return fib_string


def provide_link(level):
    """Provides a link to the video of the home run call.

    Args:
        level (str): the chosen difficulty level.
    Returns:
        (str): the home run video link.
    """
    if level == "easy":
        return "https://www.youtube.com/watch?v=Mm3ypbAbLJ8"
    if level == "medium":
        return "https://www.youtube.com/watch?v=Mm3ypbAbLJ8"
    if level == "hard":
        return ("https://www.youtube.com/watch?v=Mm3ypbAbLJ8")


def guess_check(blank_number, fib, answers, answer):
    """Asks the user for a guess. If correct, moves to the next fill-in-the-blank.
    Args:
        blank_number (int): the current blank number.
        fib (list of str): the fill-in-the-blank in its current state.
        answers (list of str): the answer key.
        answer (str): the answer to the current blank.
    Returns:
        (int): the next blank number.
    """
    blank = "___" + str(blank_number) + "___"
    guess = raw_input("Please fill in blank #" + str(blank_number) +
                      " (case-sensitive): ")
    if guess == answer:
        fib[fib.index(blank)] = answer
        print remove_spaces_before_punc(" ".join(fib)) + "\n"
        blank_number += 1
        return blank_number
    else:
        print "Incorrect. Please try again.\n"
        return guess_check(blank_number, fib, answers, answer)


def play_game():
    """Plays a game of fill-in-the-blanks.
    Displays the chosen difficulty. Game ends with a printed
    youtube address of the wizard of oz song.
    Args:
        none.
    Returns:
        none.
    """
    fib, answers, level = load_fib_difficulty()
    print ("\nHere is the fill-in-the-blank for the " + level + " difficulty "
           "level:")
    print remove_spaces_before_punc(" ".join(fib)) + "\n"

    blank_number = 1
    for answer in answers:
        blank_number = guess_check(blank_number, fib, answers, answer)

    print ("Congratulations, always follow the yellow brick road!"
           " link to the call:")
    print provide_link(level) + "\n"

play_game()
