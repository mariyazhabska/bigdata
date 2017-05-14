from pprint import pprint

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

def get_authors(commits):
    authors = {}
    for commit in commits:
        author = commit['author']
        if author not in authors:
            authors[author] = 1
        else:
            authors[author] = authors[author] + 1
    return authors
    
#function to get commits per calendar date     
def get_dates(commits):
    dates = {}
    for commit in commits:
        date = commit['date']
        if date not in dates:
            dates[date] = 1
        else:
            dates[date] =  dates[date]+1
    return dates

#function to get the number of commits per timezone    
def get_timezones(commits):
    timezones = {}
    for commit in commits:
        timezone = commit ['timezone']
        if timezone not in timezones:
            timezones[timezone] = 1
        else:
            timezones[timezone] = timezones[timezone]+1
    return timezones

#function to get number of commits per weekday     
def get_weekday(commits):
    weekdays = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(commits)):
      commit = commits[i]
      weekday = commit['weekday']
      if weekday == 'Mon':
        weekdays[0] = weekdays[0] + 1
      elif weekday == 'Tue':
        weekdays[1] = weekdays[1] + 1
      elif weekday == 'Wed':
        weekdays[2] = weekdays[2] + 1
      elif weekday == 'Thu':
        weekdays[3] = weekdays[3] + 1
      elif weekday == 'Fri':
        weekdays[4] = weekdays[4] + 1
      elif weekday == 'Sat':
        weekdays[5] = weekdays[5] + 1
      elif weekday == 'Sun':
        weekdays[6] = weekdays[6] + 1
      else:
        print("Bad day " + weekday + " in commit number " + str(i))
    return weekdays

#function to get number of commits per hour
def get_hours(commits):
    hours = [0] * 24
    for commit in commits:
        hour = int(commit['hour'])
        if hour >= 0 and hour < 24: 
            hours[hour] = hours[hour] + 1
        else:
            raise ValueError
    return hours

#getting average number of comment lines per author
def get_avg_lines(commits):
    commit_data = {}
    for commit in commits:
        author = commit['author']
        if author not in commit_data:
            commit_data[author] = [0, 0]
        number_of_lines = int(commit['number_of_lines'])
        commit_data[author][0] = commit_data[author][0] + 1
        commit_data[author][1] = commit_data[author][1] + number_of_lines
    average_lines = {}
    for author in commit_data:
        average_lines[author] = float(commit_data[author][1])/commit_data[author][0]
    return average_lines

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log.txt'
    data = read_file(changes_file)
    commits = get_commits(data)

    #print commits per author
    pprint (get_authors(commits))
    
    #print commits per timezone
    print get_timezones(commits)
    
    #print average lines per author
    avg_lines = get_avg_lines(commits)
    for author in avg_lines:
        print(author + ": " + str(round(avg_lines[author], 1)))
    
    #print commits per hour
    commits_per_hour = get_hours(commits)
    for hour in range(24):
        print(str(hour) + ": " + str(commits_per_hour[hour]))
    
    #print commits per weekday
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    commits_per_day = get_weekday(commits)
    for day in range(len(days)):
        print(days[day] + ': ' + str(commits_per_day[day]))
        
    #print commits per calendar dates
    pprint (get_dates(commits))
    
   
