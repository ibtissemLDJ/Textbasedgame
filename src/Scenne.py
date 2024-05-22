import pygame
import time
points =0 
global score
score=0
joueur =""
import random


pygame.init()
image1 = pygame.image.load("images/téléchargement (19).png")
image2 = pygame.image.load("images/téléchargement (42) (1).png")
image3 = pygame.image.load("images/téléchargement (32).png")
image4 = pygame.image.load("images/boxes.png")
image5 = pygame.image.load("images/game over.jfif")
image6 = pygame.image.load("images/tryy.png")
image7 = pygame.image.load("images/Letter I.png")
image8 = pygame.image.load("images/MORSEcode.png")
image1 = pygame.image.load("images/Поезд пиксель арт 1 (1).png")
Broom = pygame.image.load("images/Broom.png")
bird = pygame.image.load("images/bird.png")
wind = pygame.image.load("images/wind.png")
amazone = pygame.image.load("images/amazone.png")
brbranch=pygame.image.load("images/brbranch.png")
tree=pygame.image.load("images/tree.png")
Gameover=pygame.image.load("images/Gameover.png")
eat=pygame.image.load("images/eat.png")
tryagain=pygame.image.load("images/tryagain.png")
dbcave=pygame.image.load("images/dbcave.png")
cave=pygame.image.load("images/cave.png")
bear=pygame.image.load("images/bear.png")
dé=pygame.image.load("images/dé.png")
enigma=pygame.image.load("images/enigma.png")
turbo=pygame.image.load("images/turbo.png")
#image de la prtie rania####
image1 = pygame.image.load("images/téléchargement (19).png")
image_l1_1=pygame.image.load("images\Scenelevel11.png")
image_l1_4=pygame.image.load("images\image kharita1.png")
imageScene5=pygame.image.load("images\scary room 1.png")
imageScene6=pygame.image.load("images\witches1.png")
imageScene7=pygame.image.load("images\gateway.png")
imageScene_level1_1=pygame.image.load("images\magic land.png")
imageScene_level1_3=pygame.image.load("images\man.png")
imageScene_level1_4=pygame.image.load("images\image kharita1.png")
imageScene_level1_5=pygame.image.load("images\image1 the sea and land.png")
imageScene_level1_s1l=pygame.image.load("images\scary sea.png")
imageScene_level1_s2_swiming=pygame.image.load("images\crocodile 2.png")
imageScene_level1_s2_beatyes=pygame.image.load("images\gameover.jpg")
imageScene_level1_s2_noswiming=pygame.image.load("images\\boat.png")
imageScene_level1_s1__=pygame.image.load("images\sea.png")
image1 = pygame.image.load("images/Поезд пиксель арт 1 (1).png")
pause_img = pygame.image.load("images/photo_2024-05-04_10-38-42.png")


def get_scene_by_name(scene_name):
    global_scene = globals()
    if scene_name in global_scene:
        scene_class = global_scene[scene_name]
        if callable(scene_class):  # Vérifie si c'est une classe (callable)
            return scene_class()
    return None


def sauvegarder_partie(nom_joueur, score, nomScene):
    with open("sauvegarder/sauvegarde.txt", "a") as fichier:
        fichier.write(f"{nom_joueur}\n")
        fichier.write(f"{score}\n")
        fichier.write(f"{nomScene}\n")

def charger_partie(nom_joueur):
    try:
        with open("sauvegarder/sauvegarde.txt", "r") as fichier:
            for ligne in fichier:
                nom = ligne.strip()
                score = int(fichier.readline().strip())
                scene = fichier.readline().strip()
                if nom == nom_joueur:
                    return nom, score, scene

    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None, None, None


class Popup():
    def __init__(self, x, y, width, height, message):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.message = message
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, 28)
        self.bg_color = (0, 0, 0)
        self.text_color = (0, 255, 0)
        self.visible = False

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.bg_color, self.rect)
            text_surface = self.font.render(self.message, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)


class Button() :
    def  __init__(self, x ,y , image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, screen,nom_joueur, score, scene):
        screen.blit(self.image, self.rect)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) :
            if pygame.mouse.get_pressed()[0] ==1 and self.clicked ==False :
                sauvegarder_partie(nom_joueur, score, scene)
                popup.visible = True
                self.clicked = True
                

popup = Popup(150, 150, 200, 50, "well saved game")
button = Button(100 , 100 , pause_img)


class Scene:
    def __init__(self, text, image=None, actions=None, action_key_mapping=None, sound=None, font="Comic Sans MS"):
        self.text = text
        self.image = image
        self.actions = actions or []
        self.action_key_mapping = action_key_mapping or {}
        self.sound = sound
        self.font = font
        self.finished_typing = False  # Flag to indicate when typing animation is finished
        self.sound_played =False
        self.score=score
        

    def draw(self, screen):
        # Render text and optionally draw the image
        if self.image:
            screen.blit(self.image, (0, 0))

        # Dark background for text
       ## pygame.draw.rect(screen, (0, 0, 0), (0, 400, 800, 170))

        # Play sound if available
        if self.sound:
           if not self.sound_played:
            celtic_song = pygame.mixer.Sound(self.sound)
            celtic_song.set_volume(1.0)
            celtic_song.play()
            self.sound_played = True

        # Render multiline text on the dark background
        font = pygame.font.SysFont(self.font, 17)#nsewerha 
        score_text=font.render(f"score:{self.score}",1,'white')
        screen.blit(score_text,(20,20))
        lines = self.text.split('\n')
        y_offset = 430
        if self.finished_typing:
            for line in lines:
                text_surface = font.render(line, True, 'white')
                screen.blit(text_surface, (30, y_offset))
                y_offset += font.get_height() + 5  # Move to the next line
               
        else:
        
            for line in lines:
                text_so_far = ''
                for char in line:
                    text_so_far += char  # Add one character at a time
                    text_surface = font.render(text_so_far, True, 'white')
                
                    screen.blit(text_surface, (30, y_offset))
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
    def add_sub_score(self,point):
       global score
       c=self.score+point
       if c>=0 :
        score+=point
#######################################IBTISSEM############################################################
class background(Scene):

       
    def __init__(self):
        super().__init__(
            "\n\n\n\n\n                                                              Tap enter to start playing XD",
            image=pygame.image.load("images/Frame 1707478374.png") ,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (0, 400, 800, 170))
        return super().draw(screen) 
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return debut()
        else:
            return None



class debut(Scene):
   def __init__(self):
        super().__init__(
            "\n\n\n                                                                           \>",
            image= pygame.image.load("images/Frame 1707478369.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer1 = "newlevel"
        self.answer2 = "continue"
        self.user_input = ""

   def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont(self.font, 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (435, 515))  

   def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
              if self.user_input.lower() == self.answer1 :
                 return name() 
              elif self.user_input.lower() == self.answer2 :
               return nameCONTINUE() # ta3 continue 
            else:
                # Check if the pressed key is alphanumeric
                if event.unicode.isalnum():
                    self.user_input += event.unicode.lower()
        return self      
class name(Scene): 
    def __init__(self):
        super().__init__(
            "Hello Dear Player ""!\nPlease Enter Your Name:",
            image=pygame.image.load("images/Frame 1707478369.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.user_input = ""
        self.joueur = ""  # Initialize joueur

    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont(self.font, 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (270, 460))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                if self.user_input:  # Check if there's input
                    self.joueur = self.user_input  # Save user input to joueur
                    self.user_input = ""  # Reset user input for next use
                    return START()  # Return next scene if needed
            elif event.unicode.isalnum():
                self.user_input += event.unicode.lower()

        return self
    


class nameCONTINUE(Scene): 
    def __init__(self):
        super().__init__(
            "Welcom Back Dear Player\nPlease Enter Your Name:",
            image=pygame.image.load("images/Frame 1707478369.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.user_input = ""
        self.joueur = ""  # Initialize joueur

    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont(self.font, 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (270, 460))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                if self.user_input:  # Check if there's input
                    self.joueur = self.user_input  # Save user input to joueur
                    self.user_input = ""  # Reset user input for next use
                    nom , score, scene = charger_partie(joueur)
                    scene1 = get_scene_by_name(scene)
                    return scene1  # Return next scene if needed
            elif event.unicode.isalnum():
                self.user_input += event.unicode.lower()

        return self




class START(Scene):
    def __init__(self):
        super().__init__(
            "Runnnnnn  ... \nYOU ARE IN DANGERRRRR \n\n\n\n                                                                   Tap enter to continue...",
           
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/wood.mp3"
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return WoodsScene()
        else:
            return None
##########################################sofia############################################################

class WoodsScene(Scene):
    def __init__(self):
        super().__init__(
            "You are isolated in the woods...\n\nsurrounded by darkness and the distant howls of wolves.\n\n\n                                                   Tap Enter To Continue",
            image=pygame.image.load("images/photo_2024-05-19_12-11-38.jpg") ,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return BlackScene()
        else:
            return None

    

class BlackScene(Scene):
    def __init__(self):
        super().__init__(
            "You heard the sound of footsteps approaching ...\n\n\n\n\n                                                   Tap Enter To Continue",
            image=pygame.image.load("images/photo_2024-05-19_12-11-38.jpg"),
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
            "Strange sounds fill the air, making you feel scary.\n\n\n\n\n                                                   Tap Enter To Continue",
            image=pygame.image.load("images/photo_2024-05-19_12-11-38.jpg"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return HauntedHouseScene()
        else:
            return None

class  HauntedHouseScene(Scene):
    def __init__(self):
        super().__init__(
            "As you navigated through the hunted woods, trying to find safety \nYou saw lights coming from a house nearly.\nWould you go to that house?\nTap(0) For: \"no\" \nTap(1) For :\"yes\" ",
            image=pygame.image.load("images/photo_2024-05-19_12-11-38.jpg"),
            actions=["yes", "no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return Scene5()#scene rania 1 
        elif action == "no":
            return GhostScene()
        else:
            return None




class GhostScene(Scene):
    def __init__(self):
        super().__init__(
            "Whyyyy would you stay in these woodss !!!! \nThe ghoasts are running toward youu ....\nthere is nowhere to escape but that house\nDo you still don't want to go to that house?\nTap(0) For:\"no\"\nTap(1) For:\"yes\"",
            image=pygame.image.load("images/ghostScene.png"),
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return Scene5()#scene rania 1 
        elif action == "no":
            return End1Scene()
        else:
            return None     
##############################################rania########################################################    
class Scene5(Scene):#done scene5
    
    def __init__(self):
        super().__init__(
            "You are now in the house XD\nYou get in a dark room .You heard a scary sounds coming from all directions. \nIt's time to face the monsters luking inside ........ Can you survive?\n\n\n                                                   Tap Enter To Continue",
            image=imageScene5,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/HOUSE1.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene6()
        else:
            return None
   
   
    
class Scene6(Scene):#done scene6
     def __init__(self):
        super().__init__(
            "You encountered a circle of witches,seeing them spining around doing weird things.\nEverything turned black             OHH NO,what's happening ?\nYOU FAINTED!...",
            image=imageScene6,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
            
        )

     def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene7()
        else:
            return None
    
    
class Scene7(Scene):#done scene 7
    def __init__(self):
        super().__init__(
            "Once you opened your eys slowely... you saw a faint light comming from  far\nYou approached,opened the door,and suddenly XXXXXX the gateway swallowed you there \nYOU WILL NEVER GO BACK AGAIN!!!\n\n\n                                                   Tap Enter To Continue",
            image=imageScene7,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene_level1_1()
        else:
            return None
     
class Scene_level1_1(Scene):#done debut of level
    def __init__(self):
        super().__init__(
            "\n\n                                                     ETHERIA ' THE LOST LAND ',2024      ",
            image=image_l1_1,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
           
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene_level1_2()
        else:
            return None
   
class Scene_level1_2(Scene):#done scenne 2 de level
    def __init__(self):
        super().__init__(
            "Etheria, a land where magic took it's first breath, where people can fly. Everything seems like it's \nnot real. It's a land full of illusions and mystery.\n\n\n\n                                                   Tap Enter To Continue ",
            image=imageScene_level1_1,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/birds.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene_level1_3()
        else:
            return None
class Scene_level1_3(Scene):#senen 3 level
    def __init__(self):
        super().__init__(
            "Bigboy: \"I am the man who will guid you here in this land ...\nI'll help you to find the door that will take you back to your world\"\n\n\n\n                                                   Tap Enter To Continue ",
            image=imageScene_level1_3,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene_level1_4()
        else:
            return None
class Scene_level1_4(Scene):#senne 4 level
    def __init__(self):
        super().__init__(
            "Bigboy: \"There are a bunch of missions you have to complete, you have to solve all the enigmas so \nhere is the card that will help you to find the door.\" ",
            image=imageScene_level1_4,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene_level1_5()
        else:
            return None
    
class Scene_level1_5(Scene):#scene5 level
    def __init__(self):
        super().__init__(
            "As you walked in the land ...you incountered a crossroad, there are two roads in front  of you: \n1)-the land road\n2)-the river road \nTap(0) For:\"Land Road\"\nTap(1) For:\"river  Road\""
            ,
            image=imageScene_level1_5,
            actions=["the land road","the sea road"],
            action_key_mapping={"the land road": pygame.K_1, "the sea road": pygame.K_2}
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "the land road":
            return DesertScene();#le chemain ta3 ghaba nakatbou la classe de sofia
        elif action == "the sea road":
            return Scene_level1_s1l()
        else:
          return None #le chemain ta3 le sea la premier condition 
        
class Scene_level1_s1l(Scene):#scene 6level
    def __init__(self):
        super().__init__(
            "You arrived to a lack there is boat in front of you the river  seems dark and scary would you like to go by :\n1) Swiming \n2) Boat\nType (1) For: \"swiming\" \nType (1) For: \"boat\" ",
            image=imageScene_level1_s1__,
            actions=["Swiming","boat"],
            action_key_mapping={"Swiming": pygame.K_1,"boat": pygame.K_2}
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "Swiming":#swiming
            return Scene_level1_s1()#y3oume
        elif action == "boat":
            return Scene_level1_s2_noswiming_boat()#may3omche boat
        else:
            return None
            #la deuxeieme condition yes

class Scene_level1_s1(Scene):#scene 7 sea road
    def __init__(self):
        super().__init__(
            "The lack is dark, BE AWARE...  You saw a shadaw of animal in there \nAre you sure you STILL wanna continue by swiming??\nType (1) For: \"YES\" \nType (2) For: \"NO\"",
            image=imageScene_level1_s1l,
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1,"no": pygame.K_2}
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":#swiming
            return Scene_level1_s2_swiming()#y3oume
        elif action == "no":
            return Scene_level1_s2_noswiming()#may3omche
        else:
            return None
            #la deuxeieme condition yes
class Scene_level1_s2_swiming(Scene):#scene 8 swiming
    def __init__(self):
        super().__init__(
            "Ohh nooo The crocodiles are aproaching !!!\n no nononnnnoo the crocodile bites you in your leg you started bleading :X \nDo you want to beat the crocodile ?\nType (1) For: YES \nType (2) For: NO ",
            image=imageScene_level1_s2_swiming,
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1,"no": pygame.K_2}
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":#swiming
            return Scene_level1_s2_beat()#y09tale crocodile
        elif action =="no":
            return Scene_level1_s2_beat()#mayo9talche
        else:
            return None   
class Scene_level1_s2_beat(Scene):#game over#beating crocodile scene 9
    def __init__(self):
        super().__init__(
            "Oh noo the big crocodile dragged you to the bottom of the river \n\ni am sorry YOU DIED :X                                              <<<<<<<<<<GAME OVER>>>>>>>>>>\n                                                        Tap \"R\" to start again :)",
            image=imageScene_level1_s2_beatyes,
           actions=["next","repeat"],
            action_key_mapping={"next": pygame.K_RETURN,"repeat":pygame.K_r},
            sound="sounds/game-over.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return None
        else:
            if action == "repeat":
                return Scene_level1_1()
            else:
                return None 

class Scene_level1_s2_noswiming(Scene):#scene 11
    def __init__(self):
        super().__init__(
            "You took the right decision :),that river contains a scary crocodile !!\nYou are swiming again to the land,There is a boat there do you wanna take it ?\nType (1) For: \"Yes\" \nType (2) For: \"No\" ",
            image=imageScene_level1_s2_noswiming,
            actions=["boat","land"],
            action_key_mapping={"baot": pygame.K_1,"land": pygame.K_2},
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "boat":#swiming
            return Scene_level1_s2_noswiming_boat()#y3oume
        elif action == "land":
            return DesertScene()#sofia
        else:
            return None
            
class Scene_level1_s2_noswiming_boat(Scene):#scene 12
    def __init__(self):
        super().__init__( 
            "You are on the boat now... You've never been in a boat before, that's amazing!!!!!\nBut wait, suddenly the wind is huge, and the boat is about to rock.\nDo you still wanna continue by the boat \nType (1) For: Yes \nType (2) For: No",
            image=imageScene_level1_s2_noswiming,
            actions=["boat","land"],
            action_key_mapping={"boat": pygame.K_1,"land": pygame.K_2},
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "boat":#swiming
            return Scene_level1_s2_noswiming_boat_continue_gameover()#y3oume
        elif action == "land":
            return DesertScene()#sofia
        else:
            return None
class Scene_level1_s2_noswiming_boat_continue_gameover(Scene):#game over scene 13
    def __init__(self):
        super().__init__(
            "The wind has gone, but when you checked the boat, you saw water in it!!! What to do??\nOHH no you drown again !!\n                                                                   <<<<<<<<<<GAME OVER>>>>>>>>>> \n Tap 'r'  to replay the game ",
            image=imageScene_level1_s2_beatyes,
            actions=["next","repeat"],
            action_key_mapping={"next": pygame.K_RETURN,"repeat":pygame.K_r},
            sound="sounds/game-over.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return None
        else:
            if action == "repeat":
                return Scene_level1_1()
            else:
                return None 
##############################################Sofia  ######################################################   
class GhostScene(Scene):
    def __init__(self):
        super().__init__(
            "There are ghosts nearby, running toward you with dangerous weapons.\nThere is nowhere to escape but that house\nDo you want to go back ?\nTap (0) For: No\nTap (1) For: Yes",
            image=pygame.image.load("images/ghostScene.png"),
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return Scene5()#scene rania 1 
        elif action == "no":
            return End1Scene()
        else:
            return None
class End1Scene(Scene):#est ce que hna kayen game over 
    def __init__(self):
        super().__init__(
            "<<<<GAME OVER>>>>\n\n\n Tap 'r'  to replay the game ",
            image=pygame.image.load("images/End1Scene.png"),
            actions=["next","replay"],
            action_key_mapping={"next": pygame.K_RETURN,"replay":pygame.K_r},
            sound="sounds/game-over.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action=="replay":
             return WoodsScene()
        else:
         return None  
class DesertScene(Scene):
    def __init__(self):
        super().__init__(
            "You started walking and discovering this magical place,\n"
            "you want to go and find the door that will lead you home...\n"
            "By walking forward, you meet a strang animal; it seems like a dragon.\n"
            "The dragon talks to you: 'I guess you’re on the right path,\n"
            "but be ready, a lot of surprises are coming your way.'",
            image=pygame.image.load("images/DesertScene.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return BoxClosedScene()
        else:
          
                return None
                  
class BoxClosedScene(Scene):
    def __init__(self):
        super().__init__(
            "While admiring this magical city, you saw something glowing in the distance.\n"
            "You approach to see what it is. Oh! It's a big golden box.\n"
            "Do you want to open it?\nTap (0) For: No\nTap (1) For: Yes" ,
            image=pygame.image.load("images/BoxClosedScene.png"),
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return BoxOpenedScene()
        elif action == "no":
            return ThinkScene()
        else:
            return None
class BoxOpenedScene(Scene):
    def __init__(self):
        super().__init__(
            "\n******************************\n    CONGRATULATIONS!    \n******************************\nYou have gained 3 points!\n******************************\n",
            image=pygame.image.load("images/BoxOpenedScene.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/points.mp3"

        )
        super().add_sub_score(3)
    def handle_input(self, event):
        
        action = super().handle_input(event)
        if action == "next":
            return TheftScene()
        else:
            return None       
class ThinkScene(Scene):
    def __init__(self):
        super().__init__(
            "You are still thinking of that big golden box!\n"
            "Are you sure you don’t want to open it?\n"
            "Tap (0) For: No\n"
            "Tap (1) For: Yes",
            image=pygame.image.load("images/BoxClosedScene.png"),
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return TheftScene()
        elif action == "no":
            return BoxOpenedScene()
        else:
            return None  


class TheftScene(Scene):
    def __init__(self):
        super().__init__(
            "Oops, the little dwarf has stolen your map.\n"
            "What should you do now? The dwarf tells you that you have to solve this riddle to get back\n"
            "your map: I am taken once every minute, twice every moment, but never in an hour. What am I?\n"
            "Tap enter to write your answer!",
            image=pygame.image.load("images/TheftScene.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/oops.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return theM()
        else :
            return None
class theM(Scene):
    def __init__(self):
        super().__init__(
            "Enter your answer : ",
            image= enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "m"
        self.user_input = ""

    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont("Arial", 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]  
            elif event.key == pygame.K_RETURN:
                return MapScene() if self.user_input.lower() == self.answer else HelpScene()
            else:
                
                if pygame.key.name(event.key).isalpha():
                    self.user_input += pygame.key.name(event.key).lower()
        return self        
class HelpScene(Scene):
    def __init__(self):
        super().__init__(
            "Do you need help? This hint will cost you <1> point.\n"
            "Tap (0) For: No\n"
            "Tap (1) For: Yes",
            image=pygame.image.load("images/TheftScene.png"),
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action =="yes":
          global score
          if score>0 :
            super().add_sub_score(-1)
            return HelpActScene()
          else :return ScoreScene()
        elif action == "no":
            return NoHelpScene()
        else:
            return None 
class ScoreScene(Scene):
    def __init__(self):
        super().__init__(
            "Oops! Looks like you're a bit short on points for that. ¯\_(ツ)_/¯",
            image=pygame.image.load("images/TheftScene.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
       
    def handle_input(self, event):
        
        action = super().handle_input(event)
        if action == "next":
            return NoHelpScene()
        else:
            return None    
class HelpActScene(Scene):
    def __init__(self):
        super().__init__(
            "The answer have to be :::Letter:::\n\n\n\nTap enter to fill your answer!",
            image=pygame.image.load("images/TheftScene.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        
    def handle_input(self, event):
       action = super().handle_input(event)
       if action == "next":
           return theM()
       else :
           return None
class NoHelpScene(Scene):
    def __init__(self):
        super().__init__(
            "Oh oh! You should try again. ~~~\n\n\n\nTap ENTER to write your answer!",
            image=pygame.image.load("images/TheftScene.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/oops.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next": 
            return theM()
        else :
            return None
      
class MapScene(Scene):
    def __init__(self):
        super().__init__(
            "Hooohoo! You got it right! Here is your map.\n"
            "But wait, I've got a letter for you. You've got to remember it\n"
            "until the end of the level. The letter is 'R'.",
            image=pygame.image.load("images/MapScene.png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return BroomScene()
        else:
            return None  

class BroomScene(Scene):
    def __init__(self):
        super().__init__(
            "You’re so happy because the dwarf gave you back your map!\n"
            "Oh, is this a magic broom?! Do you want to ride it?\n"
            "Tap (0) for: No\n"
            "Tap (1) for: Yes",
            image=pygame.image.load("images/BroomScene.png"),
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return MagicBroom()
        elif action == "no":
            return NotbromScene()
        else:
            return None  

        
##########################################################Amira#########################################
class MagicBroom(Scene):
    def __init__(self):
        super().__init__(
            "You're flying with this magic broom.\n"
            "Wow, the view from above is fantastic!\n\n\n\n"
            "Tap Enter to continue.",
            image=Broom,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Bird()
        else:
            return None

    

class Bird(Scene):
    def __init__(self):
        super().__init__( 
            "Oh no! A bird is coming toward you! What will you do?\n\n\n\n\n"
            "Tap Enter to continue.",
            image=bird ,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Avoid()
        else:
            return None
   

class Avoid(Scene):
    def __init__(self):
        super().__init__(
            "You dodge the bird just in time, feeling the excitement of this magical ride.\n"
            "This adventure on the broom is full of surprises!\n\n\n"
            "Tap Enter to continue.",
            image=Broom,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Wind()
        else:
            return None

class Wind(Scene):
    def __init__(self):
        super().__init__(
            "Be careful, there's a strong wind. What will you do now?\n"
            "Do you want to get down from this broom?\n\n\n"
            "Tap (1) For: Yes\n"
            "Tap (0) For: No",
            image=wind,
            actions=["yes", "no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return NotbromScene()
        elif action == "no":
            return Amazone()
        else:
            return None


class Amazone(Scene):
    def __init__(self):
        super().__init__(
            "Oh no, you're falling.\n"
            "You find yourself in a place with towering trees.\n"
            "This place is vastly different from where you were.\n"
            "It's enormous, like the Amazon.\n\n"
            "Tap Enter to continue.",
            image=amazone,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Climb()  
        else:

            return None
        
class Climb(Scene):
    def __init__(self):
        super().__init__(
            "You spot a large tree leading to a cave. You decide to climb the tree.\n\n\n\n\n"
            "Tap Enter to continue.",
            image=tree,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Treeclimb()  
        else:
            return None

class Treeclimb(Scene):
    def __init__(self):
        super().__init__(
            "The tree is so long that it takes you too much time to arrive at the cave.\n"
            "While climbing the tree, you encounter a bird with its young.\n\n\n"
            "Tap Enter to continue.", 
            image= tree ,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Attack()  
        else:
            return None
class Attack(Scene):
    def __init__(self):
        super().__init__(
            "The bird starts attacking you.\n"
            "What should you do?\n\n\n"
            "Tap (1) For: Give him food\n"
            "Tap (0) For: Kill his children",
            image= brbranch ,
            actions=["give him food", "kill his children"],
            action_key_mapping={"give him food": pygame.K_1, "kill his children": pygame.K_0},
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "give him food":
            return Good()
        elif action == "kill his children":
            return Bad()
        else:
            return None
class Bad(Scene):
    def __init__(self):
        super().__init__(
            "The bird is getting angrier, and it's attacking you more aggressively.\n"
            "What should you do?? Help yourself.\n\n\n"
            "Tap (1) For: Excuse to him and give him food\n"
            "Tap (0) For: Just fight back",
            image= brbranch,
            actions=["excuse to him and give him food", "just fightm back"],
            action_key_mapping={"excuse to him and give him food": pygame.K_1, "just fightm back": pygame.K_0},
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "excuse to him and give him food":
            return Good()
        elif action == "just fightm back":
            return Fight()
        else:
            return None    

class Fight(Scene):
    def __init__(self):
        super().__init__(
            "Try to reason with him.\n"
            "Oh no, you lost your balance.\n"
            "You're falling down from the tree.\n\n\n"
            "              <<<<GAME OVER>>>>  ",
            image = Gameover,
            sound="sounds/game-over.mp3"
        )
class Good(Scene):
    def __init__(self):
        super().__init__(
            "You helped the bird by giving it food.\n"
            "In return, the bird happily assists you in climbing the tree faster.\n\n\n"
            "Tap Enter to continue.",
            image=eat,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Turboo()  
        else:
            return None
        
class Turboo(Scene):
    def __init__(self):
        super().__init__(
            "The bird says, 'Ohoo, here is a turbo. You can use it to climb the tree, but...'\n"
            "Tap Enter to continue.",
            image = turbo,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Work()  
        else:
            return None

class Work(Scene):
    def __init__(self):
        super().__init__(
           "I'll only provide the turbo after you solve this enigma.\n\n\n\n"
           "Tap Enter to continue.",
            image = turbo,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Presence() 
        else:
            return None 
   
class Presence(Scene):
    def __init__(self):
        super().__init__(
            "Enter your answer : ",
            image= enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "oxygen"
        self.user_input = ""

    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont(self.font, 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]  
            elif event.key == pygame.K_RETURN:
                return Success() if self.user_input.lower() == self.answer else Tryagain()
            else:
                
                if pygame.key.name(event.key).isalpha():
                    self.user_input += pygame.key.name(event.key).lower()
        return self
    
class Tryagain(Scene):
    def __init__(self):
        super().__init__(
            "You will continue without the turbo.\n"
            "The tree will never end, and you will never arrive at the cave.\n\n"
            "Tap Enter to put your answer.",
            image=enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "oxygen"
        self.user_input = ""
    
    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont("Arial", 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]  
            elif event.key == pygame.K_RETURN:
                return Success() if self.user_input.lower() == self.answer else Trya()
            else:
                
                if pygame.key.name(event.key).isalpha():
                    self.user_input += pygame.key.name(event.key).lower()
        return self

class Success(Scene):
    def __init__(self):
        super().__init__(
            """
            "You will continue without the turbo."
            "The tree will never end, and you will never arrive at the cave.\n\n\n"

            Tap Enter to put your answer.
            """,
            image=dbcave,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Cave()  
        else:
            return None  
        
class Cave(Scene):
    def __init__(self):
        super().__init__(
            """
            As you arrive at the cave, a sense of accomplishment fills you: "You arrived at the cave, finally!!" 
            But amidst the darkness, the sound of bats echoes faintly. Ignoring the eerie noise, you press on, determined to explore further...
            You walk cautiously through the winding passages, the echoes of your footsteps mingling with the distant sounds of dripping water. The cave seems endless as you continue your journey... 

            Tap Enter to continue
            """,
            image=cave,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Sound()  
        else:
            return None
        
class Sound(Scene):
    def __init__(self):
        super().__init__(
            """
            As the roar of a bear reaches your ears, your heart skips a beat: "You heard the sound of the bear roaring." 
            A massive creature charges toward you, its ferocity undeniable: "A big bear was running toward you." 
            Panic sets in as you realize there's no escape route: "Oh no, what to do? There is no way to escape." 

            Tap Enter To continue.
            """,
            image=bear,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/tiger-roar-loudly-193229.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Startfight()  
        else:
            return None
        
class Startfight(Scene):
    def __init__(self):
        super().__init__(
            """
            >>> START FIGHITING >>>\n\n
            Tap Enter to continue.
            """,
            image=bear,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return FightBear()  
        else:
            return None
        

class Trya(Scene):
    def __init__(self):
        super().__init__(
            """
            You tried enough, do you still want to try?

            Type (1) for Yes
            Type (0) for No
            """,
            image=enigma,
            actions=["yes", "no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0},
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return Tyag()
        elif action == "no":
            return Try()
        else:
            return None      
    
class Tyag(Scene):
    def __init__(self):
        super().__init__(
            "Try again  \n\nEnter your answer:",
             image=enigma,
             actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "oxygen"
        self.user_input = ""
    
    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont("Arial", 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]  
            elif event.key == pygame.K_RETURN:
                return Success() if self.user_input.lower() == self.answer else Try()
            else:
                
                if pygame.key.name(event.key).isalpha():
                    self.user_input += pygame.key.name(event.key).lower()
        return self   

class Try(Scene):
    def __init__(self):
        super().__init__(
            "The tree is so long that it takes you too much time to arrive at the cave. \n"
            "While climbing the tree, you encounter a bird with its young. \n\n\n"
            "Tap Enter to continue...",
    
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return LosePoints()  
        else:
            return None
        
class LosePoints(Scene):
    def __init__(self):
        super().__init__(
            "<<You used 3 points.>>\n"
            "Oh, you finally arrived at the cave \n\n\n\n"
            "Tap Enter To continue." ,
            image=dbcave,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Cave()  
        else:
            return None
        
class FightBear(Scene):
    def __init__(self):
        super().__init__(
            "Oh No! You're fighting against a BIG BEAR . \n"
            "To win against the bear, you have to roll a higher number on the dice.\n"
            "Press Enter To roll the dice.",
            image = dé ,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/dice.mp3"
        )

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return self.handle_enter_key()
        return None

    def handle_enter_key(self):
        player_roll = random.randint(1, 6)
        bear_roll = random.randint(1, 6)
        result_text = f"You rolled a {player_roll}.\nThe bear rolled a {bear_roll}.\n"
        if player_roll > bear_roll:
            result_text += "Congratulations! You won against the bear."
            return Scene38()  
        elif player_roll < bear_roll:
            result_text += "Sorry, you lost against the bear. \n\nGame Over"
        else:
            result_text += "It's a tie!"
            return Tie()
        return Result(result_text)
    
class Result(Scene):
    def __init__(self, result_text):
        super().__init__(result_text)
        self.result_text = result_text  
    
        return None
    def handle_enter_key(self):
        return FightBear()  
    

class Tie(Scene):
    def __init__(self):
        super().__init__(
            "Dom Dom it's a tie XD"
            " \n\n\nTap Enter To Try again.",
            image= tryagain,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return FightBear()
        else:
            return None       
#######################################manel###############################################################
class Scene38(Scene):
    def __init__(self):
        super().__init__(
            "You red the enigma writting in the wall of the cave, it says: \n"
            "'The first box is in the left of the third one, the fourth one is in the right of the second one,\n"
            "and the first one is in the right of the fourth. How are the boxes organised??\n "
            "Tap enter to write your answer !",
            image=image4,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action =="next":
            return Scene38answer()
        else :
            return None

class Scene38answer(Scene):
   def __init__(self):
        super().__init__(
            "Tap your answer : ",
            image= enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "2413"
        self.user_input = ""

   def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont(self.font, 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

   def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                return Scene39() if self.user_input.lower() == self.answer else Scene39B()
            else:
                # Check if the pressed key is alphanumeric
                if event.unicode.isalnum():
                    self.user_input += event.unicode.lower()
        return self  


class Scene39B(Scene):
    def __init__(self):
        super().__init__(
            "Try again XD \n"
            "please Tap enter to write your answer !",
            image=image6,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN},
            sound="sounds/oops.mp3"
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action =="next":
            return Scene38answer()
        else :
            return None

class Scene39(Scene):
    def __init__(self):
        super().__init__(
            "\n******************************\n    CONGRATULATIONS!    \n******************************\nYou have gained 3 points!\n******************************\n",
        
            image=image2,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene40()

        else:
            return None



class Scene40(Scene):
    def __init__(self):
        super().__init__(
            "Finnaly you're getting out from the cave \(^^)/.""There are  some golden pieces in the walls. \nDo you want to take some ?\nTap (1) For :Yes\nTap(0) For :No  ",
            image=image2,
            actions=["yes","no"],
            action_key_mapping={"yes": pygame.K_1, "no": pygame.K_0},

        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "yes":
            return Random()
        elif action == "no":
            return Scene41()
        else:
            return None

class Random(Scene):

    def __init__(self):
        random_number = random.randint(1, 15)
        if random_number < 8 :
         super().__init__(
            "Oh noo this gold is so precious,the cave ruined into your head. \n\n   <<<<<<GAME OVER !!>>>>>",
            image=image5,
            actions=[],
            action_key_mapping={},
            sound = "sounds/game-over.mp3"
         )
        elif random_number > 8 :
         super().__init__(
            "Oho the gold you get turns into points!!! \nYou got three additional points. \nTap Enter To Continue......",
            image=image2,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound = "sounds/points.mp3"
         )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene41()
        else:
            return None



class Scene41(Scene):
    def __init__(self):
        super().__init__(
            "You arrived to the end of the cave, you noticed a big sphinx with the body of a human and the face of a horse. \nDo you want to go there or just avoid him? \n Tap (1) For : go to the sphinix \nTap (0) For : Avoid the sphinix ",
            image=image3,
            actions=["yes","no"],
            action_key_mapping={"yes":  pygame.K_1, "no": pygame.K_0},
         )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "no":
            return Scene41B()
        elif action == "yes":
            return Scene42()
        else:
            return None

class Scene41B(Scene):
    def __init__(self):
        super().__init__(
            "There is nothing other to do!! You have to go to the sphinx \and see what he will said...\nMaybe he's kind (^^) \nTap Enter to continue.... ",
            image=image3,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},

        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene42()
        else:
            return None


class Scene42(Scene):
    def __init__(self):
        super().__init__(
            "When you went there, he didn't let you pass: 'You can't pass unless you solve this enigma' \n\nTap enter to continue...",
           image = image3 ,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene43()  # Scene ends here
        else:
            return None


class Scene43(Scene):
    def __init__(self):
        super().__init__(
            "What is this word ?? \n . - .... . .-. .. .- ",
            image = image8,
            actions=[],
            action_key_mapping={}
        )
        self.answer = "etheria"
        self.user_input = ""

    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont("Arial", 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                return Scene44() if self.user_input.lower() == self.answer else Scene43B()
            else:
                # Check if the pressed key is alphanumeric
                if event.unicode.isalnum():
                    self.user_input += event.unicode.lower()
        return self
class Scene43B(Scene):
 
    def __init__(self):
        super().__init__(
            "<<<<Try again>>>> \nplease Tap enter to write your answer !",
            image=image6,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN},
            sound="sounds/oops.mp3"
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action =="next":
            return Scene43()
        else :
            return None


class Scene44(Scene):
    def __init__(self):
        super().__init__(
            " CONGRATULATIONS!!\(OO)/ \nThe third letter is 'I', now you can go :). Good luck in your road. \nTap Enter to continue.....",
            image = image7,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene45()# Scene ends here
        else:
            return None

class Scene45(Scene):
    def __init__(self):
        super().__init__(
            "You start getting away from the cave and finnaly you saw the door \nyou were searching for. The big door will take you back to your home. \nTap Enter to continue....",
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene46()# Scene ends here
        else:
            return None


class Scene46(Scene):
    def __init__(self):
        super().__init__(
            "You are running to that door..... scared from any other surprise.\n \n \nTap ENTER to continue....",
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene47()
        else:
            return None

class Scene47(Scene):
    def __init__(self):
        super().__init__(
            "You're finnaly in front of the door but wait it's closed X(.\nYou saw something like a lock where you enter a pin code. \n< > < > < > < > < > < > < >  \nTap ENTER to continue.... ",
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene48()
        else:
            return None



class Scene48(Scene):
    def __init__(self):
        super().__init__(
            "What do you want to do ?.\n1/ Search for a hint in the door. \n2/ Use a tree branch to broke the door.\nTap (1 or 2) to pick your choice ",
            actions=["one","two"],
            action_key_mapping={"one": pygame.K_1 , "two": pygame.K_2}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return Scene49()
        elif action == "two":
            return Scene48B()
        else:
            return None

class Scene48B(Scene):
    def __init__(self):
        super().__init__(
            "Oops the door can't be broke. T.\n1/ Search for a hint in the door. \n2/ Use a tree branch to broke the door.\nTap (1 or 2) to pick your choice",
            actions=["one","two"],
            action_key_mapping={"one": pygame.K_1 , "two": pygame.K_2}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return Scene49()
        elif action == "two":
            return Scene48B()
        else:
            return None


class Scene49(Scene):
    def __init__(self):
        super().__init__(
            "you looked in the door and you find somthing saying: \n 'The letters are numbers and the numbers are pins, in this land the magic wins.' \nTape enter to write your answer !",
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN}
        )

    def handle_input(self, event):
     action = super().handle_input(event)
     if action == "next":
       return Scene49answer()
     else :
         return None 


class Scene49answer(Scene):
  def __init__(self):
        super().__init__(
            "Enter your answer : ",
            image= enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer =  "520851891"
        self.user_input = ""

  def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont("Arial", 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

  def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                return Scene50() if self.user_input.lower() == self.answer else Scene49B()
            else:
                # Check if the pressed key is alphanumeric
                if event.unicode.isalnum():
                    self.user_input += event.unicode.lower()
        return self

class Scene49B(Scene):
    def __init__(self):
        super().__init__(
            "<<<<Try again>>>.XD\n\nTap enter to write your answer!",
            image=image6,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN},
            sound="sounds/oops.mp3"
        )

    def handle_input(self, event):
     action = super().handle_input(event)
     if action == "next":
       return Scene49answer()
     else :
         return None 



class Scene50(Scene):
    def __init__(self):
        super().__init__(
            "*************Congratulations!!!************* \n",
            image=image2,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )





#######################################ibtissem############################################################    
    ## my first scene ##
class NotbromScene(Scene):
    def __init__(self):
        super().__init__(
            "You decided to not continue with the Broom,\nBut now you're confused on how to go to that Door\nYou layed down in the earth and looked up in the sky.\nTap enter continue...",
            image=pygame.image.load("images/Nuvem no céu com estilo pixel art _ Vetor Premium.jpg"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return FlowerScene()
        else:
            return None


#########################################################################################################
   ## my second scene 
class FlowerScene(Scene):
    def __init__(self):
        super().__init__(
            "\"Heeeey ! Heeeey ! do you need help??\"\nWhat was that ??? you looked around, and the only thing you saw was a plant,\nPlant : \"i can help you find the door!\".\n\"the only condition i have is to answer this enigma\"\nTap One (1) to see the enigma",
            image=pygame.image.load("images/téléchargement (23).jpg"),
            actions=["one"],
            action_key_mapping={"one": pygame.K_1}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return FlowerEnigma()
        else:
            return None

    
#########################################################################################################
   ## my Third scene 
class FlowerEnigma(Scene):
   
    def __init__(self):
       
        super().__init__(
            "Enigma : \"The first box is in the left of the third one, the fourth one\nis in the right of the second one and the first one is in the right of \nthe fourth one \",\nhow are the boxese organized ?\n\n\n\n Please Tap enter you give your answer",
            image=pygame.image.load("images/Frame 1707478366 (5).png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return floweranswer ()
        else:
            return None

    def show(self):
        woods_sound = pygame.mixer.Sound("sounds/theres-something-about-this-room-201112.mp3")
        woods_sound.play()
        woods_sound.play()
#########################################################################################################
class floweranswer(Scene):
   def __init__(self):
        super().__init__(
            "Enter your answer : ",
            image= enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "2413"
        self.user_input = ""

   def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont("Arial", 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

   def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                return FlowerHappy() if self.user_input.lower() == self.answer else FlowerError()
            else:
                # Check if the pressed key is alphanumeric
                if event.unicode.isalnum():
                    self.user_input += event.unicode.lower()
        return self
#########################################################################################################
   ## my Fourth scene 
class FlowerHappy (Scene):
    def __init__(self):
        super().__init__(
            "Plant : \"Great answerrr, hohooo! now i can tell you about the door but first \nThere is a letter you have to remebre until the end of the game \nThe letter is : \'E\' \" \n\"The door is  after these woods follow them and you will find a big castel,\nPass the castel you will find the door XD ",
            image=image1,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return SlidingDoor()
        else:
            return None

   
####################################################################################################
class FlowerError(Scene):
    def __init__(self):
       
        super().__init__(
            "Oppss... oh noo you typped the wrong answerr X(!!! \nWhat to do now ? \nLet\'s try againn :) \ntap (1)",
            image=image1,
            actions=["one"],
            action_key_mapping={"one": pygame.K_1},
            sound="sounds/oops.mp3"
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return floweranswer()
        else:
            return None
 
   
####################################################################################
class SlidingDoor(Scene):

    def __init__(self):
        
        super().__init__(
           "By walking through the woods, you suddenly saw a sliding door\nit opens ... and close ... open... close...\nTo walk to that door tap (1) ",
           image=image1,
            actions=["one"],
            action_key_mapping={"one": pygame.K_1}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return Doorclosed()
        else:
            return None

    
    
#####################################################################################################
class Doorclosed(Scene):
    def __init__(self):
        
        super().__init__(
           "Once you arrived to that door, its open. You get in, andddd.... !!!! \nohhhh noo you are stucked therexxxxx\nThere is nowhere to escape the door is closed,\nif you want to walk around tap (enter)",
            image=image1,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Wlakingaround()
        else:
            return None

    


#############################################################################################
class Wlakingaround(Scene):
    def __init__(self):
        
        super().__init__(
            "You started discovering what is this place, is this a train ?? in the woods !! how can this be possible ?\n but then you remembered you are in magic land so you didn't care \nTo continue searching tap (enter)",
            image=image1,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return StrangSmell()
        else:
            return None

   
###########################################################################################################################3333
class StrangSmell(Scene):

    def __init__(self):
        
        super().__init__(
            "TOOOT TOOOOOTT ... THE  SOUND OF ALERTS IN THE TRAIN \n FILL THE AIR ...  What is this smell?? \noh oh oh YOU CAN'T BREAAATH, This is a toxic gaze.\nto break the door tap (1)\nto search the source of the gaze tap (2)",
            image=image1,
            actions=["one","two"],
            action_key_mapping={"one": pygame.K_1 ,"two": pygame.K_2}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return BreakDoor()
        elif action =="two":
            return SearchScene()
        else:
            return None 

   

class BreakDoor(Scene):

    def __init__(self):
        
        super().__init__(
            "The Door are so secure, you broked your hand !! \nHurry up the gaze will KILL you,\nIf you wanna recover (cost: 2 pnts) Tap (1)\nDo you wanna search the source of the smell tap(2)" ,
            image=image1,
            actions=["one","two"],
            action_key_mapping={"one": pygame.K_1 ,"two": pygame.K_2}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            super().add_sub_score(-2)
            return Recover()
        elif action == "two":
            return SearchScene()
        else:
            return None

   
##############################################################################################
class Recover(Scene):
    points= points -2
    def __init__(self):
        
        super().__init__(
            "You are recovered now total points :  "+ score +"\nTap (enter) to search the source of the smell",
            image=image1,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return SearchScene()
        else:
            return None

    
#####################################################################################################
class SearchScene(Scene):

    def __init__(self):
        
        super().__init__(
            "You checked around, There is a gaze pipes do you wanna follow them ?\n\n\n\n\n\nTo follow them tap (enter)",
             image=image1,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN}
            
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Gazepipes()
        else:
            return None


#######################################################################################################
class Gazepipes(Scene):

    def __init__(self):
        
        super().__init__(
            "ohh here is the source of the gaze, YOU FOUND A LEAKING GAZE PIPES ,\n In front of you there is a paper (1), peace of wood (2) and mask (3) \n what do you want to take? ",
             image=image1,
            actions=["one","two","three"],
            action_key_mapping={"one": pygame.K_1 ,"two": pygame.K_2,"three": pygame.K_3}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return Paper()
        elif action == "two":
            return Peaceofwood()
        elif action == "three":
            return mask()
        else:
            return None

#############################################################################################################################################33
class Peaceofwood(Scene):

    def __init__(self):
        
        super().__init__(
            "You took the peace of wood, do you want to :\nBreak the gaze pipe (1) \nTake the paper instead (2) \nTake the mask instead (3)",
             image=image1,
            actions=["one","two","three"],
            action_key_mapping={"one": pygame.K_1 ,"two": pygame.K_2,"three": pygame.K_3}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return gazeDie()
        elif action == "two":
            return Paper()
        elif action == "three":
            return mask()
        else:
            return None

#############################################################################################################################################33
class gazeDie(Scene):
    def __init__(self):
        
        super().__init__(
            "The gaze start leaking so fast, you couldn't breath....\nIT WAS A TOXIC GAZE \nYOU ........ DIED X(\n\nYOU WANT TO RESTART TAP (R) ",
            image=image1,
            actions=["restart"],
            action_key_mapping={"restart": pygame.K_r},
            sound="sounds/game-over.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "restart":
            return NotbromScene()
        else:
            return None



#######################################################################################################
class mask(Scene):

    def __init__(self):
        
        super().__init__(
            "You took the mask! you are half secure \nThe mask is (mou9ata3) the gaze may kill you \nBECAREFULL ,\nwhat do you want to take now ? \nTap (1) For : The paper\nTap (2) For :peace of wood",
             image=image1,
            actions=["one","two"],
            action_key_mapping={"one": pygame.K_1 ,"two": pygame.K_2,}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "one":
            return Paper()
        elif action == "two":
            return Peaceofwood()

        else:
            return None


#######################################################################################################
class Paper(Scene):
    def __init__(self):
        
        super().__init__(
            "Once you took the paper you notice something written there \n\"SOLVE THIS EGNIGMA TO STOP THE GAZE\"\n\" I'm alwyas in front of you but you can never see me... \nYou use me everyday yet you hardly notice me who am i? \" \nTap enter to write te answer",
            image=image1,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN}
        )
   
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return TapEnigma()
        else:
            return None

  
#######################################################################################################
class TapEnigma(Scene):
  def __init__(self):
        super().__init__(
            "Tap your answer : ",
            image= enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "oxygen"
        self.user_input = ""

  def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont(self.font, 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

  def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]  
            elif event.key == pygame.K_RETURN:
                return helloScene() if self.user_input.lower() == self.answer else Tryagain()
            else:
                
                if pygame.key.name(event.key).isalpha():
                    self.user_input += pygame.key.name(event.key).lower()
        return self


########################################################LINA#############################################################
class  helloScene(Scene):
    def __init__(self):
        super().__init__(
            "The door opens,\nand the oxigen fill the train now you are breathing normally escape the train \n\n\n      Tap ENTER to continue",
            image=pygame.image.load("images/train.jpg"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return aftertrain()
        else:
            return None

##
class  aftertrain(Scene):
    def __init__(self):
        super().__init__(
            "When you step out of the train, \nyou notice that it isn't the area where you were, \nthe train moved when you get out, but now you can see the castle the flower informed you about. \n\n          Tap ENTER t go to the castle. ",
            image=pygame.image.load("images/castle (1).png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return aftercastle()
        
        else:
            return None

        
class  aftercastle(Scene): 
    def __init__(self):
        super().__init__(
            "When you arrive at the castle\n, there is a large golden door that is so big that you can barely see it's end. \nIt is written there\n: 'if you arrived to the castle, so for sure you solved three enigmas, \nand you have two letters in your hand, \ngive me the two letters and I'll give you the third one and let you in.' \nTap enter to write the letters",
            image=pygame.image.load("images/golden door (1).png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return theletters()
        else:
            return None
class theletters(Scene):
  def __init__(self):
        super().__init__(
            "The letters : ",
            image= enigma,
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
        self.answer = "e r"
        self.user_input = ""

  def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont("Arial", 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

  def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                return inthecastle() if self.user_input.lower() == self.answer else thelettersagain()
            else:
                # Check if the pressed key is alphanumeric
                if event.unicode.isalnum():
                    self.user_input += event.unicode.lower()
        return self    


class thelettersagain(Scene):
    def __init__(self):
        super().__init__(
            "<<<<Try again>>>>XD \n\nTap enter to write your answer!",
            image=image6,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN},
            sound="sounds/oops.mp3"
        )

    def handle_input(self, event):
     action = super().handle_input(event)
     if action == "next":
       return theletters()
     else :
         return None 


        
class inthecastle(Scene):

    def __init__(self):
        super().__init__(
            "Welcome to the castle where everything is made of gold! **<>**.\nIf you touch anything, the castle will shatter on your head .\n\n\n     Tap ENTER to continue..",
            image=pygame.image.load("images/téléchargé (1).png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )

    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return puzzle()
        else:
            return None
        

class puzzle(Scene):
    
    def __init__(self):
        super().__init__(
            "As you walk through the castle, you hear a strange sound echoing through the halls.\nYou realize you are trapped with no way to escape.\n\nI may help you if you help me solve this enigma,a mysterious voice whispers.\n\nWhat is this word: .-.. .. -.- .-?\n\nTap Enter to write the answer!",
            image=pygame.image.load("images/morse code (1).png"),
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return puzzekanswer()
        else:
            return None
        
       
        ####manque des images 
class puzzekanswer(Scene):
    def __init__(self):
        super().__init__(
            "What is this word ?? \n . - .... . .-. .. .- ",
            image = image8,
            actions=[],
            action_key_mapping={}
        )
        self.answer = "etheria"
        self.user_input = ""

    def draw(self, screen):
        super().draw(screen)
        font = pygame.font.SysFont(self.font, 17)
        user_input_surface = font.render(self.user_input, True, 'white')
        screen.blit(user_input_surface, (10, 430))  

    def handle_input(self, event):
        action = super().handle_input(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            elif event.key == pygame.K_RETURN:
                return afterpuzzle() if self.user_input.lower() == self.answer else Scenepuzzel()
            else:
                # Check if the pressed key is alphanumeric
                if event.unicode.isalnum():
                    self.user_input += event.unicode.lower()
        return self

class Scenepuzzel(Scene):
 
    def __init__(self):
        super().__init__(
            "<<<<Try again>>>> XD \nplease Tap enter to write your answer !",
            image=image6,
            actions=["next"],
            action_key_mapping={"next":pygame.K_RETURN},
            sound="sounds/oops.mp3"
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action =="next":
            return puzzekanswer()
        else :
            return None

    
class afterpuzzle(Scene):
    
    def __init__(self):
        super().__init__(
            "the third letter is \"I\"\ncongratulations the castle door is opened",
            image=pygame.image.load("images/image kharita1.png"),##image ta3 bab mftouh
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN},
            sound="sounds/right-answer.mp3"
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return dooropened()
        else:
            return None
        
class dooropened(Scene):

    def __init__(self):
        super().__init__(
            "After the castle door opened, you ran to the large door you had been looking for,  that will take you to your home , \nHowever, you were still confused as to why you needed these letters. \nWhy do they tell me to memorize and give me these letters over and over again?",
            image=pygame.image.load("images/golden door (1).png"),##image ta3 bab ftouh
            actions=["next"],
            action_key_mapping={"next": pygame.K_RETURN}
        )
    def handle_input(self, event):
        action = super().handle_input(event)
        if action == "next":
            return Scene47()
        else:
            return None


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


image1 = pygame.image.load("images/téléchargement (19).png")
current_scene =background()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alone In Etheria")

running = True
while running:
    screen.fill('black')
    current_scene.draw(screen)
    scene_name = type(current_scene).__name__    #recuperer le nom de la scene courrante String
    button.draw(screen , joueur, score, scene_name)
    popup.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        next_scene = current_scene.handle_input(event)

        if next_scene:
            current_scene = next_scene
            
    pygame.display.flip()
    

pygame.quit()