def flames(male, female):
    # male = request.query['male']
    # female = request.query['female']
    full_form = {'F': 'Friends', 'L': 'Love', 'A': 'Affection',
                 'M': 'Marriage', 'E': 'Enemy', 'S': 'Sister'}

    flame = ['F', 'L', 'A', 'M', 'E', 'S']

    male_list = [x.lower() for x in male if not x == ' ']
    female_list = [x.lower() for x in female if not x == ' ']
    male_iter = iter(male)

    for letter in male_iter:
        if letter in female_list:
            male_list.pop(male_list.index(letter))
            female_list.pop(female_list.index(letter))

    total_length = len(male_list) + len(female_list)

    # print('male : ', male_list)
    # print('female : ', female_list)
    # print('len : ', total_length)

    while len(flame) > 1:
        outindex = (total_length % len(flame)) - 1
        _not = flame.pop(outindex)

        if outindex < 0:
            flame = flame[0:]
        else:
            flame = flame[(outindex):] + flame[0:outindex]

    return full_form[flame[0]]