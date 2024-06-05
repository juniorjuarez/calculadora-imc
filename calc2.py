import flet as ft

dinnergray = "#696969"
Gainsboro = "#DCDCDC"
LightGrey = "#D3D3D3"
grey31 = "#4F4F4F"
grey11 = "#1C1C1C"

## VERDE
SpringGreen = "#e5f8e5"

## amarelo
Khaki = "#F0E68C"
OrangeRed = "#FF4500"


def main(page: ft.Page):
    page.title = "Calculadora IMC"
    page.window_height = 550
    page.window_width = 350
    page.bgcolor = dinnergray

    def erro_close(e):
        page.banner.open = False
        page.update()

    espaco = ft.Container(height=30)

    page.banner = ft.Banner(
        bgcolor=grey11,
        leading=ft.Icon(ft.icons.WARNING_AMBER_OUTLINED, color=Gainsboro),
        content=ft.Text("Ops, preencha todos os campos!", size=12, color=Gainsboro),
        actions=[
            ft.TextButton("Ok", on_click=erro_close),
        ],
    )

    def limpar_dados(e):
        if "contresult" in globals():
            page.remove(contresult)
            page.update()

    def calcular(e):
        
        global contresult
        

        if peso.value == "" or altura.value == "" or biotipo.value == "":
            page.banner.open = True
            page.update()
        else:
            try:
                if "contresult" in globals():
                    page.remove(contresult)
                    page.update()
               
                if not peso.value.replace('.', '').replace('-', '').isdigit() or not altura.value.replace('.', '').replace('-', '').isdigit():
                    raise ValueError("Os valores de peso e altura devem ser numéricos")
             
                valor_peso = float(peso.value)
                valor_altura = float(altura.value)
                valor_biotipo = biotipo.value

                imc = valor_peso / (valor_altura * valor_altura)

                imc = float(f"{imc:.2f}")
                if valor_biotipo == "Feminino":

                    ## abaixo do peso
                    if imc < 18.5:

                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.WARNING, color=OrangeRed),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nRsultado: {imc}\nVocê está abaixo do peso!",
                                        color=grey11,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor=grey11,
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=Khaki,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)

                    ### peso ok
                    elif imc >= 18.5 and imc < 24.9:
                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.CHECK, color=grey31),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nResultado: {imc}\nVocê está com peso normal.",
                                        color=grey31,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor=grey11,
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=SpringGreen,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)

                    ## Sobrepeso
                    elif imc > 24.9 and imc <= 30:
                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.WARNING, color=OrangeRed),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nResultado: {imc}\nAtenção, você está com sobrepeso!",
                                        color=OrangeRed,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor=grey11,
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=Khaki,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)

                        ## Obeso
                    elif imc > 30:
                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.WARNING, color="yellow"),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nResultado: {imc}\nAtenção, você está com obesidade!",
                                        color=Gainsboro,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor="red",
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=OrangeRed,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)
                ### Masculino
                elif valor_biotipo == "Masculino":
                    ## abaixo do peso
                    if imc < 20:

                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.WARNING, color=OrangeRed),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nRsultado: {imc}\nVocê está abaixo do peso!",
                                        color=grey11,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor=grey11,
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=Khaki,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)

                    ### peso ok
                    elif imc >= 20 and imc < 24.9:
                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.CHECK, color=grey31),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nResultado: {imc}\nVocê está com peso normal.",
                                        color=grey31,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor=grey11,
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=SpringGreen,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)

                    ## Sobrepeso
                    elif imc > 24.9 and imc <= 30:
                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.WARNING, color=OrangeRed),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nResultado: {imc}\nAtenção, você está com sobrepeso!",
                                        color=OrangeRed,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor=grey11,
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=Khaki,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)

                        ## Obeso
                    elif imc > 30:
                        contresult = ft.Container(
                            ft.Row(
                                [
                                    ft.Icon(ft.icons.WARNING, color="yellow"),
                                    ft.Text(
                                        f"\nBiotipo: {valor_biotipo}, Peso: {valor_peso}, Altura: {valor_altura}\nResultado: {imc}\nAtenção, você está com obesidade!",
                                        color=Gainsboro,
                                        size=10,
                                        weight="bold",
                                    ),
                                    ft.ElevatedButton(
                                        "Ok",
                                        on_click=limpar_dados,
                                        color=LightGrey,
                                        bgcolor=grey11,
                                    ),
                                ]
                            ),
                            alignment=ft.alignment.center,
                            bgcolor=OrangeRed,
                            padding=5,
                            border_radius=10,
                        )
                        page.add(contresult)

                peso.value = ""
                altura.value = ""
                biotipo.value = ""
                page.update()
            except Exception as ex:
                print(f"Erro inesperado: {ex}")
                page.banner.content = ft.Text(f"Erro: {ex}", size=12, color=Gainsboro)
                page.banner.open = True
                peso.value = ""
                altura.value = ""
                biotipo.value = ""
                valor_altura = ""
                valor_biotipo = ""
                valor_altura = ""
                page.update()

    ## Cabeçalho
    cabecalho = ft.Container(
        ft.Row(
            [
                ft.Icon(ft.icons.MULTILINE_CHART, color=Gainsboro),
                ft.Text("Calculadora de IMC", color=Gainsboro, size=25),
            ]
        ),
        alignment=ft.alignment.center,
        bgcolor=grey11,
        padding=10,
        border_radius=5,
    )

    dados_user = ft.Text(value="Informe seus dados", color=Gainsboro, size=15)

    altura = ft.TextField(
        label="Informe a altura, ex: 1.75",
        color=Gainsboro,
        bgcolor=dinnergray,
        border_color=Gainsboro,
    )

    peso = ft.TextField(
        label="Informe seu peso, ex: 80",
        color=Gainsboro,
        bgcolor=dinnergray,
        border_color=Gainsboro,
    )

    biotipo = ft.Dropdown(
        options=[ft.dropdown.Option("Masculino"), ft.dropdown.Option("Feminino")],
        hint_text="Informe seu biotipo",
        color=Gainsboro,
        bgcolor=dinnergray,
        border_color=Gainsboro,
    )

    box2 = ft.Container(
        content=dados_user,
        alignment=ft.alignment.center,
    )

    box3 = ft.Container(
        ft.Column([altura, peso, biotipo]),
        alignment=ft.alignment.center,
    )

    box4 = ft.Container(
        content=ft.ElevatedButton(
            "Calcular IMC", color=LightGrey, bgcolor=grey11, on_click=calcular
        ),
        alignment=ft.alignment.center,
    )
    page.add(espaco, cabecalho, box2, box3, box4)


ft.app(target=main)
