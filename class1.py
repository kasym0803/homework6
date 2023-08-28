


class Hello:

    def __init__(self,name):
        self.name = name

class Hi(Hello):

    def __str__(self):
        return f'name:{self.name}'

from art import tprint

input_name = Hi('kasymbek')
tprint(input_name.name)
