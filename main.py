from telegram.ext import*
import random

API_Key = '5336566887:AAFqct-JzctC2mpUjl14sU8FI5iIi-E3GMw'


def handle_message(update, context):

    text = update.message.text

    response = create_responses(text)
    update.message.reply_text(response)


def create_responses(input_text):

    #responses_list = ["Ja okay", "Jo", "Fick dich!", "Ich sags ihm", "Ich werds ihm ausrichtne", "Geh mir nicht auf die Nüsse, eh", "Notiert. Und jetzt fapiss dich.", "ja, sag ich ihm", "Gut...", "Wenns sein muss...", "Nö", "Ja. Nö.", "Sags ihm doch selber", "Keine Lust", "Vielleicht. Vielleicht auch nicht", "Hahahaaha, als ob", "Ist der Pabst pädophil?", "Wenn du mich oral befriedigst, mach ich es."]

    if input_text == "Hey" or input_text == "hey" or input_text == "Hi" or input_text == "Hallo" or input_text == "hallo":
        return "Jo, was willst du Hund?"

    elif input_text == "Danke" or input_text == "danke":
        return "Fick dich und lass mich endlich in Ruhe..."

    elif "bist" and " ein " in input_text:
        return "Du bist selber ein " + input_text.split(" ")[-1] + "!"

    elif "bist" in input_text:
        return "Du bist selber " + input_text.split(" ")[-1] + "!"

    elif "?" in input_text:
        return "Was willst du? Paar aufs Maul?"

    elif "nein" in input_text:
        return "Ähhh, doch?!"

    elif "Nein" in input_text:
        return "Ähhh, doch?!"

    elif "beleidigen" in input_text:
        return "Heul doch, du Pussy"

    else:
        return "selber " + input_text + "!"




def main():
    updater = Updater(API_Key)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(0)


if __name__ == "__main__":
    main()
