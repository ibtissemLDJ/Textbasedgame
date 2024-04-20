import pygame
import pygame.font
import pygame.mixer

image1 = pygame.image.load("Textbasedgame/images/téléchargement (19).png")
image2 = pygame.image.load("Textbasedgame/images/The Art Showcase.png")
image3 = pygame.image.load("Textbasedgame/images/The Art Showcase.png")


class Scene:
    def init(self, text, image=None, actions=None, action_key_mapping=None, sound=None):
        self.text = text
        self.image = image  # Optional image for visual elements
        self.actions = actions or []  # List of available actions (choices)
        self.action_key_mapping = action_key_mapping or {}
        self.sound = sound

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

    def handle_input_event(self, event):
        if event.type == pygame.KEYDOWN:
            for action, key in self.action_key_mapping.items():
                if event.key == key:
                    # Print the key pressed for debugging
                    print("Key Pressed:", event.key)
                    print("Mapped Action:", action)
                    return action
        return None


class WoodsScene(Scene):
    def init(self):
        super().init(
            "You are isolated in the woods ,surrounded \nby darkness and the distant  howls of wolves.\n(1:yes or 0: no)",
            image=image1,
            actions=["yes", "no"],
            action_key_mapping={
                "yes": pygame.K_1,
                "no": pygame.K_0
            },
            sound="Textbasedgame/sounds/theres-something-about-this-room-201112.mp3"
        )

    def handle_input(self, event):
        action = self.handle_input_event(event)
        if action:
            # Process the chosen action
            if action == "yes":
                # Handle the consequence of staying
                return BlackScene()
            elif action == "no":
                # Handle the consequence of going deeper
                return HauntedScene()
        return None

    def show(self):
        # Play the sound when the scene is displayed
        woods_sound = "Textbasedgame/sounds/theres-something-about-this-room-201112.mp3"
        woods_sound.play()


class BlackScene(Scene):
    def init(self):
        super().init(
            "you hear the sound of footsteps approaching",
            image=image2,
            actions=["next"],
            action_key_mapping={
                "next": pygame.K_RETURN
            }
        )

    def handle_input(self, event):
        action = self.handle_input_event(event)
        if action == "next":
            return HauntedScene()  # Return the next scene object
        return None


class HauntedScene(Scene):
    def init(self):
        super().init(
            "As you navigate through the haunted woods,\nstrange sounds fill  the air, making you feel uneasy  ",
            image=image3,
            actions=["next"],
            action_key_mapping={
                "next": pygame.K_RETURN
            }
        )

    def handle_input(self, event):
        action = self.handle_input_event(event)