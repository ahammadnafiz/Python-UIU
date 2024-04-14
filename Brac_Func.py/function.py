# Task 1
def even_checker(num:int) -> str:
  if num%2==0:
    print("Even!!")
  else:
    print("Odd!!")

# Task 2 
def fibonacci(lim:int) ->int:
  a,b=0,1
  for i in range(lim + 1):
      print(a, end=' ')
      a,b=b,a+b
  print()

# Task 3
def foo_moo(n:int) ->str:
    if n % 2 == 0 and n % 3 == 0:
        print('FooMoo')
    elif n % 2 == 0:
        print('Foo')
    elif n % 3 == 0:
        print('Moo')
    else:
        print('Boo')

# Task 4
def function_name(string:str) ->str:
  upper = 0
  lower = 0
  for i in string:
    if i.isupper():
      upper += 1
    elif i.islower():
      lower += 1
  print(f"No. of Uppercase characters : {upper}")
  print(f"No. of Lowercase Characters: {lower}")

# Task 5
def calculate_tax(age,salary,job):
  job=job.lower()
  if age<18:
    tax=0
  elif job=="president":  
    tax=0
  elif salary<10000:
    tax=0
  elif salary<20000:
    tax=salary*0.05
  else:
    tax=salary*0.1
  print(tax)

# Task 6 
def function_name(days):
  years=days//365
  months=(days%365)//30
  remaining_days=(days%365)%30
  print(f"{years} years, {months} months and {remaining_days} days")

# Task 7
def show_palindrome(n):
    palindrome = ''
    
    for i in range(1, n + 1):
        palindrome += f"{i}"
    else:
        for j in range(n - 1, 0, -1):
            palindrome += f"{j}"
    print(palindrome)

# Task 8
def show_palindromic_triangle(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(' ',end=' ')
        for j in range(1, i + 1):
            print(j, end=' ')
        for j in range(i - 1, 0, -1):
            print(j, end=' ')
        print()

# Task 9
import math
def area_circumference_generator(r):
  area=math.pi*r**2
  circumference=2*math.pi*r  
  return (area,circumference)
  
# Task 10
def make_square(t):
    s, e = t
    return {k:v ** 2 for (k, v) in enumerate(range(s, e + 1), start=s)}

# Task 11 
def rem_duplicate(t):
    my_list = list(t)
    unique = []
    duplicate = []
    for i in my_list:
        if i not in unique:
            unique.append(i)
        else:
            duplicate.append(i)  
    return unique

# Task 12
def function_name(my_list):
    d = {}
    for i in my_list:
        d[i] = d.get(i, 0) + 1

    removed_count = 0
    new_list = []
    for k, v in d.items():
        if v > 2:
            removed_count += v - 2
            v = 2
        new_list.extend([k] * v)

    print(f"Removed: {removed_count}")
    return new_list

# Task 13
def calculator(operator, n1, n2):
    if operator =='+':
        return n1 + n2
    elif operator =='-':
        return n1 - n2
    elif operator =='*':
        return n1 * n2
    elif operator =='/':
        return n1 / n2
    else:
        return f"Invalid Operator"
  
# Task 14
def function_name(sentence, position):
    new_sentence = ''
    remove_word = ''
    for w in range(1, len(sentence)):
        if w % position == 0:
            remove_word += f"{sentence[w]}"
        else:
            new_sentence += f"{sentence[w]}"
    full = sentence[0] + new_sentence + f"{remove_word}"
    return full
  
# Task 15
def function_name(item_list, location = "Dhanmondi"):
    item_price = {
        'rice' : 105,
        'potato' : 20,
        'chicken' : 250,
        'beef' : 510,
        'oil' : 85
    }

    total_price = []
    for item, price in item_price.items():
        for i in item_list:
            if i == item:
                total_price.append(price)
    if location == "Dhanmondi":
        price = 30 + sum(total_price)
    else:
        price = 70 + sum(total_price)
    
    return price

# Task 16
def splitting_money(amount):
  notes = {500:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
  for key in sorted(notes, reverse=True):
    notes[key] = amount // key
    amount = amount % key
  return " ".join(f"{key} Taka: {notes[key]} note(s)" for key in notes)

# Task 17  
def remove_odd(lst):
  lst_even = [x for x in lst if x%2==0]
  print(lst_even)
  
# Task 18
def function_name(start, end, first_divisor, second_divisor):
    result = 0

    for i in range(start, end):
        if i % first_divisor == 0 and i % second_divisor == 0:
            result += 0
        elif i % first_divisor == 0 or i % second_divisor == 0:
            result += i
        else:
            result += 0

    print(result)
  
# Task 19
def function_name(string):
    test = 'abcdefghij'
    slist = ''.join(sorted(set([s for s in string.lower() if s != ' '])))
    print(slist)
    c = 0
    if all(letter in slist for letter in test):
        c = 5
    else:
        c = 6
    for i in range(c):
        print("PSG will win the Champions League this season")  
  
# Task 20  
def individul_bonus_calculation(player,yearly_earning,goals,percent):
  bonus = goals*(percent/100*yearly_earning)
  if goals>30:
    bonus+=10000
  elif 20<=goals<=30:
    bonus+=5000
  print(player,"earned a bonus of",bonus,"Taka for",goals,"goals.")
    
# Task 21
def cal_bonus(*args):
  for i in range(0,len(args),4):
    individul_bonus_calculation(args[i],args[i+1],args[i+2],args[i+3])
