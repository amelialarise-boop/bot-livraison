import os
import telebot

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

   MENU DU MORBI'SHOP56  

LA CARTE TOP MOUSE:
10G 40€ / 25G 90€ / 50G 130€
                100G 250€ 

 LA CARTE STATIC / FILTRER:

5G 40€ / 10G 70€ / 25G 150€
       50G 260€ / 100G 480€

         LA CARTE CALI US 🇺🇸
(BLACK SKULL SEEDS ZKITTLEZ)

                   6.7G 80€
     
       LA CARTE WEED HOLLANDAISE 

5G 50€ / 10G 80€ / 20G 150€
50G 320€ 

LA CARTE ZIP COLOMBIENNE 96% 🇨🇴

1G 70€ / 3G 190€ 
5G 300€ / 10G 550€ 

LA CARTE ZIP MEXICAINE 87% 🇲🇽

1G 50€ / 3G 150€ / 5G 250€ 
10G 450€ 

          LA CARTE KÉTAMINE 🦄

2.5G 40€ / 5G 80€ / 10G 150€

💵 Paiement à la livraison uniquement.

Pour commander, écrivez simplement ce que vous voulez.
Exemple :
- 1G à 70€ + 2G à 50€ 
- 10G mousse 40€

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, MENU, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    texte = message.text.lower()

    if "MOUSSE OR FILTRER" in texte or "COCAÏNE" in texte or "WEED" in texte or "KÉTAMINE" in texte:
        bot.reply_to(message, "✅ Commande reçue !\nUn livreur va vous contacter.\nMerci 🙏")
        
        # ⚠️ REMPLACE PAR TON ID TELEGRAM
        ID_LIVREUR = @secretariatmorbiblanche56
        
        bot.send_message(
            ID_LIVREUR,
            f"📦 Nouvelle commande :\n\nClient: @{message.from_user.username}\nCommande: {message.text}"
        )
    else:
        bot.reply_to(message, MENU, parse_mode="Markdown")

print("Bot started...")
bot.infinity_polling()
