##Import
from tkinter import *
import winsound

##Functions
def SilverChariot(color,num):
    print(color + ' : ' + str(num))
    for i in range(1,octave):
        if color == 'Touche Blanche' :
#(Numéro de la touche en octave 2 * Numéro d'Octave) - ((Numéro d'Octave*Distance de la touche à Do Octave2)-Distance de la touche à Do Octave2)
            if num == 0 :
                print('Do')
                winsound.Beep(int(Do),300)
                Utilisateur.append('Do')     
                print(Utilisateur)
                break      
            elif num - 7 == 0 or num - 7 == 7*i:
                print('Do')
                winsound.Beep(int(Do*(2*num/7)),300) #num/7 = Octave car par exemple 14/7 = 2 donc Octave 2
                Utilisateur.append('Do')     
                print(Utilisateur)
                break
            elif num == 1:
                print('Ré')
                winsound.Beep(int(Ré),300)           
                Utilisateur.append('Ré')     
                print(Utilisateur)
                break
            elif num - 7 == 1 or num - 7 == (8*i)-(i-1):
                print('Ré')
                winsound.Beep(int(Ré*(2*num/8)),300)    
                Utilisateur.append('Ré')     
                print(Utilisateur)
                break        
            elif num == 2:
                print('Mi')
                winsound.Beep(int(Mi),300)
                break        
            elif num - 7 == 2 or num == (9*i)-((i*2)-2):
                print('Mi')
                winsound.Beep(int(Mi*(2*num/9)),300)   
                break         
            elif num == 3:
                print('Fa')
                winsound.Beep(int(Fa),300)   
                break         
            elif num - 7 == 3 or num == (10*i)-((i*3)-3):
                print('Fa')
                winsound.Beep(int(Fa*(2*num/10)),300)  
                break          
            elif num == 4:
                print('Sol')
                winsound.Beep(int(Sol),300)   
                break         
            elif num - 7 == 4 or num == (11*i)-((i*4)-4):
                print('Sol')
                winsound.Beep(int(Sol*(2*num/11)),300)    
                break        
            elif num == 5:
                print('La')
                winsound.Beep(int(La),300)
                break
            elif num - 7 == 5 or num == (12*i)-((i*5)-5):
                print('La')
                winsound.Beep(int(La*(2*num/12)),300)
                break            
            elif num == 6:
                print('Si')
                winsound.Beep(int(Si),300)    
                break        
            elif num - 7 == 6 or num == (13*i)-((i*6)-6):
                print('Si')
                winsound.Beep(int(Si*(2*num/13)),300)
                break          
        if color == 'Touche Noire' :
            if num == 0 :
                print('Do#')
                winsound.Beep(int(DoD),300)      
                break      
            elif num - 7 == 0 or num - 7 == 7*i:
                print('Do#')
                winsound.Beep(int(DoD*(2*num/7)),300)
                break
            elif num == 1:
                print('Ré#')
                winsound.Beep(int(RéD),300)           
                break
            elif num - 7 == 1 or num - 7 == (8*i)-(i-1):
                print('Ré#')
                winsound.Beep(int(RéD*(2*num/8)),300)    
                break              
            elif num == 3:
                print('Fa#')
                winsound.Beep(int(FaD),300)   
                break         
            elif num - 7 == 3 or num == (10*i)-((i*3)-3):
                print('Fa#')
                winsound.Beep(int(FaD*(2*num/10)),300)  
                break          
            elif num == 4:
                print('Sol#')
                winsound.Beep(int(SolD),300)   
                break         
            elif num - 7 == 4 or num == (11*i)-((i*4)-4):
                print('Sol#')
                winsound.Beep(int(SolD*(2*num/11)),300)    
                break        
            elif num == 5:
                print('La#')
                winsound.Beep(int(LaD),300)
                break
            elif num - 7 == 5 or num == (12*i)-((i*5)-5):
                print('La#')
                winsound.Beep(int(LaD*(2*num/12)),300)
                break
    for k in range(0,len(Utilisateur)):
        if Utilisateur[k] == 'Ré' and Utilisateur[k-1] == 'Do' and Utilisateur[k-2] == 'Do' :
            print('Bien ouej')
                

def HierophantGreen(octave,touche_blanche):
    ModeLabel.pack_forget()
    Nombre_Octave.pack_forget()
    EnterLabel.pack_forget()
    fen1.unbind("<KeyPress-space>")
    octave = int(star.get())
    touche_noire = [1, 1, 0, 1, 1, 1, 0] * octave
    fen1.geometry('{}x200'.format(300 * octave))
    #Touche Blanche
    for i in range(0,(touche_blanche*octave)):
        Blanc = Button(fen1, bg='white', activebackground='gray85', command=lambda i=i: SilverChariot('Touche Blanche', i)).grid(row=0, column=i*3, rowspan=2, columnspan=3, sticky='nsew') #Utilisez sticky='nesw' pour l’étirer dans les deux directions afin de remplir la cellule
    #Touche Noire
    for i in range((touche_blanche*octave)-1):
        if touche_noire[i]: #if touche_noire[i] == 1
            Noir = Button(fen1, bg='gray10', activebackground='gray25', command=lambda i=i: SilverChariot('Touche Noire', i)).grid(row=0, column=(i*3)+2, rowspan=1, columnspan=2, sticky='nsew')
    #Configuration Hauteur
    for i in range((touche_blanche*octave)*3):
        fen1.columnconfigure(i, weight=1)
    #Configuration Largeur
    for i in range(2):
        fen1.rowconfigure(i, weight=1)

def Mode():
    if int(star.get()) == 1 :
        mode.set(str(int(star.get())) +" Octave")
    else :
        mode.set(str(int(star.get())) +" Octaves")

def StarPlatinium(octave,touche_blanche):
    ModeLabel.pack()
    Nombre_Octave.pack()
    EnterLabel.pack()
    fen1.bind("<KeyPress-space>  ",lambda event: HierophantGreen(octave,touche_blanche))
    
##Note
Do = 65.4064
Ré = 73.4162
Mi = 82.4069
Fa = 87.3071 
Sol = 97.9989
La = 110
Si = 123.471

DoD = 69.2957
RéD = 77.7817
FaD = 92.4986 
SolD = 103.826
LaD = 116.541
##Core
fen1 = Tk()
octave = 100
Utilisateur = []
touche_blanche = 7
touche_noire = [1, 1, 0, 1, 1, 1, 0] * octave
star = StringVar()
fen1.title('Stardust Instrument')
fen1.geometry('475x105')
#fen1.attributes("-fullscreen", True)
star.set(1)
mode = StringVar()
Nombre_Octave = Spinbox(fen1, from_=1, to=75, increment=1, textvariable = star,font= 'Times',command = Mode)
mode.set(str(int(star.get()))+" Octave")
ModeLabel = Label(fen1,textvariable=mode, font= 'Times')
EnterLabel = Label(fen1, font="Times",text="Appuyez sur la touche 'Espace' pour continuer")
StarPlatinium(octave,touche_blanche)
#HierophantGreen(octave,touche_blanche)
fen1.mainloop()
