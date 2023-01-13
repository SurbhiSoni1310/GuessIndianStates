from turtle import Screen
import pandas
from score_board import ScoreBoard

from label import Label
board = ScoreBoard()
data = pandas.read_csv("data.csv")
row = data.state
list_of_states = row.to_list()
s = Screen()
s.title("Indian States Quiz")
s.setup(850, 850)
s.bgpic("india.gif")
while board.score != len(list_of_states):
    answer = s.textinput("State", "Write the name of the state\nClick cancel if you don't know further")
    if answer is None:
        break
    answer = answer.title()
    if answer in list_of_states:
        list_of_states.remove(answer)
        x = data[data.state == answer].x.to_list()[0]
        y = data[data.state == answer].y.to_list()[0]
        position = (x, y)
        tag = Label(position, answer)
        board.upgrade()

for i in list_of_states:
    x = data[data.state == i].x.to_list()[0]
    y = data[data.state == i].y.to_list()[0]
    position = (x, y)
    tag = Label(position, i)

s.exitonclick()
