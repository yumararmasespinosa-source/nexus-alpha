import google.generativeai as genai
from config.settings import GEMINI_API_KEY

# Configure the Gemini API with the API key
genai.configure(api_key=GEMINI_API_KEY)

class GeminiMarketAnalysisService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
    
    def analyze_market(self, market_data):
        """Use Gemini API to analyze market data"""
        prompt = f"Analyze this market data and provide insights:\n{market_data}"
        response = self.model.generate_content(prompt)
        return response.text
    
    def generate_report(self, analysis):
        """Generate a detailed report using the analysis"""
        prompt = f"Based on this analysis, generate a comprehensive market report:\n{analysis}"
        response = self.model.generate_content(prompt)
        return response.text

# Example usage
if __name__ == '__main__':
    service = GeminiMarketAnalysisService()
    market_data = "Sample market data for analysis"
    analysis = service.analyze_market(market_data)
    report = service.generate_report(analysis)
    print(report)