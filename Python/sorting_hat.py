Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Wrong input')

print('==================')

print("Q2) When I’m dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    Hufflepuff += 2
elif answer == 2:
    Slytherin += 2
elif answer == 3:
    Ravenclaw += 2
elif answer == 4:
    Gryffindor += 2
else:
    print('Wrong input')
print('==================')

print("Q3) Which kind of instrument most pleases your ear?")

print('  1) The Violin')
print('  2) The Trumpet')
print('  3) The Piano')
print('  4) The Drum')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    Slytherin += 4
elif answer == 2:
    Hufflepuff += 2
elif answer == 3:
    Ravenclaw += 4
elif answer == 4:
    Gryffindor += 4
else:
    print('Wrong input')

max_points = max(Gryffindor,Ravenclaw,Hufflepuff,Slytherin)

if Gryffindor == max_points:
    print('🦁 Gryffindor')
elif Ravenclaw == max_points:
    print('🦅 Ravenclaw')
elif Hufflepuff == max_points:
    print('🦡 Hufflepuff')
elif Slytherin == max_points:
    print('🐍 Slytherin')
else:
    print('Wrong input')
