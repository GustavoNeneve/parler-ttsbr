import re
import unicodedata
from num2words import num2words

class BrazilianPortugueseTextNormalizer:
    def __init__(self):
        self.number_re = re.compile(r'[0-9]+')
        self.language = "pt-br"
        self.voice_descriptions = {
            "francisca": {
                "pt-br": "Uma voz feminina madura e acolhedora com sotaque brasileiro neutro, falando de forma clara e profissional",
                "en": "A mature and welcoming female voice with neutral Brazilian accent, speaking clearly and professionally"
            }
        }
        
    def normalize(self, text):
        # Converter números para texto
        text = self.number_re.sub(lambda m: num2words(int(m.group()), lang='pt-br'), text)
        
        # Normalizar acentos
        text = unicodedata.normalize('NFKC', text)
        
        # Remover pontuação desnecessária mantendo apenas . , ? ! 
        text = re.sub(r'[^\w\s.,!?]', '', text)
        
        # Processar descrições de voz específicas
        for voice_name, description in self.voice_descriptions.items():
            if voice_name.lower() in text.lower():
                return description.get(self.language)
                
        return text
        
    def set_language(self, lang_code):
        """Define o idioma para geração de voz (pt-br ou en)"""
        if lang_code not in ["pt-br", "en"]:
            raise ValueError("Idioma não suportado. Use 'pt-br' ou 'en'")
        self.language = lang_code
        
    def get_voice_description(self, voice_name):
        """Retorna a descrição padrão para uma voz específica no idioma configurado"""
        voice_info = self.voice_descriptions.get(voice_name.lower())
        if voice_info:
            return voice_info.get(self.language)
        return None
