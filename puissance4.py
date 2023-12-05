
import turtle
import random

'dessin de la grille'
quadrillagex = turtle.Turtle()
quadrillagey = turtle.Turtle()
turtle.screensize(1000,1000)

quadrillagex.speed('fastest')
quadrillagey.speed('fastest')
quadrillagex.up()
quadrillagey.up()
quadrillagey.goto(-300,400)
quadrillagey.pendown()
quadrillagex.goto(-300,-300)
quadrillagex.pendown()

quadrillagex.goto(-300,400)
quadrillagex.goto(-200,400)
quadrillagex.goto(-200,-300)
quadrillagex.goto(-100,-300)
quadrillagex.goto(-100,-300)
quadrillagex.goto(-100,400)
quadrillagex.goto(0,400)
quadrillagex.goto(0,-300)
quadrillagex.goto(100,-300)
quadrillagex.goto(100,400)
quadrillagex.goto(100,400)
quadrillagex.goto(200,400)
quadrillagex.goto(200,-300)
quadrillagex.goto(300,-300)
quadrillagex.goto(300,400)
quadrillagex.goto(400,400)
quadrillagex.goto(400,-300)

quadrillagey.goto(400,400)
quadrillagey.goto(400,300)
quadrillagey.goto(-300,300)
quadrillagey.goto(-300,200)
quadrillagey.goto(400,200)
quadrillagey.goto(400,100)
quadrillagey.goto(-300,100)
quadrillagey.goto(-300,0)
quadrillagey.goto(400,0)
quadrillagey.goto(400,-100)
quadrillagey.goto(-300,-100)
quadrillagey.goto(-300,-200)
quadrillagey.goto(400,-200)
quadrillagey.goto(400,-300)
quadrillagey.goto(-300,-300)

'definition des cases'

case11 = 0
case12 = 0
case13 = 0
case14 = 0
case15 = 0
case16 = 0
case17 = 0
case21 = 0
case22 = 0
case23 = 0
case24 = 0
case25 = 0
case26 = 0
case27 = 0
case31 = 0
case32 = 0
case33 = 0
case34 = 0
case35 = 0
case36 = 0
case37 = 0
case41 = 0
case42 = 0
case43 = 0
case44 = 0
case45 = 0
case46 = 0
case47 = 0
case51 = 0
case52 = 0
case53 = 0
case54 = 0
case55 = 0
case56 = 0
case57 = 0
case61 = 0
case62 = 0
case63 = 0
case64 = 0
case65 = 0
case66 = 0
case67 = 0
case71 = 0
case72 = 0
case73 = 0
case74 = 0
case75 = 0
case76 = 0
case77 = 0

liste1 = [case11, case12, case13, case14, case15, case16, case17]
liste2 = [case21, case22, case23, case24, case25, case26, case27]
liste3 = [case31, case32, case33, case34, case35, case36, case37]
liste4 = [case41, case42, case43, case44, case45, case46, case47]
liste5 = [case51, case52, case53, case54, case55, case56, case57]
liste6 = [case61, case62, case63, case64, case65, case66, case67]
liste7 = [case71, case72, case73, case74, case75, case76, case77]
listex = [liste1, liste2, liste3, liste4, liste5, liste6, liste7]

#pour acceder a un element: listex[la colonne sur laquelle il se situe][la ligne sur laquelle il se situe]

'variables de jeu'

'la fonction pion met le pion ou elle veut et ne se charge pas de le faire descendre, cette mechanique est a ajouter avant'

creel = False

def pionRouge(casex,casey):
  destinx = 0
  destiny = 0
  pionRouge=turtle.Turtle()
  pionRouge.speed('fastest')
  pionRouge.color('red')
  pionRouge.up()

  if casey+1==1:
    destiny=350
  elif casey+1==2:
    destiny=250
  elif casey+1==3:
    destiny=150
  elif casey+1==4:
    destiny=50
  elif casey+1==5:
    destiny=-50
  elif casey+1==6:
    destiny=-150
  elif casey+1==7:
    destiny=-250

  if casex+1==1:
    destinx=-250
  if casex+1==2:
    destinx=-150
  if casex+1==3:
    destinx=-50
  if casex+1==4:
    destinx=50
  if casex+1==5:
    destinx=150
  if casex+1==6:
    destinx=250
  if casex+1==7:
    destinx=350

  listex[casex][casey]=2
  pionRouge.goto(destinx,destiny-50)
  pionRouge.pendown()
  pionRouge.circle(50)
  'le premier argument designe le mouvement horizontal, le deuxieme le mouvement vertical '

def pionBleu(casex,casey):
  destinx = 0
  destiny = 0
  pionBleu=turtle.Turtle()
  pionBleu.speed('fastest')
  pionBleu.color('blue')
  pionBleu.up()

  if casey+1==1:
    destiny=350
  elif casey+1==2:
    destiny=250
  elif casey+1==3:
    destiny=150
  elif casey+1==4:
    destiny=50
  elif casey+1==5:
    destiny=-50
  elif casey+1==6:
    destiny=-150
  elif casey+1==7:
    destiny=-250

  if casex+1==1:
    destinx=-250
  if casex+1==2:
    destinx=-150
  if casex+1==3:
    destinx=-50
  if casex+1==4:
    destinx=50
  if casex+1==5:
    destinx=150
  if casex+1==6:
    destinx=250
  if casex+1==7:
    destinx=350
  listex[casex][casey]=1
  pionBleu.goto(destinx,destiny-50)
  pionBleu.pendown()
  pionBleu.circle(50)
  'le premier argument designe le mouvement horizontal, le deuxieme le mouvement vertical '

def xdanscolonne(colonne):
  i = 6
  while listex[colonne][i]!=0:
    i=i-1
  return(i)

def victoire(grille):
  findelapartie = False
  'verification des lignes'

  for j in range(7):
    if grille[j][3]!=0:
      for i in range(4):
        grille[j][i+2]
        if grille[j][i]==grille[j][i+1]==grille[j][i+2]==grille[j][i+3]:
          findelapartie = True
          if grille[j][i+1]==1:
            print('victoire des bleus')
          else:
            print('victoire des rouges')
          quit()

  'verification des colonnes'

  for k in range(7):
    if grille[3][k]!=0:
      for l in range(4):
        if grille[l][k]==grille[l+1][k]==grille[l+2][k]==grille[l+3][k]:
          findelapartie = True
          if grille[3][k]==1:
            print('victoire des bleus')
          else:
            print('victoire des rouges')
          quit()
  
  'verification des diagonales de haut en gauche a bas a droite'
  for m in range(4):
    for n in range(4):
      if grille[m][n]!=0:
        if grille[m][n]==grille[m+1][n+1]==grille[m+2][n+2]==grille[m+3][n+3]:
          findelapartie = True
          if grille[m][n]==1:
            print('victoire des bleus')
            quit()
          else:
            print('victoire des rouges')
            quit()
  
  for o in range(4):
    for p in range(4):
      q=6-p
      if grille[q][o]!=0:
        if grille[q][o]==grille[q-1][o+1]==grille[q-2][o+2]==grille[q-3][o+3]:
          if grille[q][o]==1:
            print('victoire des bleus')
            quit()
          else:
            print('victoire des rouges')
            quit()

  return(findelapartie)

def jeu():
  tourdejeu = 1
  while victoire(listex)==False:

    jeu = int(input("entrez le numero de la colonne dans laquelle vous souhaitez jouer "))-1

    'le premier joueur est bleu'
    if tourdejeu%2==0:
      pionBleu(jeu, xdanscolonne(jeu))
    else:
      pionRouge(jeu, xdanscolonne(jeu))
    tourdejeu=tourdejeu+1


#def jeuOrdi(grille):
#def min(profondeur, grille):
#def max(profondeur, grille): 
#def eval(joueur, grille):

'l etat vide est 0, l etat bleu est 1, l etat rouge est 2'

'partie execution'

jeu()


