import pygame;
import pygame.font
import pygame.mixer

image1=pygame.image.load("images/téléchargement (19).png")
image2=pygame.image.load("images/The Art Showcase.png")
image3=pygame.image.load("images/The Art Showcase.png")


class Scene:
    def __init__(self, text, image=None, actions=None,action_key_mapping=None ,sound=None):
        self.text = text
        self.image = image  # Optional image for visual elements
        self.actions = actions or []  # List of available actions (choices)
        self.action_key_mapping=action_key_mapping or{}
        self.sound=sound
    def draw(self, screen):
        # Render text and optionally draw the image
        if self.image:
            screen.blit(self.image, (0, 0))  # Display image at the top

        # Dark background for text
        pygame.draw.rect(screen, (0, 0, 0), (0, 310, 800, 90))
  
        # Play sound if available
        if self.sound:
            celtic_song = pygame.mixer.Sound(self.sound)
            celtic_song.set_volume(1.0)
            celtic_song.play()

        # Render multiline text on the dark background
        font = pygame.font.SysFont("Arial", 17)
        lines = self.text.split('\n')  # Split text into lines if it contains newline characters
        y_offset = 320  # Initial y-coordinate for text
        for line in lines:
            text_surface = font.render(line, True, 'white')
            screen.blit(text_surface, (10, y_offset))
            y_offset += text_surface.get_height() + 5  # Adjust the vertical spacing between lines


    def handle_input(self, event,action_key_mapping):
        if event.type == pygame.KEYDOWN:
            # Check for key presses that correspond to actions
            for i, action in enumerate(self.actions):
                if event.key == action_key_mapping[action]:
                    return self.actions[i]  # Return the chosen action
        return None  # No action chosen
    

class WoodsScene(Scene):
    def __init__(self):
        super().__init__(
           "You are isolated in the woods ,surrounded \nby darkness and the distant  howls of wolves.",
           image=image1,
            actions=["next"],
           action_key_mapping = {
            
            "next" :pygame.K_RETURN,
        }  ,sound="sounds/theres-something-about-this-room-201112.mp3"
        )
         
    def  handle_input(self, event):
        action =  super().handle_input(event,self.action_key_mapping)
        if action == "next":
            return BlackScene()  
        else:
            return None 
    def show(self):
        # Play the sound when the scene is displayed
        woods_sound="sounds/theres-something-about-this-room-201112.mp3"
        woods_sound.play()
class BlackScene(Scene):
    def __init__(self):
        super().__init__(
           "you hear the sound of footsteps approaching",
           image=image2,
            actions=["next"],
            action_key_mapping = {
            
           "next" :pygame.K_RETURN ,
        }   
        )
       
    def handle_input(self, event):
        action = super().handle_input(event,self.action_key_mapping)
        if action == "next":
            return HauntedScene()  # Return the next scene object
        else:
            return None  
        
class HauntedScene(Scene):
    def __init__(self):
        super().__init__( "As you navigate through the haunted woods,\nstrange sounds fill  the air, making you feel uneasy  "
          ,image=image3 , actions=["next"],
        action_key_mapping = {
            
            "next":pygame.K_RETURN
        }   

        
        )
    def handle_input(self, event):
        action = super().handle_input(event,self.action_key_mapping)
        if action == "next":
            return None # Return the next scene object
        else:
            return None  
        
  
        
SCREEN_WIDTH=600
SCREEN_HIGHT=400

pygame.init()
current_scene =WoodsScene()  # Set the initial scene
screen=pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HIGHT))
running = True
while running:
    screen.fill('black')
    
    current_scene.draw(screen)
    
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle scene-specific input based on current_scene
        next_scene = current_scene.handle_input(event)
        if next_scene:
         current_scene = next_scene
    
   

    
    pygame.display.flip()