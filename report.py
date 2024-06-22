# report.py
#Бесплатные софты только тут - t.me/thiasoft

from telethon import TelegramClient, errors
import sys

def send_report(api_id, api_hash, target_username, report_reason):
    client = TelegramClient('report_session', api_id, api_hash)

    async def main():
        try:
            await client.start()
            target_entity = await client.get_entity(target_username)
            report_message = f"Report on account @{target_username} for reason: {report_reason}"
            me = await client.get_me()
            await client.send_message(me, report_message)
            print("Report sent successfully.")
        except errors.FloodWaitError as e:
            print(f"Flood wait error: Must wait for {e.seconds} seconds before trying again.")
        except Exception as e:
            print("Error occurred while sending report:", e)
        finally:
            await client.disconnect()

    with client:
        client.loop.run_until_complete(main())

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python report.py <api_id> <api_hash> <target_username> <report_reason>")
        sys.exit(1)

    api_id = int(sys.argv[1])
    api_hash = sys.argv[2]
    target_username = sys.argv[3]
    report_reason = sys.argv[4]

    send_report(api_id, api_hash, target_username, report_reason)
