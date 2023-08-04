def colorize(text,color):
    if type(color) is not str:
        raise TypeError("color is not str type")
    if type(color) is not str:
        raise TypeError("text is not str type")
    if color not in colors:
        raise ValueError("Unexceptable color name")

    print(f"{text} {color} colorful write")
try:
    colorize("hello","red")
    colorize("hello","blue")
except (TypeError,ValueError) as ex:
    print(ex)
    
        



