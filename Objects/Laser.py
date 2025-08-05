from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    """
    Class for the lasers shot by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Laser.png")
        self.set_image(image, 33, 9)
        
        # set movement
        self.set_direction(0, 20)
        self.register_collision_object("Astronaut")
        self.register_collision_object("Asteroid")
        self.register_collision_object("Zork")
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)
    
    def handle_collision(self, other, other_type):
        if other_type == "Asteroid":
            self.room.asteroid_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(5)
        elif other_type == "Astronaut":
            self.room.astronaut_shot.play()
            self.room.delete_object(other)
            self.room.score.update_score(-10)
            Globals.LIVES -= 1
            if Globals.LIVES <= 0:
                self.room.running = False
                Globals.LIVES = 5
                Globals.SCORE = 0
                self.room.lives.update_image()
            else:
                self.room.lives.update_image()
        elif other_type == "Zork":
            self.room.asteroid_shot.play()
            print("Zork hit by laser")
            Globals.zork_lives -= 1
            other.check_lives()
            
        self.room.delete_object(self)
    