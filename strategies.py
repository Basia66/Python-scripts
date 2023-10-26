import itertools
import numpy as np


def index_to_val(index):
    if index == 0:
        return 15
    if index == 1:
        return 20
    if index == 2:
        return 30


losses = [[1, 2, 3],
          [5, 2, 3],
          [7, 6, 3]]

# losses = [[1, 2, 3],
#           [1, 2, 3],
#           [1, 2, 3]]

frequency_of_responses = [[1/2, 1/2, 0, 0],
                          [0, 1/2, 1/2, 0],
                          [0, 0, 1/3, 2/3]]

# strategies
a = [0, 1, 2]
strategies = [p for p in itertools.product(a, repeat=4)]

print("\nStrategie:")
for i, strategy in enumerate(strategies):
    print(str(i+1) + " - " + str([index_to_val(x) for x in strategy]))

# liczenie action probabilities
action_probabilities = []
for strategy in strategies:
    tmp1 = []
    for f in frequency_of_responses:
        tmp = [0, 0, 0]
        i = 0
        for a in strategy:
            tmp[a] += f[i]
            i += 1
        tmp1.append(tmp)
    action_probabilities.append(tmp1)

# liczenie average losses dla action probabilities
average_losses = []
for action in action_probabilities:
    tmp = []
    for i, (loss, ac) in enumerate(zip(losses, action)):
        tmp.append(sum(np.array(loss)*np.array(ac)))
    average_losses.append(tmp)

# usuwanie strategii zdominowanych
to_remove = []
for i in range(len(average_losses)):
    for j in range(len(average_losses)):
        if i == j:
            continue
        if np.greater_equal(average_losses[j], average_losses[i]).all():
            to_remove.append(j)

tmp = list(np.array(average_losses))
to_remove = list(set(to_remove))
to_remove.sort(reverse=True)
for r in to_remove:
    del tmp[r]

# wypisanie strategii dopuszczalnych
print("\nStrategie dopuszczalne:")
indexes = []
for i in range(len(average_losses)):
    if i not in to_remove:
        print(str(i+1) + "->" + str(strategies[i]))
        indexes.append(i)

print("\nStrategie najlepsze:")
tmp1 = []
for i, x1 in enumerate(tmp):
    tmp1.append((indexes[i], max(x1)))

tmp2 = [tmp1[0]]
for i in tmp1:
    if i[1] < tmp2[0][1]:
        tmp2 = [i]
    elif i[1] == tmp2[0][1]:
        tmp2.append(i)

for i in set(tmp2):
    ampers = [index_to_val(x) for x in strategies[i[0]]]
    print("Strategia " + str(i[0]+1) + " -> " + str(ampers))
