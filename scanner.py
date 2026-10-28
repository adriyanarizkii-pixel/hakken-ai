import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}"

def main():
    offset = None
    print("Hakken aktif!")

    while True:
        try:
            response = requests.get(
                f"{API}/getUpdates",
                params={"offset": offset, "timeout": 30},
                timeout=35
            )
            data = response.json()

            for update in data.get("result", []):
                offset = update["update_id"] + 1
                message = update.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                text = message.get("text", "")

                if chat_id and text == "/start":
                    requests.post(
                        f"{API}/sendMessage",
                        json={
                            "chat_id": chat_id,
                            "text": "text": (
    "Hakken AI aktif! 🤖\n\n"
    "Asisten Swing Trading Saham Indonesia\n\n"
    "Gunakan perintah:\n"
    "/saham BBCA\n"
    "/saham BBRI\n"
    "/saham ANTM\n\n"
    "Fitur analisis teknikal sedang dikembangkan."
                    )
                        },
                        timeout=15
                    )
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
