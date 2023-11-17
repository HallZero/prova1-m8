import re
from random import randint

def payment():
    frases = ['Digita o número do cartão e os 3 digitos engraçados atrás!', 'Finalmente vai me pagar, caloteiro?', 'Compra pra mim também?', 'Tô nem ai KKKKKK']
    print(frases[randint(0, len(frases)-1)])

def status():
    frases = ['Sei lá, cara... Uma hora chega.', 'Desculpa a ansiedade, mas... O que você pediu?', 'Pergunta no Posto Ipiranga']
    print(frases[randint(0, len(frases)-1)])
    

intentions = {
    r"(?:([Cc]art[ãa]o ([Dd]e) (([Cc]r[[ée]dito)|([Dd][ée]bito)))|(?:([Pp]agamento)|([Mm]udar)|([Aa]tualiza)(r|[çc][ãa]o|do)))": "payment",
    r"(?:([Ss]tatus)|([Rr]astrear)|([Oo]nde)|([Pp]edido)|([Ee]ntrega)|([Aa]companhar))": "status",
    # Exit
}

actions = {
    "payment": payment,
    "status": status,
    "sair": exit,
}

def main():
    
    while 1:
        text = input("Chora:")
    
        if text == 'sair':
            print("Exiting...")
            return 0
        
        for expression, action in intentions.items():
            pattern = re.compile(expression)
            groups = pattern.findall(text)

            if groups:
                actions[action]()

if __name__ == "__main__":
    main()