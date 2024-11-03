import google.generativeai as genai
from ..config import settings
from typing import Optional, Dict

class GeminiAI:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.history: Dict[str, list] = {}  # Kullanıcı bazlı sohbet geçmişi

    async def get_response(self, message: str, user_id: Optional[str] = None) -> str:
        try:
            # Eğer kullanıcı kimliği varsa, geçmiş kontrolü yap
            context = ""
            if user_id and user_id in self.history:
                context = "\n".join(self.history[user_id][-5:])  # Son 5 mesaj
                
            # Mesajı hazırla
            prompt = f"{context}\nUser: {message}" if context else message
            
            # Yanıt al
            response = await self.model.generate_content(prompt)
            
            # Geçmişi güncelle
            if user_id:
                if user_id not in self.history:
                    self.history[user_id] = []
                self.history[user_id].append(f"User: {message}")
                self.history[user_id].append(f"Assistant: {response.text}")
            
            return response.text
            
        except Exception as e:
            print(f"Error in get_response: {str(e)}")
            return f"Üzgünüm, bir hata oluştu: {str(e)}"