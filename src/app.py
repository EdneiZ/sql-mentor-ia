import json

with open("../data/conhecimento.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)

print("=" * 50)
print("🤖 SQL Mentor IA - Assistente para Iniciantes")
print("Digite sua dúvida sobre SQL.")
print("Digite 'sair' para encerrar.")
print("=" * 50)
contador = 0

while True:

    pergunta = input("\nDigite sua dúvida SQL (ou sair): ").lower()

    if pergunta != "sair":
        contador += 1

    if pergunta == "sair":
        print(f"\nVocê realizou {contador} consultas.")
        print("Até a próxima!")
        break

    encontrou = False

    for item in base:
        if item["pergunta"] in pergunta:
            print("\nResposta:")
            print(item["resposta"])
            encontrou = True
            break

    if not encontrou:
        print("\nNão encontrei essa informação na base de conhecimento.")