import random
status = ['rock', 'scissors', 'paper']
nums = [1, 2, 3, 4, 5, 6]

def main():
   print(figure_guess())
   print(get_nums())

def figure_guess():
    return random.choice(status)

def get_nums():
    return random.choice(nums)

if __name__ == "__main__":
    main()

