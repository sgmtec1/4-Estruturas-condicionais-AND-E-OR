# Estruturas condicionais AND E OR
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')

var1 = input(lcd.escrever(board, 0, 0, 'DIGITE 1 NUMERO '))
var2 = input(lcd.escrever(board, 0, 0, 'DIGITE 2 NUMERO '))
var3 = input(lcd.escrever(board, 0, 0, 'DIGITE 3 NUMERO '))

if var2> var1:
    lcd.escrever(board, 0, 0, 'O 2 NUM E        ')
    lcd.escrever(board, 0, 1, 'MAIOR Q O 1      ')
elif var2 == 500:
    lcd.escrever(board, 0, 0, 'O 2 NUM VALE 500       ')
    lcd.escrever(board, 0, 1, '                       ')
elif var3 == var2:
    lcd.escrever(board, 0, 0, 'O 3 NUM TEM O MESMO')
    lcd.escrever(board, 0, 1, 'VALOR DO 2 NUM  ')
elif var4 is str ('4'):
    lcd.escrever(board, 0, 0, 'O 4 NUM E       ')
    lcd.escrever(board, 0, 1, 'DO TIPO STRING     ')
else:
    lcd.escrever(board, 0, 0, 'NENHUMA CONDICAO   ')
    lcd.escrever(board, 0, 1, 'E VERDADEIRA       ')
time.sleep(100.0)
lcd.limpar(board)
board.exit()