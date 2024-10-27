team1_num = 5 #количество участников первой команды
team2_num = 6 #количество участников в обеих командах
score1 = 40 #количество задач решённых командой1
score2 = 42 #количество задач решённых командой2
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2 #количество решённых задач по командам
time_avg = (team1_time + team2_time)/(tasks_total)
challenge_result = 'Победа команды Волшебники данных!' #исход соревнования
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print("В команде Мастера кода участников:%s !" % team1_num)
print("Итого сегодня в командах участников:%s и %s !" %(team1_num, team2_num))
print("Команда Волшебники данных решила задачи: {} !".format(score2))
print("Волшебники данных решили задачи за {} с !".format(team2_time))
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')