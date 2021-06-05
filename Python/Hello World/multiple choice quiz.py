
class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions_colors = [
    "What color are apples?\n(a)Red\n(b)Orange\n(c)Black\n\n",
    "What color are bananas?\n(a)Pink\n(b)Yellow\n(c)Magenta\n\n",
    "What color are strawberries?\n(a)Blue\n(b)Red\n(c)Violet\n\n"
]

questions_ans = [
    Questions(questions_colors[0], "a"),
    Questions(questions_colors[1], "b"),
    Questions(questions_colors[2], "b")
]


def run_test(question):
    score = 0
    for question in questions_ans:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    print("You scored " + str(score) + " out of " + str(len(questions_ans)))
    print("You scored " + str(score) + " out of " + str(len(questions_ans)))


run_test(questions_ans)
