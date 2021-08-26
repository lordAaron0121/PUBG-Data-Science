# this is a context manager
with open('train.csv', 'r') as f:
    with open('train_2.txt', 'w') as w:
        for line in f:
            w.write(line)