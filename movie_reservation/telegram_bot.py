import asyncio
import telegram 

TOKEN='7906795471:AAHfbhlk7tLpWJ6-dalU74mbCl6D-E8MxN4'
async def main():
    bot = telegram.Bot(token=TOKEN)
    # 비동기적으로 업데이트 가져오기
    # updates = await bot.getUpdates()
    
    # for update in updates:
    #     print(update)
    #     if update.message:  # 메시지가 있는 경우만 출력
    #         print(update.message.text)
            
    await bot.sendMessage(chat_id=7540647235,text="테스트입니다.")

# asyncio 이벤트 루프 실행
if __name__ == '__main__':
    asyncio.run(main())
