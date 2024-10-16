"""
File: PR07_DataArray.py
Requirements: See PT07_DataArray
"""

# Additional quotations can be found https://sourceforge.net/projects/mightymaxims
def load_data():
    return (
        "George Bernard Shaw|You can not believe in honor until you have achieved it. Better keep yourself clean and bright; you are the window through which you must see the world.",
        "Gilbert Keith Chesterton|Those thinkers who cannot believe in any gods often assert that the love of humanity would be in itself sufficient for them; and so, perhaps, it would, if they had it.",
        "Brian Tracy|You cannot control what happens to you, but you can control your attitude toward what happens to you, and in that, you will be mastering change rather than allowing it to master you.",
        "Johann Wolfgang Von Goethe|When all is said the greatest action is to limit and isolate one's self.",
        "Malcolm S. Forbes|The biggest mistake people make in life is not trying to make a living at doing what they most enjoy.",
        "Isadora Duncan|What one has not experienced one will never understand in print.",
        "Sri Ramakrishna|So long as the bee is outside the petals of the lily, and has not tasted the sweetness of its honey, it hovers around the flower emitting the buzzing sound; but when it is inside the flower, it noiselessly drinks the nectar. So long as a man quarrels and disputes about doctrines and dogmas, he has not tasted the nectar of true faith; when he has tasted it, he becomes quiet and full of peace.",
        "Author Unknown|Young men, and old men too, should learn the truth that the only real, lasting pleasure in life comes from being actively busy at some work every day; doing something worth while, and doing it as well as you know how. The more we appreciate this fact, the more will we be able to make the most of our lives.",
        "Ralph Waldo Emerson|Without a rich heart, wealth is an ugly beggar.",
        "G. Randolf|Truly great friends are hard to find, difficult to leave, and impossible to forget.",
        "Richard Baker|To get rich never risk your health. For it is the truth that health is the wealth of wealth.",
        "Rogers|The good are better made by ill, As odors crush'd are sweeter still.",
        "Johann Wolfgang Von Goethe|What by a straight path cannot be reached by crooked ways is never won.",
        "Mohammed|Patience is the key to contentment.",
        "Arnold Bennett|You wake up in the morning, and your purse is magically filled with twenty-four hours of un-manufactured tissue of the universe of your life! It is yours. It is the most precious of possessions. No one can take it from you. And no one receives either more or less than you receive.",
        "Isaac B. Singer|When you betray somebody else, you also betray yourself.",
        "St. Gregory The Great|The universe is not rich enough to buy the vote of an honest man.",
        "Reverend Theodore M. Hesburgh|The most important thing a father can do for his children is to love their mother.",
        "Vince Lombardi|The spirit, the will to win, and the will to excel are the things that endure. These qualities are so much more important than the events that occur.",
        "Ralph Marston|There are very real obstacles and challenges to any course of action. And there's no need to add to them, by making up obstacles of your own. Unchain yourself from the bondage of your own thinking.",
        "Pythagoras|Wisdom thoroughly learned will never be forgotten.",
    )


# TODO: Create a dictionary (see instructions for more information)
def parse_data(data):
    pass


# Data loading / access test ...
for ss, line in enumerate(load_data(), 1):
    print(ss, line)