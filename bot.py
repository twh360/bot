import os
from datetime import date


d = str(date(2020, 6, 2))
with open('bot.txt', 'a') as file:
    file.write(d+'\n')
os.system('git add bot.txt')
os.system('git commit --date="' + d + '" -m "first commit from twh"')

## push the commit to github
os.system('git push -u origin main')