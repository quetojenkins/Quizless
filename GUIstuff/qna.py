import random

def get_qnas(file_path):
    q = []
    a = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Iterate through the lines in the file
    i = 0
    while i < len(lines)-1:
        if lines[i].strip() == "#":
            # If a line contains "#", it's a question
            question = lines[i + 1].strip()
            q.append(question)
            i += 2  # Move to the next line for the answer
        else:
            # Otherwise, it's an answer
            answer = lines[i].strip()
            a.append(answer)
            i += 1  # Move to the next question or "#" line
    return q,a

def initialise(file_path):
    q,a = get_qnas(file_path)
    return q, a, [0 for _ in range(len(q))]

def correct(i,d):
    d[i] = 1
    return d

def get_next(q,a,d):
    r_num = random.randint(0, len(q)-1)
    found = False
    count = 0
    while found == False and count < len(q):
        if d[r_num] != 1: found = True
        else:
            count += 1
            if r_num == len(q) - 1:
                r_num = 0
            else:
                r_num += 1
    return wrap_text(q[r_num],50), wrap_text(a[r_num],50), r_num, found

def get_num_correct(d):
    count = 0
    for element in d:
        if element == 1:
            count += 1
    return count, len(d)


def wrap_text(text, line_length):
    wrapped_text = ""
    remaining_text = text

    while len(remaining_text) > line_length:
        # Find the last space within the line_length
        last_space = remaining_text.rfind(" ", 0, line_length)

        if last_space == -1:
            # If there's no space within the line_length, add a newline character at line_length
            last_space = line_length

        wrapped_text += remaining_text[:last_space] + "\n"
        remaining_text = remaining_text[last_space + 1:]

    wrapped_text += remaining_text  # Add the remaining text
    return wrapped_text

if __name__ == '__main__':
    q,a,d = initialise("FileHandeling Section/qnas/example.txt")
    found = True
    while found == True:
        ques, ans, num, found = get_next(q,a,d)
        correct(num,d)
        print(ques)
        print(ans)
    print(wrap_text("This is a long text that we want to wrap around to fit within a fixed line length.",20))
