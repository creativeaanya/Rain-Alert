import turtle
import pandas

screen = turtle.Screen()
screen.title("Africa Countries Game")
image = "blank_countries_img.gif"
turtle.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("54_countries.csv")
all_countries = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 50:
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/54 Countries Correct",
                                      prompt="What's another country's name?").title()
    if answer_country == "Exit":
        missing_countries = []
        for country in all_countries:
            if country not in guessed_countries:
                missing_countries.append(country)
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        break
    if answer_country in all_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(country_data.x.item(), country_data.y.item())
        t.write(answer_country)

