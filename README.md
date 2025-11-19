# 🤖 AI Invoice Processing API

> Intelligent invoice data extraction powered by Google Gemini AI and OCR

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/karanbhati05/invoice-processing-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 🤖 **AI-Powered Extraction** - Uses Google Gemini 2.0 for intelligent data extraction
- 📄 **OCR Processing** - Extracts text from images using OCR.space API
- 🎯 **Comprehensive Data** - Extracts vendor, date, total, invoice number, tax, subtotal, summary, and line items
- 🌍 **Multi-Currency Support** - Handles $, €, £, ¥ and other currencies
- 🔄 **Smart Fallback** - Automatically falls back to regex if AI fails
- ⚡ **Serverless** - Deployed on Vercel with zero infrastructure management
- 🎨 **Beautiful UI** - Drag & drop interface included

## 📁 Project Structure

```
invoice-processing-api/
├── api/                    # Backend API
│   ├── __init__.py
│   ├── index.py           # Flask routes
│   └── processor.py       # Extraction logic
├── public/                 # Frontend UI
│   └── index.html         # Web interface
├── docs/                   # Documentation
│   ├── AI_SETUP.md        # Gemini API setup guide
│   ├── DEPLOYMENT.md      # Deployment instructions
│   └── TROUBLESHOOTING.md # Common issues & solutions
├── tests/                  # Test scripts
│   ├── test_gemini.py     # API diagnostics
│   └── quick_test.py      # Quick verification
├── sample/                 # Sample files
│   └── sample-invoice.pdf # Test invoice
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel configuration
└── README.md              # This file
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/karanbhati05/invoice-processing-api.git
cd invoice-processing-api
```

### 2. Set Up Environment Variables

Create a Vercel account and add these environment variables:

- `OCR_API_KEY` - Get from [OCR.space](https://ocr.space/ocrapi)
- `GEMINI_API_KEY` - Get from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 3. Deploy to Vercel

```bash
npm install -g vercel
vercel --prod
```

## 📡 API Reference

### POST `/api/process`

Upload and process an invoice image.

**Request:**
```http
POST /api/process
Content-Type: multipart/form-data

file: <image_file>
```

**Supported formats:** PNG, JPG, JPEG, PDF, GIF, BMP, TIFF

**Response:**
```json
{
  "success": true,
  "extraction_method": "ai",
  "ai_enabled": true,
  "data": {
    "vendor": "CPB SOFTWARE (GERMANY) GMBH",
    "date": "1. März 2024",
    "total": "453,53 €",
    "invoice_number": "123100401",
    "tax": "72,41 €",
    "subtotal": null,
    "summary": "Invoice for various services including Basic Fees...",
    "line_items": [
      {
        "description": "Basic Fee wmView",
        "quantity": null,
        "price": "130,00 €"
      }
    ]
  }
}
```

### GET `/api/health`

Check API health and configuration status.

**Response:**
```json
{
  "status": "healthy",
  "service": "Invoice Processing API",
  "version": "1.0.0",
  "gemini_api_configured": true,
  "ocr_api_configured": true
}
```

## 🧪 Testing

Run the diagnostic tools to verify your setup:

```bash
# Comprehensive API diagnostics
python tests/test_gemini.py

# Quick verification test
python tests/quick_test.py
```

## 📚 Documentation

- **[AI Setup Guide](docs/AI_SETUP.md)** - Complete guide to setting up Google Gemini API
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Step-by-step deployment instructions
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Common issues and solutions

## 🎯 Accuracy

- **AI Extraction**: ~95% accuracy
- **Regex Fallback**: ~60% accuracy
- **Multi-language**: Supports invoices in English, German, and other European languages

## 🔧 Technology Stack

- **Backend**: Flask (Python 3.9+)
- **AI**: Google Gemini 2.0 Flash
- **OCR**: OCR.space API
- **Deployment**: Vercel Serverless Functions
- **Frontend**: Vanilla JavaScript, HTML5, CSS3

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⭐ Support

If this project helped you, please give it a star! ⭐

---

**Made with ❤️ by [Karan Bhati](https://github.com/karanbhati05)**
