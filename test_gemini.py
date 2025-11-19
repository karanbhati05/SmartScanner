"""
Diagnostic script to test Gemini API integration
Run this to verify your GEMINI_API_KEY is working correctly
"""

import requests
import json
import os

def test_gemini_api():
    """Test the Gemini API with a simple request"""
    
    # IMPORTANT: Replace this with your actual API key from Vercel environment
    api_key = input("Enter your GEMINI_API_KEY: ").strip()
    
    if not api_key:
        print("❌ No API key provided!")
        return False
    
    print(f"✓ Using API key: {api_key[:10]}...")
    
    # Test endpoint
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # Simple test prompt
    payload = {
        "contents": [{
            "parts": [{
                "text": "Say 'Hello, API is working!' in JSON format like: {\"message\": \"Hello, API is working!\"}"
            }]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 100
        }
    }
    
    print("\n🔄 Testing Gemini API connection...")
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        
        print(f"\n📊 Response Status: {response.status_code}")
        print(f"📋 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n✅ SUCCESS! API is working correctly!")
            print(f"📄 Full Response:\n{json.dumps(result, indent=2)}")
            
            if 'candidates' in result:
                generated = result['candidates'][0]['content']['parts'][0]['text']
                print(f"\n💬 Generated Text: {generated}")
                return True
        else:
            print(f"\n❌ FAILED! Status Code: {response.status_code}")
            print(f"📄 Error Response:\n{response.text}")
            
            # Common error diagnostics
            if response.status_code == 400:
                print("\n🔍 Diagnosis: Bad Request - Check API endpoint or payload format")
            elif response.status_code == 403:
                print("\n🔍 Diagnosis: API key may be invalid or API not enabled")
                print("   → Go to https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com")
                print("   → Make sure 'Generative Language API' is ENABLED")
            elif response.status_code == 404:
                print("\n🔍 Diagnosis: Endpoint not found - Model name may be incorrect")
                print("   → Current model: gemini-1.5-flash")
                print("   → Try: gemini-pro or gemini-1.5-pro")
            elif response.status_code == 429:
                print("\n🔍 Diagnosis: Rate limit exceeded - Wait a moment and try again")
            
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out - API may be slow or unreachable")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - Check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_invoice_extraction():
    """Test invoice extraction with Gemini AI"""
    
    api_key = input("\nEnter your GEMINI_API_KEY for invoice test: ").strip()
    
    if not api_key:
        print("❌ No API key provided!")
        return False
    
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # Sample invoice text
    sample_invoice = """
    ACME Corporation
    123 Business St, Suite 100
    New York, NY 10001
    
    INVOICE
    
    Invoice Number: INV-2024-001
    Date: January 15, 2024
    
    Bill To:
    John Smith
    456 Customer Ave
    Boston, MA 02101
    
    Description                  Qty    Price      Amount
    Web Development Services      40    $150.00    $6,000.00
    Design Consultation          10    $200.00    $2,000.00
    
    Subtotal:                                      $8,000.00
    Tax (8.5%):                                      $680.00
    Total:                                         $8,680.00
    
    Payment due within 30 days
    """
    
    prompt = f"""You are an expert invoice data extraction system. Extract the following information from this invoice text:

1. Vendor/Company Name (the business issuing the invoice)
2. Invoice Date (in original format)
3. Total Amount (with currency symbol)
4. Invoice Number (if present)
5. Tax Amount (if present, with currency symbol)
6. Subtotal (amount before tax, with currency symbol)

Invoice Text:
{sample_invoice}

Respond ONLY with a valid JSON object in this exact format:
{{
  "vendor": "Company Name",
  "date": "MM/DD/YYYY",
  "total": "$XXX.XX",
  "invoice_number": "INV-12345",
  "tax": "$XX.XX",
  "subtotal": "$XXX.XX"
}}

If you cannot find a field, use null. Keep currency symbols with amounts."""

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
    
    print("\n🔄 Testing invoice extraction...")
    
    try:
        response = requests.post(url, json=payload, timeout=15)
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n✅ Invoice extraction successful!")
            
            if 'candidates' in result:
                generated = result['candidates'][0]['content']['parts'][0]['text']
                print(f"\n📄 AI Response:\n{generated}")
                
                # Try to parse JSON
                try:
                    cleaned = generated.replace('```json', '').replace('```', '').strip()
                    data = json.loads(cleaned)
                    print(f"\n✅ Parsed JSON successfully:")
                    print(f"   Vendor: {data.get('vendor')}")
                    print(f"   Date: {data.get('date')}")
                    print(f"   Total: {data.get('total')}")
                    print(f"   Invoice #: {data.get('invoice_number')}")
                    print(f"   Tax: {data.get('tax')}")
                    print(f"   Subtotal: {data.get('subtotal')}")
                    return True
                except json.JSONDecodeError as e:
                    print(f"⚠️ JSON parsing failed: {e}")
                    return False
        else:
            print(f"\n❌ Failed! Status: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {type(e).__name__}: {str(e)}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("GEMINI API DIAGNOSTIC TOOL")
    print("=" * 60)
    
    print("\n📝 This tool will help diagnose Gemini API issues")
    print("   You'll need your GEMINI_API_KEY from Vercel environment")
    print("   (Settings → Environment Variables → GEMINI_API_KEY)")
    
    print("\n" + "=" * 60)
    print("TEST 1: Basic API Connection")
    print("=" * 60)
    
    test1_passed = test_gemini_api()
    
    if test1_passed:
        print("\n" + "=" * 60)
        print("TEST 2: Invoice Extraction")
        print("=" * 60)
        
        test2_passed = test_invoice_extraction()
        
        if test2_passed:
            print("\n" + "=" * 60)
            print("✅ ALL TESTS PASSED!")
            print("=" * 60)
            print("\nYour Gemini API key is working correctly.")
            print("The issue may be with Vercel environment configuration.")
            print("\nNext steps:")
            print("1. Verify GEMINI_API_KEY is set in Vercel → Settings → Environment Variables")
            print("2. Make sure it's enabled for 'Production' environment")
            print("3. Redeploy your application after adding the key")
            print("4. Check Vercel Function logs for error messages")
        else:
            print("\n❌ Invoice extraction test failed")
    else:
        print("\n❌ Basic connection test failed")
        print("\nPlease fix the API key or API enablement issue first.")
    
    print("\n" + "=" * 60)
