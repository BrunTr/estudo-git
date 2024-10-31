def main():
    hello = greeting(input("Olá! Como foi sua refeição?"))
    dollars = dollars_to_float(input("Quanto foi a refeição? "))
    percent = percent_to_float(input("Quantos porcento de gorjeta gostaria de deixar? "))
    tip = dollars * percent
    print(f"Deixe R${tip:.2f}")

def greeting(response):
   print("Obrigado por compartilhar! Vamos calcular a gorjeta.")
    
def dollars_to_float(d):
    # TODO
    d = d.replace(",", ".").strip("$")
    return float(d)

def percent_to_float(p):
    p = p.replace(",", ".").strip("$")
    return float(p)/100

main()