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
    return q[r_num], a[r_num], r_num, found

if __name__ == '__main__':
    q,a,d = initialise("FileHandeling Section/qnas/example.txt")
    found = True
    while found == True:
        ques, ans, num, found = get_next(q,a,d)
        correct(num,d)
        print(ques)
        print(ans)
