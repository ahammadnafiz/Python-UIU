num_of_colors = int(input('Enter the number of colors to classify: '))

red = (255, 0, 0)
blue = (0, 0, 255)

red_count = 0
blue_count = 0

for i in range(num_of_colors):
    print('Enter the RGB values for color 1 (0-255) for each channel: ')
    r = int(input('Red: '))
    g = int(input('Green: '))
    b = int(input('Blue: '))
    
    red_distance = ((red[0] - r) ** 2 + (red[1] - g) ** 2 + (red[2] - b) ** 2) ** 0.5
    blue_distance = ((blue[0] - r) ** 2 + (blue[1] - g) ** 2 + (blue[2] - b) ** 2) ** 0.5
    
    if red_distance < blue_distance:
        print(f'Color {i + 1} is Closer to Red.')
        red_count += 1
    elif blue_distance < red_distance:
        print(f'Color {i + 1} is Closer to Blue.')
        blue_count += 1
    else:
        print(f"Color {i +1 } is Equidistant from Red and Blue.")

print()
print(f"Total colors Closer to Red: {red_count}")
print(f"Total colors Closer to Blue: {blue_count}")



#Expalination
'''
Question er output e vul ache, ei calculation theke bujhba

Test Case 1:
Red: (250, 10, 5)
Blue: (0, 0, 255)

Euclidean distance to Red:
d = √[(250 - 255)² + (10 - 0)² + (5 - 0)²]
   = √[(-5)² + 10² + 5²]
   = √[25 + 100 + 25]
   = √150
   ≈ 12.25

Euclidean distance to Blue:
d = √[(250 - 0)² + (10 - 0)² + (5 - 255)²]
   = √[250² + 10² + (-250)²]
   = √[62500 + 100 + 62500]
   = √125200
   ≈ 353.55

Test Case 2:
Red: (100, 200, 100)
Blue: (0, 0, 255)

Euclidean distance to Red:
d = √[(100 - 255)² + (200 - 0)² + (100 - 0)²]
   = √[(-155)² + 200² + 100²]
   = √[24025 + 40000 + 10000]
   = √74025
   ≈ 272.09

Euclidean distance to Blue:
d = √[(100 - 0)² + (200 - 0)² + (100 - 255)²]
   = √[100² + 200² + (-155)²]
   = √[10000 + 40000 + 24025]
   = √74025
   ≈ 272.09

Test Case 3:
Red: (5, 5, 245)
Blue: (0, 0, 255)

Euclidean distance to Red:
d = √[(5 - 255)² + (5 - 0)² + (245 - 0)²]
   = √[(-250)² + 5² + 245²]
   = √[62500 + 25 + 60025]
   = √122550
   ≈ 350.43

Euclidean distance to Blue:
d = √[(5 - 0)² + (5 - 0)² + (245 - 255)²]
   = √[5² + 5² + (-10)²]
   = √[25 + 25 + 100]
   = √150
   ≈ 12.25

So, the calculated distances for the three test cases are as follows:

Test Case 1:
Distance to Red: 12.25
Distance to Blue: 353.55

Test Case 2:
Distance to Red: 272.09
Distance to Blue: 272.09 

Test case 2 tai same so red count 2 ta howa possible nah
tai Equidistant from Red and Blue

Test Case 3:
Distance to Red: 350.43
Distance to Blue: 12.25
'''