from mapview import MapView
from mapview import MapMarker
from mapview import MarkerMapLayer
from mapview import MapMarkerPopup
from kivy.app import App
from kivy.properties import NumericProperty
from plyer import gps
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# from BusStopClubServer import BusStopClubServer
from functools import partial
import time
import threading


class tela1(FloatLayout):
    def on_press_bt1(self, *args):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(tela3())

    def on_press_bt2(self, *args):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(tela2())

    def __init__(self, **kwargs):
        super(tela1, self).__init__(**kwargs)
        bt1 = Button(text="Compartilhar localizacao do onibus", size_hint=(0.7, 0.1),
                     pos_hint={"center_x": 0.5, "center_y": 0.5},
                     on_press=self.on_press_bt1)
        bt2 = Button(text="Procurar Onibus", size_hint=(0.7, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.65},
                     on_press=self.on_press_bt2)
        self.add_widget(bt1)
        self.add_widget(bt2)


class tela2(BoxLayout):
    lat = NumericProperty(0)
    lon = NumericProperty(0)
    map = MapView()
    layer = MarkerMapLayer()
    info = FloatLayout()

    def __init__(self, **kwargs):
        super(tela2, self).__init__(**kwargs)
        self.orientation = "vertical"
        gps.configure(on_location=self.on_location)
        gps.start()
        self.map = MapView(zoom=90, lat=self.lat, lon=self.lon)
        MapMarker(lon=self.lon, lat=self.lat, source="pessoa.png", on_press=self.on_press)
        self.add_widget(self.map)
        self.map.add_widget(self.layer)
        self.bind(lon=partial(self.tracking))
        time.sleep(1)

    def tracking(self, *args):
        threading.Timer(5.0, self.tracking).start()
        self.layer.clear_widgets()
        self.layer.add_widget(MapMarker(lon=self.lon, lat=self.lat, source="pessoa.png", on_release=self.on_release,
                                        on_press=self.on_press))
        self.map.center_on(self.lat, self.lon)

    def on_location(self, **kwargs):
        self.lat = kwargs['lat']
        self.lon = kwargs['lon']

    def on_press(self, *args):
        self.remove_widget(self.info)
        self.info.clear_widgets()
        lb1 = Label(text="Voce esta aqui", pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.info.add_widget(lb1)
        self.add_widget(self.info)

    def on_release(self, *args):
        self.remove_widget(self.info)


class tela3(BoxLayout):
    lat = NumericProperty(0)
    lon = NumericProperty(0)
    info = FloatLayout()
    layer = MarkerMapLayer()
    map = MapView()
    layer = MarkerMapLayer()


    def __init__(self, **kwargs):
        super(tela3, self).__init__(**kwargs)
        self.orientation = "vertical"
        gps.configure(on_location=self.on_location)
        gps.start()
        self.map = MapView(zoom=90, lat=self.lat, lon=self.lon)
        MapMarker(lon=self.lon, lat=self.lat, source="bus.png", on_release=self.on_release1)
        self.add_widget(self.map)
        self.map.add_widget(self.layer)
        self.bind(lon=partial(self.tracking))
        time.sleep(1)

    def tracking(self, *args):
        threading.Timer(5.0, self.tracking).start()
        self.layer.clear_widgets()
        self.layer.add_widget(MapMarker(lon=self.lon, lat=self.lat, source="bus.png", on_release=self.on_release1))
        self.map.center_on(self.lat, self.lon)

    def on_location(self, **kwargs):
        self.lat = kwargs['lat']
        self.lon = kwargs['lon']

    def on_release(self, *args):
        self.remove_widget(self.info)

    def on_release1(self, *args):
        self.remove_widget(self.info)
        self.info.clear_widgets()
        lb1 = Label(text="Onibus linha: ", pos_hint={"center_x": 0.38, "center_y": 0.4})
        lb2 = Label(text="Numero de passageiros:", pos_hint={"center_x": 0.27, "center_y": 0.5})
        lb3 = Label(text="Opcao cadeirante:", pos_hint={"center_x": 0.33, "center_y": 0.6})
        lb4 = Label(text="Transito:", pos_hint={"center_x": 0.41, "center_y": 0.7})
        e1 = TextInput(size_hint=(0.2, 0.05), pos_hint={"center_x": 0.6, "center_y": 0.4})
        e2 = TextInput(size_hint=(0.2, 0.05), pos_hint={"center_x": 0.6, "center_y": 0.5})
        e3 = TextInput(size_hint=(0.2, 0.05), pos_hint={"center_x": 0.6, "center_y": 0.6})
        e4 = TextInput(size_hint=(0.2, 0.05), pos_hint={"center_x": 0.6, "center_y": 0.7})
        bt1 = Button(text="Confirmar", size_hint=(0.2, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.2},
                     on_release=self.on_release)

        self.info.add_widget(lb1)
        self.info.add_widget(lb2)
        self.info.add_widget(lb3)
        self.info.add_widget(lb4)
        self.info.add_widget(e1)
        self.info.add_widget(e2)
        self.info.add_widget(e3)
        self.info.add_widget(e4)
        self.info.add_widget(bt1)
        self.add_widget(self.info, "TOP")


class bus(App):
    def build(self):
        return tela1()


janela = bus()
janela.run()

