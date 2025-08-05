from GameFrame import RoomObject, Globals
import pygame
import random
from Objects.Laser import Laser
from Objects.Rescue_kit import Rescue_kit
class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        self.handle_key_events = True
        self.can_shoot = True
        rescue_spawn_time = 500
        self.set_timer(rescue_spawn_time, self.spawn_rescue_kit)
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            self.y_speed -= 5
        elif key[pygame.K_s]:
            self.y_speed += 5
        elif key[pygame.K_SPACE]:
            self.shoot_laser()
    def keep_in_room(self):

        if self.y <0:
            self.y = 0
            self.y_speed *= -0.2
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -0.2

    def step(self):
        self.keep_in_room()
    
    def shoot_laser(self):
        if self.can_shoot:
            self.room.shoot_laser.play()
            new_laser =  Laser(self.room,
                          self.x + self.width,
                          self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(15 , self.reset_shot)
    def reset_shot(self):
        self.can_shoot = True
    def spawn_rescue_kit(self):
        """
        Randomly spawns a new Rescue Kit
        """
        # spawn Rescue Kit and add to room
        new_rescue_kit = Rescue_kit(self.room, Globals.SCREEN_WIDTH - 50, random.randint(0, Globals.SCREEN_HEIGHT - 50))
        self.room.add_room_object(new_rescue_kit)
        
        # reset time for next Rescue Kit spawn
        rescue_spawn_time = 1000
        self.set_timer(rescue_spawn_time, self.spawn_rescue_kit)