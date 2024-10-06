
alien_0 = {'color':'green','points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])


alien_0['x_position']=0
alien_0['y_position']=25

print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points']=5
print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

#tracking the position of alient that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#move the alien to the right
#determine how far the alien based on its current speed
if alien_0['speed']=='slow':
    x_increment = 1
elif alien_0['speed']=='medium':
    x_increment = 2
else:
    x_increment = 3

#the new position is the old position plus the increment
alien_0['x_position']=alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#removing a key value 
alien_0={'color': 'green','points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#storing different kind of informations about one object
favorite_languages = {'jen': 'Python',
                      'sarah': 'c',
                      'edward': 'rust',
                      'phil': 'python',}
language= favorite_languages['sarah'].title()
print(f"Sarah's favorite_language is {language}.")

