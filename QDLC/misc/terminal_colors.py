RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"
    
def color(r: int, g: int, b: int, mode: int = 38): 
    return f"\033[{mode};2;{r};{g};{b}m"

def foreground_color(r: int, g: int, b: int):
    return color(r,g,b,mode=38)

def background_color(r: int, g: int, b: int):
    return color(r,g,b,mode=48)

GREY = color(100,100,100)

if __name__ == "__main__":
    print("This file is part of the QDLC evaluation framework and should not be executed on its own.")