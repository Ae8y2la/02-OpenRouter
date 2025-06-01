import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class ChatBot:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "My AI Bot"
            }
        )
        self.model = "deepseek/deepseek-chat-v3-0324:free"

    async def chat(self, message: str):
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

async def main():
    bot = ChatBot()
    print("🤖 AI Bot Ready! Type 'exit' to quit")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        response = await bot.chat(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    asyncio.run(main())