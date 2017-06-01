def read_file(changes_file):
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            details = data[index + 1].split('|')
            #creating a dictionary for elements
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip().split(' ')[0],
                'hour': details[2].strip().split(' ')[1].split(':')[0],
                'timezone': details[2].strip().split(' ')[2],
                'weekday':details[2].strip().split(' ')[3][1:-1],
                'number_of_lines': details[3].strip().split(' ')[0]
            }
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits
