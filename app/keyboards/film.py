from aiogram.utils.keyboard import InlineKeyboardBuilder

def build_films_keyboard(films: list):
    builder = InlineKeyboardBuilder()
    for index, film in enumerate(films):
        builder.button(text=film.get('title'),
                       callback_data=f"film_{index}")
    return builder.as_markup()

def build_film_details_keyboard(url):
    builder = InlineKeyboardBuilder()
    builder.button(text="Перейти за посиланням", url=url)
    builder.button(text="Перейти до меню", callback_data="back")
    builder.button(text="Перейти назад", callback_data="back")
    return builder.as_markup()

def build_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Опитування", callback_data=f"films")
    builder.button(text="Калькулятор переробника", callback_data=f"filmcreate")
    builder.button(text="Калькулятор рейду", callback_data=f"filmcreate")
    builder.button(text="Пітдримка", callback_data=f"filmcreate")
    return builder.as_markup()
