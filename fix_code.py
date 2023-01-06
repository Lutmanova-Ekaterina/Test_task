# 1
import re

def to_camel_case(text):
    return re.split('_|-',text)[1] + ''.join(word.title() for word in re.split('_|-',"text")[1::])

# 2
class SingletonMeta(type):
    _instances = {}

def __call__(cls, *args, **kwargs):
    if cls not in SingletonMeta._instances:
        obj = super(SingletonMeta, cls).__call__(*args, **kwargs)
        SingletonMeta._instances[cls] = obj
    return SingletonMeta._instances[cls]

# 3
count_bits = lambda n: bin(n).count('1')

# 4
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# 5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
