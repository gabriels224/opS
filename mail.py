#1111111111111111111111111111111
import flet as ft

def main(pagina):
    texto = ft.Text("Chat")
#111111111111111111111111111

#6666666666666666666666666666666666
    chat = ft.Column()
#666666666666666666666666666666666666

#444444444444444444444444
    nome_usuario = ft.TextField(label="Escreva seu nome")
#44444444444444444444444444444


#777777777777777777777777777777777777777

    def enviar_mensagem_tunel(mensagem):

#777777777777777777777777777777777777777

#1010101010101010101010101010101010
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
#1010101010101010101010101010101010

#9999999999999999999999999999999999999999999        
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
#9999999999999999999999999999999999999999999    

                        #f"{usuario_mensagem}: {texto_mensagens}")) = #999
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))

#1010101010101010101010101010101010
        else:
             usuario_mensagem = mensagem["usuario"]
             chat.controls.append(ft.Text(f"{usuario_mensagem}: entrou no chat", size=20, italic=True, color=ft.colors.GREEN_800))

#1010101010101010101010101010101010

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
         #^^ - ISSO ESTA NO #5 NO ON=CLICK
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})

                           #({"texto": campo_mensagem.value, "usuario": nome_usuario.value}) = #999

        campo_mensagem.value = ""
    
        pagina.update()

#88888888888888888888888888888888888888888


#55555555555555555555555555555555
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

#55555555555555555555555555555555

    def entrar_popup(evento):
       
#1010101010101010101010101010101010
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
#1010101010101010101010101010101010


#6666666666666666666666666666666666
        pagina.add(chat)
#666666666666666666666666666666666

#55555555555555555555555555555555555555
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))

        pagina.update()
#555555555555555555555555555555555



#33333333333333333333333333
    popup = ft.AlertDialog(
#33333333333333333333333333

#444444444444444444444444444444444        
        open=False,
        modal=True,
        title=ft.Text("Bem vindo"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup )],
        
#44444444444444444444444444444444444444
    )
#3333333333333333333333333333333333
    def entra_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
#333333333333333333333333333333333

#2222222222222222222222
    botao_iniciar = ft.ElevatedButton("Iniciar", on_click=entra_chat)
#222222222222222222222222222

#1111111111111111111111
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=2130)
#view=web
#1111111111111111111111111111
















