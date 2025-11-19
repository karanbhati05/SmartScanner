"""
Quick test of the updated Gemini model with invoice extraction
"""

import requests
import json

# Your API key
api_key = "AIzaSyBQBUTdMpy1l1aNhqnksDuGd8gs_Blxv7M"

# Sample invoice text
sample_text = """
ACME Corporation
123 Business St
Invoice #12345
Date: 01/15/2024
Total: $453.00
"""

# Gemini API endpoint with gemini-2.5-flash
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}"

prompt = f"""You are an expert invoice data extraction system. Extract the following information from this invoice text:

1. Vendor/Company Name
2. Invoice Date
3. Total Amount (with currency symbol)
4. Invoice Number

Invoice Text:
{sample_text}

Respond ONLY with a valid JSON object in this exact format:
{{
  "vendor": "Company Name",
  "date": "MM/DD/YYYY",
  "total": "$XXX.XX",
  "invoice_number": "INV-12345"
}}

If you cannot find a field, use null."""

payload = {
    "contents": [{
        "parts": [{
            "text": prompt
        }]
    }],
    "generationConfig": {
        "temperature": 0.1,
        "maxOutputTokens": 800
    }
}

print("Testing gemini-2.5-flash model...")
print(f"API Key: {api_key[:10]}...")
print(f"\nURL: {url[:80]}...")

response = requests.post(url, json=payload, timeout=15)

print(f"\nStatus Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    print(f"\n✅ SUCCESS!")
    
    if 'candidates' in result:
        generated = result['candidates'][0]['content']['parts'][0]['text']
        print(f"\nGenerated Text:\n{generated}")
        
        # Parse JSON
        try:
            cleaned = generated.replace('```json', '').replace('```', '').strip()
            data = json.loads(cleaned)
            print(f"\n✅ Parsed Data:")
            for key, value in data.items():
                print(f"  {key}: {value}")
        except json.JSONDecodeError as e:
            print(f"\n⚠️ JSON parsing failed: {e}")
else:
    print(f"\n❌ FAILED!")
    print(f"Response: {response.text}")
