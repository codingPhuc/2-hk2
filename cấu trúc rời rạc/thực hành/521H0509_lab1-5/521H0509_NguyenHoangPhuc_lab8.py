# Ex1
Andersen = {
    "The Emperor's New Clothes",
    "The Little Mermaid",
    "The Little Match Girl",
    "The SnowQueen",
}

# Ex2
Shakespeare = {
    "Romeo and Juliet",
    "Hamlet",
    "King Lear",
    "Macbeth",
    "A Midsummer Night's Dream",
    "A Comedy of Errors",
}


# Ex3
Tragedy = {
    "Medea",
    "Octavia",
    "Oedipus",
    "Ur-Hamlet",
    "Romeo and Juliet",
    "Hamlet",
    "King Lear",
    "Macbeth",
}
Comedy = {
    "The Three Musketeer",
    "The Clouds",
    "A Midsummer Night's Dream",
    "A Comedy of Errors",
}
Uncategory = {
    "Don Quixote", 
    "Rapunzel",
    "Cinderella", 
    *Andersen}


# Shakespeare_Tragedy = Shakespeare.difference(Comedy)
# giao n (in python &)
# Andersen_Comedy = Andersen.intersection(Comedy)
# hop u (in python |)

# Ex4 
Shakespeare_Tragedy = Shakespeare - Comedy

# Ex5
Andersen_Comedy = Andersen & Comedy


# Ex6
# isdisjoint Return True if no items in set x is present in set y
# issubset Return True if all items in set x are present in set y
def issubset(A, B):
    for a in A:
        if a not in B:
            return False
    return True

def isdisjoint(A, B):
    return not issubset(A, B)

def issuperset(A, B):
    for b in B:
        if b not in A:
            return False
    return True

def getNameVariable(variable):
    for name in globals():
        if eval(name) == variable:
            return name

def relationship():
    authors = [Andersen_Comedy, Shakespeare_Tragedy]
    works = [Andersen, Shakespeare, Tragedy, Comedy, Uncategory]
    for author in authors:
        for work in works:
            print(
                getNameVariable(author),
                "issubnet",
                getNameVariable(work),
                "is",
                author.issubset(work),
            )
            print(
                getNameVariable(author),
                "issuperset",
                getNameVariable(work),
                "is",
                author.issuperset(work),
            )
            print(
                getNameVariable(author),
                "isdisjoint",
                getNameVariable(work),
                "is",
                author.isdisjoint(work),
            )
            print("")

        print("\n")


# Ex7
Work = Andersen | Tragedy | Comedy | Uncategory


# Ex8
Author = {"Shakespeare", "Andersen", "Unknown"}


# Ex9
def gAuthor(work):
    if work in Andersen:
        return "Andersen"
    if work in Shakespeare:
        return "Shakespeare"
    return "Unknown"


Author_Of = {w: gAuthor(w) for w in Work}
# print(Author_Of)

# Ex10
def writen_by():
    result = {}
    for work, author in Author_Of.items():
        if result.get(author) == None:
            result[author] = [work]
        else:
            result[author].append(work)
        # print(work, author)
    # print(result)
    return result


Writen_By = writen_by()
# print(Writen_By)

# ex11
Work_Count = len(Work)
# print("Work_Count: ", Work_Count)

# ex12
questions = [
    """Han Christian Andersen is famous for fairy tales such as: "The Emperor's New Clothes", "The Little Mermaid", "The Little Match Girl", "The Snow Queen". Create a set in Python named Andersen and put his fairy tales' names as elements.""",
    """Shakespeare is mostly famous for his tragedies such as: "Romeo and Juliet", "Hamlet", "King Lear", "Macbeth". Meanwhile, he also wrote comedies such as: "A Midsummer Night's Dream" and "A Comedy of Errors". Create a set in Python named Shakespeare and put his plays names as elements.""",
    """Given the tragedies such as: "Medea", "Octavia", "Oedipus", "Ur-Hamlet". Comedies such as: "The Three Musketeer", "The Clouds". Meanwhile there are some stories that is hard to put in either comedies or tragedies such as: "Don Quixote", "Rapunzel", "Cinderella". Create 3 sets named Tragedy, Comedy and Uncategory then put the above works', included Andersen and Shakespeare's works, names in the right categories.""",
    """Create a set named Shakespeare_Tragedy by taking the difference of 2 related sets""",
    """Create a set named Andersen_Comedy by taking the intersection of 2 related sets""",
    """Determine the relationship of Andersen_Comedy and Shakespeare_Tragedy with Shakespeare, Andersen, Tragedy, Comedy, and Uncategory set. The relations needed to be test is: issubset, issuperset, isdisjoint.""",
    """Create a set named Work by combine all the above set""",
    """Create a set named Author taking authors' names and 'Unknown' as it's elements.""",
    """Using python Dict named Author_Of to represent the relation between Work and Author. Which mean, print(Author_Of['Hamlet']) should print Shakespeare.""",
    """Using python Dict named Writen_By to represent the invert relation of Author_Of.""",
    """Using python Dict named Work_Count to count how many sets each Work appeared.""",
    """Within the content of Exercise section count how many words are in this section of the Lab.""",
    """Count how many times each words appeared and sorted the word by number of times they appeared descending.""",
]


def countWordInQuestion():
    result = {}
    i = 1
    total = 0 
    for question in questions:
        result["Question " + str(i)] = len(
            question.replace('"', "").replace("' ", "").replace(".", "").split(" ")
        )
        i += 1
        total += len(
            question.replace('"', "").replace("' ", "").replace(".", "").split(" ")
        )
    result["Total: "] = total
    return result


Section_Count = countWordInQuestion()
# print(Section_Count)

# ex13
def sortByTime(input):
    return input[1]


def timeEachWord():
    result = {}
    i = 1
    for question in questions:
        # section = {word for word in question.split(" ")}
        sections = {}
        for word in (
            question.replace('"', "").replace("' ", "").replace(".", "").split(" ")
        ):
            if sections.get(word) == None:
                sections[word] = 1
            else:
                sections[word] += 1
        result["Question " + str(i)] = [section for section in sections.items()]
        i += 1

    for r in result.items():
        # r[1] = []
        r[1].sort(reverse=True, key=sortByTime)
        # print(type(r[1]))
        # print((r[1]))
    return result


def timeEachWordAll():
    result = {}
    for question in questions:
        for word in (
            question.replace('"', "").replace("' ", "").replace(".", "").split(" ")
        ):
            if result.get(word) == None:
                result[word] = 1
            else:
                result[word] += 1

    result = [r for r in result.items()]
    result.sort(reverse=True, key=sortByTime)
    return result


Time_Each_Word = timeEachWord()
Time_Each_Word_ALL = timeEachWordAll()

# for e in Time_Each_Word.items():
#     print("Time_Each_Word in", e[0], ":")
#     for pair in e[1]:
#         print("\t", pair)
# print("Time_Each_Word:")
# for e in Time_Each_Word_ALL:
#     print("\t", e)

# main
if __name__ == "__main__":
    # ex1
    print("=" * 10)
    print("Exericises 1".upper())
    print("Andersen", Andersen)

    # ex2
    print("=" * 10)
    print("Exericises 2".upper())
    print("Shakespeare", Shakespeare)

    # ex3
    print("=" * 10)
    print("Exericises 3".upper())
    print("Tragedy", Tragedy)
    print("Comedy", Comedy)
    print("Uncategory", Uncategory)

    # ex4
    print("=" * 10)
    print("Exericises 4".upper())
    print("Shakespeare_Tragedy", Shakespeare_Tragedy)

    # ex5
    print("=" * 10)
    print("Exericises 5".upper())
    print("Andersen_Comedy", Andersen_Comedy)

    # ex6
    print("=" * 10)
    print("Exericises 6".upper())
    relationship()

    # ex7
    print("=" * 10)
    print("Exericises 7".upper())
    print("Work", Work)

    # ex8
    print("=" * 10)
    print("Exericises 8".upper())
    print("Author", Author)

    # ex9
    print("=" * 10)
    print("Exericises 9".upper())
    for e in Author_Of.items():
        print("Author_Of", e[0], "is", e[1])

    # ex10
    print("=" * 10)
    print("Exericises 10".upper())
    for e in Writen_By.items():
        print("Writen_By", e[0], "is", e[1])

    # ex11
    print("=" * 10)
    print("Exericises 11".upper())
    Work_Count = len(Work)
    print("Work_Count", Work_Count)
    # Work_Count = 4
    # print("Work_Count", Work_Count)

    # ex12
    print("=" * 10)
    print("Exericises 12".upper())
    for e in Section_Count.items():
        print("Section count in", e[0], "is", e[1])

    # ex13
    print("=" * 10)
    print("Exericises 13".upper())
    for e in Time_Each_Word.items():
        print("Time_Each_Word in", e[0], ":")
        for pair in e[1]:
            print("\t", pair)
    print("Time_Each_Word:")
    for e in Time_Each_Word_ALL:
        print("\t", e)

