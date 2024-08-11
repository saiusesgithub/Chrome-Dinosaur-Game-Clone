# Dinosaur Game Clone

### Description:

#### About the Project

Clone of the classic Google Chrome Dinosaur game 

> made using pygame

The Google Dinosaur game probably doesn't need any explanation.
~~but gonna explain it anyway~~.
 Everyone has been there atleast once when their internet wasn't working

Basically, you are a dinosaur and you can jump and crouch to avoid the obstacles(cacti and birds)and the player score shows how long you have survived along with the previous high score.


> Explanation of code:

**project.py** is the main file which contains most of the code.

Here are some of the functions explained - 

1) **the collision function** checks if there is a collision between the player and obstacle and returns true or false which is assigned to **game_active** variable.

2) **Display score function** : 
current_time gets the time from the initialisation of python
so if a new game has been started, the start_time is subtracted from current_time so it starts from zero again

3) **Obstacle movement function** :
randomly adds obstacles to the list and moves them 5(steps/pixels?) on every iteration of loop
the obstacles_rect don't have any info about the type of obstacle except there coordinates so if x coordinate = 350 then its cactus or else its the bird and only adds the obstacle to list if x coordinate of obstacles is greater than -100


4) **Dino_animation** :
if dino index = 0 it shows frame 1
slowly, on each iteration we add 0.1 so it eventually becomes 1 and then the second frame is shown.
after the index is 1,it is set back to zero
and this it happens so fast that it seems like its moving


**Now lets actually look at the main code**



pygame is initialized before the main loop which initializes all the components of pygame ready for use

the screen is set and some more variables are defined like the gravity, game_active score, start time
  
and some assets are imported using pygame.image.load(path)(for images) including font, music and rectangles are created where ever needed

and then we added 2 timers for bird animation and obstacles

and the real magic happens in the while loop

pygame.event.get() gets all the events
and then we check for specific kind of event and perform actions like quit and mouse button and jumping and even animation the bird 


and also not to make the game too easy, the dinosaur can only jump if it touches the ground, so it cant jump while its in the air



~~i kinda cheated with physics~~.
instead of gravity, i have used a work around which does the job 
       
            
randint(0,1) picks a random number between 0 and 1 and depending on output, a specific enemy is spawned


i have divided the content to be shown on the screen into 2 parts:
game_active and else


game_active has all the surfaces to be displayed on the screen when the game is active
and else has everything to show when the game is inactive(specific cases for not started and game ended)

in the end pygame.display.update() frequently updates the display and

and clock.tick(60) makes sure that our fps stays constant





### test_project.py

this file contains 3 tests for the functions in the project.py and can be run using pytest

at the start, some temporary variables are made because pygame isn't suited to be tested with pytest

1. First test checks if the score in the starting is 0

2. Second test places one obstacle in the list and calls the obstacle_movement function and makes sure returned list contains one obstacle

3. Third test checks if collision turns the game active to false by placing a sample obstacle at a specific position



### HOW TO RUN THE PROJECT


#### Requirements

1) python
2) pygame module installed
3) pytest module (if you want to run the tests)


Clone the project repository from GitHub:
https://github.com/saiusesgithub/Chrome-Dinosaur-Game-Clone/

then run the project.py file

Press any mouse button to start the game and use the spacebar to make the dinosaur jump over obstacles

enjoy!



### TODOS
1. clean up the code and modularize the content obviously

2. add better sound effects for scoring 100 points

3. show high score

4. better way to restart the game and separate screens for start and end

5. make the game harder as the game improves

6. make multiple sized cacti

7. decrease the height of birds and make a crouch mechanic

8. day and night cycle

9. animated background




> Thank you for checking out my project
