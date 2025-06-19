from kivymd.app import MDApp
from kivymd.uix.screen import Screen,MDScreen
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager 
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton,MDIconButton,MDFillRoundFlatIconButton
from kivy.animation import Animation
import random
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.metrics import dp, sp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivymd.uix.list import BaseListItem,IRightBodyTouch,OneLineListItem,ThreeLineListItem,OneLineRightIconListItem
#from kivmob import KivMob, TestIds
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.graphics.instructions import Canvas
from kivy.graphics import Rectangle, Color
#requires:
#kivymd=1.2.0

from kivy.utils import platform
from kivy.core.window import Window


if platform in ("win", "linux", "macosx"):  # Desktop testing only
    Window.size = (360, 660)




screen_helper='''
<StoreItem>:
    Image:
        source:'scoin.png'

            
    
<About>:
    size_hint_y:0.4
    MDLabel:
        text:app.about
        pos_hint: {"x": 0.1, "center_y": 0}

<DarkModeCard>:
    no_ripple_effect:True
    IconLeftWidget:
        icon:'white-balance-sunny'
    RightSwitch:
        pos_hint: {"center_x": 0, "center_y": 0.37}
        on_active:
            app.theme_change() if self.parent.parent.text == 'Dark Mode' else root.callback(self) 

ScreenManager:
    HomeScreen:
    GameScreen:



<HomeScreen>:
    name:'HomeScreen'
    MDFloatLayout:
        MDScreenManager:
            id:screen_manager

            
            Home:
            Rewards:                  
            Setting:
            Store:     
            Missions:
                    
        
        MDFloatLayout:
            opacity:0 if root.ids.screen_manager.current=='Settings' else 1   
            canvas:
                Color:
                    rgba: (0, 0, 0, 0.7) if self.theme_cls.theme_style == "Light" else (1,1,1,0.85)
                RoundedRectangle:
                    pos: (self.width*0.75,self.height*0.92)
                    size: (self.width*0.23,self.height*0.033)
                    radius:5,5,5,5
                
                RoundedRectangle:
                    pos: (self.width*0.45,self.height*0.92)
                    size: (self.width*0.23,self.height*0.033)
                    radius:5,5,5,5
            Image:
                source:'scoin.png'
                size_hint:(0.09,0.09)
                pos_hint: {"center_x": .75, "center_y": .937}
            
            Image:
                source:'coin.png'
                size_hint:(0.09,0.09)
                pos_hint: {"center_x": .45, "center_y": .937}

            MDLabel:
                id: scoin
                color:(1,1,1,1) if self.theme_cls.theme_style == "Light" else (0,0,0,1)
                text:str(app.scoin)
                font_name:'comicbd.ttf'
                pos_hint: {"center_x": 1.31, "center_y": .938}
            
            MDLabel:
                id: coin
                color:(1,1,1,1) if self.theme_cls.theme_style == "Light" else (0,0,0,1)
                text:str(app.coin)
                font_name:'comicbd.ttf'
                pos_hint: {"center_x": 1.01, "center_y": .938}
        
                
        
        
        MDIconButton:
            id:SettingsButton
            name:'Settings'
            icon:'cog-outline'
            icon_size:'30dp'
            pos_hint:{'center_x':0.10,'center_y':0.05}
            on_release:
                root.switch(self)
                self.icon='cog'
        
        MDIconButton:
            id:StoreButton
            name:'Store'
            icon:'cart-outline'
            icon_size:'30dp'
            pos_hint:{'center_x':0.30,'center_y':0.05}
            on_release:
                root.switch(self)
                self.icon='cart'

        MDIconButton:
            id: HomeButton
            name:'Home'
            icon:'home'
            icon_size:'30dp'
            pos_hint:{'center_x':0.5,'center_y':0.05}
            on_release:
                root.switch(self)
                self.icon='home'        

        MDIconButton:
            id:RewardsButton
            name:'Rewards'
            icon:'treasure-chest-outline'
            icon_size:'30dp'
            pos_hint:{'center_x':0.70,'center_y':0.05}
            on_release:
                root.switch(self)
                self.icon='treasure-chest'

        MDIconButton:
            id:MissionsButton
            name:'Missions'
            icon:'trophy-outline'
            icon_size:'30dp'
            pos_hint:{'center_x':0.90,'center_y':0.05}
            on_release:
                root.switch(self)
                self.icon='trophy'

<Home>:
    name:'Home'
    
    Image:
        id: image
        source: 'Game01logo(White).png'
        size_hint:(1,1)
        pos_hint: {"center_x": .5, "center_y": .70}
        fit_mode:"fill"

    MDIconButton:
        id: play
        icon:'play'
        icon_size:'50sp'
        md_bg_color: [0,1,0.43,1]
        opacity:1
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: (0.45,.08)
        on_release:
            app.root.transition.direction = 'left'
            app.root.current='Game'
            app.gamestart()

    MDFillRoundFlatButton:
        id:howtoplay
        text:'HOW TO PLAY'
        text_color:'black'
        font_style:"H6"
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint: (.45,.08)
        md_bg_color:[0.36,0.88,0.90,1]
        opacity:1
        
        on_release: app.show_rules()

    MDLabel:
        id: Highest_Score_display
        text:("HIGHEST SCORE: "+str(app.highscore))
        theme_text_color:"Custom"
        text_color:(1,0,0,1)
        opacity:0
        font_style:"H5"
        pos_hint:{'center_x':0.5,'center_y':0.74}
        halign:'center'

        

<Setting>:
    name:'Settings'

    MDFloatLayout:
        MDLabel:
            text:'Settings'
            halign:'center'
            font_name:'comicbd.ttf'
            font_size:'30sp'
            pos_hint:{'center_x':0.5,'center_y':0.9}

        ScrollView:
            size_hint_y:.7
            pos_hint:{'center_x':0.5,'center_y':0.5}
            MDList:
                id:settings_list
                spacing:15
                

                DarkModeCard:
                    text:'Dark Mode'
                    

<Store>:
    name:'Store'

    ScrollView:
        size_hint_y:0.9
        MDList:
            id: StoreList
            spacing:30
            
            OneLineListItem:
                text : 'jkhjkh'
            MDCard:
                padding: 10
                size_hint: None, None
                size: "350dp", "100dp"

                MDRelativeLayout:
                    MDLabel:
                        id: label
                        text: "Coins"
                        
                        color: "grey"
                        halign: 'center'
                        
                        bold: True
            MDCard:
                padding: 4
                size_hint: None, None
                size: "100dp", "100dp"

                MDRelativeLayout:

                    MDIconButton:
                        icon: "dots-vertical"
                        pos_hint: {"top": 1, "right": 1}

                    MDLabel:
                        id: label
                        text: "yoyo"
                        adaptive_size: True
                        color: "grey"
                        pos: "12dp", "12dp"
                        bold: True
            MDGridLayout:
                cols:3
                MDCard:
                    padding: 4
                    size_hint: None, None
                    size: "100dp", "100dp"

                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            id: label
                            text: "yoyo"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
                MDCard:
                    padding: 4
                    size_hint: None, None
                    size: "100dp", "100dp"

                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            id: label
                            text: "yoyo"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
                MDCard:
                    padding: 4
                    size_hint: None, None
                    size: "100dp", "100dp"

                    MDRelativeLayout:

                        MDIconButton:
                            icon: "dots-vertical"
                            pos_hint: {"top": 1, "right": 1}

                        MDLabel:
                            id: label
                            text: "yoyo"
                            adaptive_size: True
                            color: "grey"
                            pos: "12dp", "12dp"
                            bold: True
                
            StoreItem:
            

                      
<temp>:
    ScrollView:
        size_hint_y:0.8
        pos_hint:{'center_x':0.5,'center_y':0.5}
        MDGridLayout:
            cols:3
            id: list2
            
            MDCard:
                text:'yuu'


            
            
                    
                
            



<Rewards>:
    name:'Rewards'
    MDLabel:
        text:'Rewards'
    MDProgressBar:
        id: progress
        value:50
        size_hint: (0.85,0.025)
        pos_hint:{'center_x':0.5,'center_y':0.7}

    MDRaisedButton:
        text:'up'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:self.parent.ids.progress.value+=10
    MDRaisedButton:
        text:'downn'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_press:self.parent.ids.progress.value-=10
    
    MDFloatLayout:
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.95,0.12)
        canvas:
            Color:
                rgba: (0, 0, 0, 0.7)
            RoundedRectangle:
                pos: (self.width*0.025,self.height*0.5)
                size:(self.width,self.height)
                radius:5,5,5,5
        


        
<Missions>:
    name:'Missions'
    MDLabel:
        text:'Missions2'
    MDFloatLayout:   



           

    


<GameScreen>:
    name: 'Game'
            

    MDRelativeLayout:

        MDFillRoundFlatIconButton:
            id:pause
            text: 'Home'
            icon: 'home'
            pos_hint: {"center_x":0.30,"center_y": .2}
            on_press:
                app.home()

        MDFillRoundFlatIconButton:
            id:pause
            text: 'Pause'
            icon: 'pause-box'
            pos_hint: {"center_x":0.70,"center_y": .2}
            on_press:
                app.pause()
                


        MDFloatingActionButton:
            id:1
            text:'1'
            pos_hint:{'center_x':0.25,'center_y':0.65}
            on_release:app.button_press(app.root.get_screen('Game').ids['1'])
        
        MDFloatingActionButton:
            id:2
            text:'2'
            pos_hint:{'center_x':0.5,'center_y':0.65}
            on_release:app.button_press(app.root.get_screen('Game').ids['2'])
        
        MDFloatingActionButton:
            id:3
            text:'3'
            pos_hint:{'center_x':0.75,'center_y':0.65}
            on_release:app.button_press(app.root.get_screen('Game').ids['3'])
        
        MDFloatingActionButton:
            id:4
            text:'4'
            pos_hint:{'center_x':0.25,'center_y':0.5}
            on_release:app.button_press(app.root.get_screen('Game').ids['4'])

        MDFloatingActionButton:
            id:5
            text:'5'
            pos_hint:{'center_x':0.5,'center_y':0.5}
            on_release:app.button_press(app.root.get_screen('Game').ids['5'])

        MDFloatingActionButton:
            id:6
            text:'6'
            pos_hint:{'center_x':0.75,'center_y':0.5}
            on_release:app.button_press(app.root.get_screen('Game').ids['6'])

        MDFloatingActionButton:
            id:7
            text:'7'
            pos_hint:{'center_x':0.25,'center_y':0.35}
            on_release:app.button_press(app.root.get_screen('Game').ids['7'])

        MDFloatingActionButton:
            id:8
            text:'8'
            pos_hint:{'center_x':0.5,'center_y':0.35}
            on_release:app.button_press(app.root.get_screen('Game').ids['8'])

        MDFloatingActionButton:
            id:9
            text:'9'
            pos_hint:{'center_x':0.75,'center_y':0.35}
            on_release:app.button_press(app.root.get_screen('Game').ids['9'])

        MDLabel:
            id:Score_display
            text:("SCORE: "+str(app.score))
            pos_hint:{'center_x':0.5,'center_y':0.94}
            halign:'center'
            theme_text_color:"Custom"
            text_color:(0,1,0,1)
            font_style:"H6"
        
        MDIcon:
            icon:'clock'
            pos_hint:{'center_x':0.42,'center_y':0.87}

        MDLabel:
            id:Time_display
            text:("01:00")
            pos_hint:{'center_x':0.54,'center_y':0.87}
            halign:'center'
            font_style:"H5"

        
        
'''
class StoreItem(MDFloatLayout):
    pass
class temp(MDFloatLayout):
    pass
class About(MDFloatLayout):
    pass

class DarkModeCard(OneLineAvatarIconListItem):
    def callback(obj,instance):
        print('error')

class RightSwitch(IRightBodyTouch, MDSwitch):
    pass


class Home(MDScreen):
    pass

class Rewards(MDScreen):
    pass

class Setting(MDScreen):
    def on_pre_enter(self):
        self.AboutPanel=MDExpansionPanel(icon='information-outline',
                                         content=About(),
                                         panel_cls=MDExpansionPanelOneLine(text='About')
                                         )
        self.ids.settings_list.add_widget(self.AboutPanel)
    def on_leave(self):
        self.ids.settings_list.remove_widget(self.AboutPanel)   
        
class Store(MDScreen):
    pass

class Missions(Screen):
    pass


class HomeScreen(Screen):
    def switch(self,instance):
        self.ids['SettingsButton'].icon='cog-outline'
        self.ids['StoreButton'].icon='cart-outline'
        self.ids['HomeButton'].icon='home-outline'
        self.ids['RewardsButton'].icon='treasure-chest-outline'
        self.ids['MissionsButton'].icon='trophy-outline'

        
        
        if self.ids.screen_manager.current == 'Settings':
            self.ids.screen_manager.transition.direction = 'left'
            
        
        elif self.ids.screen_manager.current == 'Store':
            if instance.name == 'Settings':
                self.ids.screen_manager.transition.direction = 'right'
                
            else:
                self.ids.screen_manager.transition.direction = 'left'
                
        
        elif self.ids.screen_manager.current == 'Home':
            if instance.name == 'Settings' or instance.name == 'Store':
                self.ids.screen_manager.transition.direction = 'right'
                
            else:
                self.ids.screen_manager.transition.direction = 'left'
                

        elif self.ids.screen_manager.current == 'Rewards':
            if instance.name == 'Missions':
                self.ids.screen_manager.transition.direction = 'left'
                
            else:
                self.ids.screen_manager.transition.direction = 'right'
                

        elif self.ids.screen_manager.current == 'Missions':
            self.ids.screen_manager.transition.direction = 'right'
            
        
        else:
            print('Error')

        self.ids.screen_manager.current = instance.name
        print(instance.name)
        print(self.ids.screen_manager.current)

class GameScreen(Screen):
    pass

sm=ScreenManager()
sm.add_widget(HomeScreen(name='HomeScreen'))
sm.add_widget(GameScreen(name='Game'))

Rules = '''1) Click the green button to START the game\n
2) 9 buttons will be displayed\n
3) Click on the button which has DIFFERENT color\n
4) If CORRECT button clicked: +5\n
5) If WRONG button clicked: -10\n
6) Try to Score max in 60 seconds!!
'''
class DemoApp(MDApp):
    dialog = None
    dialog2 = None
    highscore=0
    score=0
    time_left=60
    coin=10000
    scoin=10000
    about='\n\nVersion 1.0\nMade by Yajur Chatnani\n\n'
    #green,yellow,red,blue,orange,purple
    colors=[[0,1,0.43,1],[1,0.87,0.35,1],[1, 0.3, 0.4, 0.85],[0.36, 0.88, 0.90,1],[1.00, 0.533, 0.243,1],[0.549, 0.322, 1,1]]
    def build(self):
        
        LabelBase.register(name="Comic_Sans_MS",fn_regular="comicbd.ttf")
        
        self.theme_cls.font_styles["Comic_Sans_MS"] = ["Comic_Sans_MS",16,False,0.15,]
        #self.theme_font_styles.append('Comic_Sans_MS')
        
        #self.animation()
        return Builder.load_string(screen_helper)
        
    
    def on_start(self,**kwargs):
        pass
        
        
        
        
        #self.root.get_screen('Home').ids['play'].disabled=True
        #anim = Animation(color=(1,1,1,1),duration=2)
        #anim += Animation(color=(1,1,1,0),duration=0.2)
        #anim.start(self.root.get_screen('Home').ids['postprespalsh'])
        #anim.bind(on_complete=self.anim2)
        
    
    #def anim2(self,*args):
        
    
    def anim3(self,*args):
        anim3 = Animation(opacity=0,duration=0)
        anim3 += Animation(disabled=False,duration=0)
        anim3 += Animation(opacity=1,duration=0.5)
        anim3.start(self.root.get_screen('HomeScreen').ids['play'])
        anim3.start(self.root.get_screen('HomeScreen').ids['howtoplay'])
        anim3.start(self.root.get_screen('HomeScreen').ids['Dark_switch'])

        anim4 = Animation(opacity=0,duration=0)
        anim4 += Animation(opacity=1,duration=0.5)
        anim4.start(self.root.get_screen('HomeScreen').ids['darkmodelabel'])
        if self.highscore != 0:
            anim4.start(self.root.get_screen('HomeScreen').ids['Highest_Score_display'])
        
    
        

    
    

    def show_rules(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = 'Rules',
                text = Rules,
                buttons=[MDRaisedButton(text='OK',on_release = self.rules_close)],
                radius=[10, 10, 10, 10],
                size_hint=(0.9,0.5)
                )
        
        self.dialog.open()

    def rules_close(self,obj):
        self.dialog.dismiss()

    def theme_change(self):
        if self.theme_cls.theme_style == "Light":
            self.root.get_screen('HomeScreen').ids.screen_manager.get_screen('Home').ids['image'].source='Game01logo(Black).png'
            self.theme_cls.theme_style = "Dark"
            self.root.get_screen('HomeScreen').ids.screen_manager.get_screen('Home').ids['Highest_Score_display'].text_color=[1,0.87,0.35,1]
        else:
            self.root.get_screen('HomeScreen').ids.screen_manager.get_screen('Home').ids['image'].source='Game01logo(White).png'
            self.theme_cls.theme_style = "Light"
            self.root.get_screen('HomeScreen').ids.screen_manager.get_screen('Home').ids['Highest_Score_display'].text_color=[1,0,0,1]

    def gamestart(self):
        self.score=0
        self.time_left=60
        self.root.get_screen('Game').ids['Time_display'].text = "01:00"
        self.root.get_screen('Game').ids['Score_display'].text = "SCORE: "+str(self.score)

        for button_no in range(1,9+1):
            self.root.get_screen('Game').ids[str(button_no)].disabled=False
            self.root.get_screen('Game').ids[str(button_no)].md_bg_color=self.theme_cls.primary_color

        self.button_no = random.randint(1,9)
        self.root.get_screen('Game').ids[str(self.button_no)].md_bg_color= [1, 0.3, 0.4, 0.85]

        self.root.get_screen('Game').ids['pause'].icon = 'pause-box'
        self.root.get_screen('Game').ids['pause'].text='Pause'
        Clock.unschedule(self.time_update,1)
        Clock.schedule_interval(self.time_update,1)


    
    def button_press(self,instance):
        colors=[[0,1,0.43,1],[1,0.87,0.35,1],[1, 0.3, 0.4, 0.85],[0.36, 0.88, 0.90,1],[1.00, 0.533, 0.243,1],[0.549, 0.322, 1,1]]
        if instance.text==str(self.button_no):
            self.score=self.score+5
        else:
            self.score=self.score-10

        if self.score > random.randint(20,40):
            all_color = random.choice(colors)
            colors.remove(all_color)
            odd_color = random.choice(colors)
            
        else:
            all_color = self.theme_cls.primary_color
            odd_color = [1,0.3,0.4,0.85]
        
        for button_no in range(1,9+1):
            self.root.get_screen('Game').ids[str(button_no)].md_bg_color=all_color

        self.button_no=random.randint(1,9) 
        self.root.get_screen('Game').ids[str(self.button_no)].md_bg_color=odd_color
        
        self.root.get_screen('Game').ids['Score_display'].text = "SCORE: "+str(self.score)

        

       
    def home(self):
        Clock.unschedule(self.time_update,1)
        self.time_left=60
        self.root.transition.direction = 'right'
        self.root.current = "HomeScreen"
   
    def pause(self):
        icon=self.root.get_screen('Game').ids['pause'].icon
        if icon == 'pause-box':
            self.dialog2=False
            Clock.unschedule(self.time_update,1)
            for button_no in range(1,9+1):
                self.root.get_screen('Game').ids[str(button_no)].disabled=True
            self.root.get_screen('Game').ids['pause'].icon='play-box'
            self.root.get_screen('Game').ids['pause'].text='Resume'
        else:
            self.dialog2 = True
            Clock.schedule_interval(self.time_update,1)
            for button_no in range(1,9+1):
                self.root.get_screen('Game').ids[str(button_no)].disabled=False
            self.root.get_screen('Game').ids['pause'].icon='pause-box'
            self.root.get_screen('Game').ids['pause'].text='Pause'
        
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title = 'Game paused',
                buttons=[MDIconButton(icon='home',text='Home',on_release = self.Gamepause_close),
                         MDIconButton(icon='play',text='Resume',on_release = self.Gamepause_close),
                         MDIconButton(icon='restart',text='Restart',on_release = self.Gamepause_close)],
                radius=[10, 10, 10, 10],
                #size_hint=(0.9,0.5)
                )
        
            self.dialog2.open()

    def Gamepause_close(self,instance):
        self.dialog2.dismiss()
        if instance.text == 'Resume':
            self.dialog2.dismiss()

        elif instance.text == 'Restart':
            self.dialog2.dismiss()
            self.score=0
            self.time_left=60
            self.root.get_screen('Game').ids['Time_display'].text = "01:00"
            self.root.get_screen('Game').ids['Score_display'].text = "SCORE: "+str(self.score)
        else:
            #home
            self.dialog2.dismiss()
            self.root.transition.direction = 'right'
            self.root.current = "HomeScreen"
            Clock.unschedule(self.time_update,1)

        icon=self.root.get_screen('Game').ids['pause'].icon
        if icon == 'pause-box':
            Clock.unschedule(self.time_update,1)
            for button_no in range(1,9+1):
                self.root.get_screen('Game').ids[str(button_no)].disabled=True
            self.root.get_screen('Game').ids['pause'].icon='play-box'
            self.root.get_screen('Game').ids['pause'].text='Resume'
        else:
            Clock.schedule_interval(self.time_update,1)
            for button_no in range(1,9+1):
                self.root.get_screen('Game').ids[str(button_no)].disabled=False
            self.root.get_screen('Game').ids['pause'].icon='pause-box'
            self.root.get_screen('Game').ids['pause'].text='Pause'
    

    def time_update(self,obj):
        if self.time_left == 0:
            self.root.transition.direction = 'right'
            self.root.current = "HomeScreen"
            self.gameend()
        self.time_left = self.time_left-1
        temp=self.time_left
        self.time_left='%02d'%self.time_left
        self.root.get_screen('Game').ids['Time_display'].text = "00:"+ str(self.time_left)
        self.time_left=temp
    

    def gameend(self):
        Clock.unschedule(self.time_update,1)
        self.time_left=60
        if self.score > self.highscore:
            self.highscore = self.score
            self.root.get_screen('HomeScreen').ids.screen_manager.get_screen('Home').ids['Highest_Score_display'].text="HIGHEST SCORE: "+str(self.highscore)
        
        self.score = 0
        self.root.get_screen('Game').ids['Score_display'].text="SCORE: "+str(self.score)
        self.root.get_screen('HomeScreen').ids.screen_manager.get_screen('Home').ids['Highest_Score_display'].opacity=1
    
    
    

    

 
DemoApp().run()