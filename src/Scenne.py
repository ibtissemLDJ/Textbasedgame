import pygame
import time

image1 = pygame.image.load("images/téléchargement (19).png")
class Scene:
    def __init__(self, text, image=None, actions=None, action_key_mapping=None, sound=None):
        self.text = text
        self.image = image
        self.actions = actions or []
        self.action_key_mapping = action_key_mapping or {}
        self.sound = sound
        self.finished_typing = False  # Flag to indicate when typing animation is finished

    def draw(self, screen):
        # Render text and optionally draw the image
        if self.image:
            screen.blit(self.image, (0, 0))

        # Dark background for text
        pygame.draw.rect(screen, (0, 0, 0), (0, 310, 800, 90))

        # Play sound if available
        if self.sound:
            celtic_song = pygame.mixer.Sound(self.sound)
            celtic_song.set_volume(1.0)
            celtic_song.play()

        # Render multiline text on the dark background
        font = pygame.font.SysFont("Arial", 17)
        lines = self.text.split('\n')
        y_offset = 320
        if self.finished_typing:
            for line in lines:
                text_surface = font.render(line, True, 'white')
                screen.blit(text_surface, (10, y_offset))
                y_offset += font.get_height() + 5  # Move to the next line
        else:
        
            for line in lines:
                text_so_far = ''
                for char in line:
                    text_so_far += char  # Add one character at a time
                    text_surface = font.render(text_so_far, True, 'white')
                
                    screen.blit(text_surface, (10, y_offset))
                    pygame.display.flip()  # Update the display
                    time.sleep(0.1)  # Adjust the delay between characters (e.g., 0.1 seconds)
                y_offset += font.get_height() + 5  # Move to the next line

            self.finished_typing = True  # Set flag to indicate typing animation is finished
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            for action, key in self.action_key_mapping.items():
                if event.key == key:
                    # Print the key pressed for debugging
                    print("Key Pressed:", event.key)
                    print("Mapped Action:", action)
                    return action
        return None



class WoodsScene(Scene):
    def __init__(self):
        super().__init__(
            "You are isolated in the woods, surrounded \nby darkness and the distant howls of wolves.",
            image=image1,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/theres-something-about-this-room-201112.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return BlackScene()
        else:
            return None

    def show(self):
        woods_sound = pygame.mixer.Sound("sounds/theres-something-about-this-room-201112.mp3")
        woods_sound.play()

class BlackScene(Scene):
    def __init__(self):
        super().__init__(
            "you hear the sound of footsteps approaching",
            image=pygame.image.load("images/The Art Showcase.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return HauntedScene()
        else:
            return None

class HauntedScene(Scene):
    def __init__(self):
        super().__init__(
            "As you navigate through the haunted woods,\nstrange sounds fill the air, making you feel uneasy.",
            image=pygame.image.load("images/The Art Showcase.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return AnotherScene()
        else:
            return None

class AnotherScene(Scene):
    def __init__(self):
        super().__init__(
            "You are isolated in the woods, surrounded \nby darkness and the distant howls of wolves.\nDo you want to continue?\n(1: Yes, 0: No)",
            image=image1,
            actions=["yes", "no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0},
            sound="sounds/theres-something-about-this-room-201112.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return Scene4()
        elif action == "no":
            return Scene6()
        else:
            return None


class Scene4(Scene):
    def __init__(self):
        super().__init__(
            "You chose Yes and moved to Scene 4.",
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return None  # Scene ends here
        else:
            return None


class Scene6(Scene):
    def __init__(self):
        super().__init__(
            "You chose No and moved to Scene 6.",
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return None  # Scene ends here
        else:
            return None


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

pygame.init()
image1 = pygame.image.load("images/téléchargement (19).png")
current_scene = WoodsScene()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    screen.fill('black')
    current_scene.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        next_scene = current_scene.handle_input(event)
        if next_scene:
            current_scene = next_scene
    pygame.display.flip()

pygame.quit()