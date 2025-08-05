from GameFrame import RoomObject, Globals
import random
class Rescue_kit(RoomObject):
    """
    A class for the Rescue Kit that can be collected by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Rescue Kit object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Repair_kit.png")
        self.set_image(image, 50, 50)
        
        # register events
        self.register_collision_object("Ship")
        angle = random.randint(135,225)
        self.set_direction(angle, 5)

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Rescue Kit
        """
        if other_type == "Ship":
            if Globals.LIVES >= 3:
                Globals.LIVES = 5
            else:
                Globals.LIVES += 2
            self.room.lives.update_image()
            self.room.delete_object(self)  # Remove the Rescue Kit after collection
    def step(self):
        """
        Determines what happens to the asteroid on each tick of the game clock
        """
        self.keep_in_room()
        self.outside_of_room()
        
    def keep_in_room(self):
        """
        Keeps the asteroid inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1
            
    def outside_of_room(self):
        """
        removes asteroid that have exited the room
        """
        if self.x + self.width < 0:
            print("asteroid deleted")
            self.room.delete_object(self)