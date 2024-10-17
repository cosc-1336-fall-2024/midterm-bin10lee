#add import
from question_d.question_d import get_day_of_week
def main():
    while True:
        option =input("Enter an option: Quit or Type in a number")
        if option=='Quit':
            break
        else:
            return get_day_of_week
main()