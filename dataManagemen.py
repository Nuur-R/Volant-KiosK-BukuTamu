def log(name, time, date, status):
    with open('data/log.csv', 'a') as f:
        if (name != 'unknown'):
            f.writelines(f'\n{name},{time},{date},{status}')