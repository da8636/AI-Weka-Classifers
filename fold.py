with open('pima.csv') as pima:
    pima_list = []
    for line in pima:
        pima_list.append(line.strip().split(','))

    class_yes = []
    class_no = []
    for line in pima_list:
        if line[-1] == "yes":
            class_yes.append(line)
        elif line[-1] == "no":
            class_no.append(line)

    results = [[] for i in range(10)]

    # print("Len of Y - {}".format(len(class_yes)))
    # print("Len of X - {}".format(len(class_no)))

    div_yes = len(class_yes) // 10
    div_no = len(class_no) // 10
    for i in range(10):
        for x in range(div_yes):
            results[i].append(class_yes.pop())

    for i in range(10):
        for x in range(div_no):
            results[i].append(class_no.pop())
    for i in range(8):
        results[i].append(class_yes.pop())

    fold = 0
    while (fold < 10):
        print("fold{}".format(fold+1))
        for line in results[fold]:
            print(",".join(line))
        fold += 1
        print()
