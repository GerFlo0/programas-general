from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import math


class CuerdaApp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # Entradas
        self.add_widget(Label(text="Ancho del neumático (mm):"))
        self.ancho_input = TextInput(multiline=False)
        self.add_widget(self.ancho_input)

        self.add_widget(Label(text="Perfil del neumático (%):"))
        self.relacion_input = TextInput(multiline=False)
        self.add_widget(self.relacion_input)

        self.add_widget(Label(text="Diámetro de la llanta (pulgadas):"))
        self.diametro_input = TextInput(multiline=False)
        self.add_widget(self.diametro_input)

        self.add_widget(Label(text="Ancho de la cuerda (mm):"))
        self.ancho_cuerda_input = TextInput(multiline=False)
        self.add_widget(self.ancho_cuerda_input)

        # Botón
        self.calcular_button = Button(text="Calcular")
        self.calcular_button.bind(on_press=self.calcular)
        self.add_widget(self.calcular_button)

    def calcular(self, instance):
        try:
            # Obtener valores
            ancho = float(self.ancho_input.text)
            relacion = float(self.relacion_input.text)
            diametro_llanta = float(self.diametro_input.text) * 2.54  # Convertir pulgadas a milímetros
            ancho_cuerda = float(self.ancho_cuerda_input.text)
            
            # Funciones auxiliares
            def fun_radio(diametro_llanta, relacion):
                return (5 * diametro_llanta / math.sqrt(100 - relacion)) * 10
            
            def fun_perimetro(r):
                return (2 * r) * math.pi
            
            def fun_metros_perimetro(ancho, perimetro, ancho_cuerda):
                return (math.ceil(ancho / ancho_cuerda) * perimetro)
            
            def fun_metros_cara(radio, ancho_cuerda, suma_perimetros=0.0):
                if radio <= 0:
                    return suma_perimetros
                suma_perimetros += fun_perimetro(radio) / 1000
                return fun_metros_cara(radio - ancho_cuerda, ancho_cuerda, suma_perimetros)
            
            # Cálculos
            radio = fun_radio(diametro_llanta, relacion)
            perimetro = fun_perimetro(radio) / 1000
            metros_cara = fun_metros_cara(radio, ancho_cuerda)
            metros_perimetro = fun_metros_perimetro(ancho, perimetro, ancho_cuerda)
            total_cuerda = metros_cara + metros_perimetro
            
            # Mostrar resultado
            popup = Popup(title="Resultado",
                        content=Label(text=f"Metros de cuerda totales requeridos: {total_cuerda:.2f}"),
                        size_hint=(0.8, 0.4))
            popup.open()
            
        except ValueError:
            popup = Popup(title="Error",
                        content=Label(text="Por favor, ingrese valores numéricos válidos."),
                        size_hint=(0.8, 0.4))
            popup.open()


class CalculadoraApp(App):
    def build(self):
        return CuerdaApp()


if __name__ == "__main__":
    CalculadoraApp().run()
