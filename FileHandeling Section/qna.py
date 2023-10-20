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

if __name__ == '__main__':
    q,a = get_qnas("main/qnas/example.txt")
    print(q)
    print(a)
    

