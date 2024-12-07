import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require('2.0.0')  # Versão mínima do Kivy necessária


class ConversaoMoedasApp(App):
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Campo para taxa do dólar
        self.layout.add_widget(Label(text="Taxa do Dólar:"))
        self.taxa_dolar_input = TextInput(hint_text="Exemplo: 5.00", multiline=False)
        self.layout.add_widget(self.taxa_dolar_input)

        # Campo para taxa do euro
        self.layout.add_widget(Label(text="Taxa do Euro:"))
        self.taxa_euro_input = TextInput(hint_text="Exemplo: 5.50", multiline=False)
        self.layout.add_widget(self.taxa_euro_input)

        # Campo para valor em reais
        self.layout.add_widget(Label(text="Valor em Reais:"))
        self.valor_reais_input = TextInput(hint_text="Exemplo: 100.00", multiline=False)
        self.layout.add_widget(self.valor_reais_input)

        # Botão para realizar a conversão
        self.converter_button = Button(text="Converter")
        self.converter_button.bind(on_press=self.converter_moedas)
        self.layout.add_widget(self.converter_button)

        # Resultado da conversão
        self.resultado_label = Label(text="Resultados aparecerão aqui")
        self.layout.add_widget(self.resultado_label)

        return self.layout

    def converter_moedas(self, instance):
        try:
            # Obtém as taxas e valores
            taxa_dolar = float(self.taxa_dolar_input.text)
            taxa_euro = float(self.taxa_euro_input.text)
            valor_reais = float(self.valor_reais_input.text)

            # Calcula as conversões
            valor_dolar = valor_reais / taxa_dolar
            valor_euro = valor_reais / taxa_euro

            # Atualiza o resultado na interface
            self.resultado_label.text = (
                f"Valor em Dólar: US$ {valor_dolar:.2f}\n"
                f"Valor em Euro: € {valor_euro:.2f}"
            )
        except ValueError:
            # Caso o usuário insira valores inválidos
            self.resultado_label.text = "Erro: Insira valores numéricos válidos."


if __name__ == "__main__":
    ConversaoMoedasApp().run()
