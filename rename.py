import os

os.chdir('/Users/sahilsharma/Desktop/Demo')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if f_name != '.DS_Store' and f_name != 'rename':
        f_title, f_num = f_name.split(' ')

        new_name = '{} {}'.format(f_num, f_title)
        print(new_name)
        os.rename(f, new_name)
