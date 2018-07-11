import os
files = os.listdir('path/to/my/fixtures')
apps = ["util", "profiles", "problems", "ideas", "events"]


def traverse_fixtures():
    for app in apps:
        load_data()


def load_data(file):
    if os.path.splitext(file)[1] == '.json' and file != 'initial_data.json':
        print(file)
        os.system("python manage.py loaddata %s" % file)


map(load_data, files)