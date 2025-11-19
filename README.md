# Intelligent Invoice Processing API

A serverless API for extracting key information from invoice images using OCR and intelligent pattern matching.

## Features

- **OCR Processing**: Uses Tesseract OCR to extract text from invoice images
- **Smart Data Extraction**: 
  - Vendor name matching using fuzzy string matching
  - Date extraction supporting multiple formats (MM/DD/YYYY, Month DD YYYY, etc.)
  - Total amount extraction with currency symbol support ($, €, £)
- **REST API**: Simple POST endpoint for file uploads
- **Serverless**: Designed for Vercel deployment

## API Endpoints

### POST `/api/process`
Upload an invoice image for processing.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file upload with key `file`

**Response:**
```json
{
  "success": true,
  "data": {
    "vendor": "Amazon",
    "date": "January 15, 2024",
    "total": "$1,234.56"
  }
}
```

### GET `/api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "Invoice Processing API",
  "version": "1.0.0"
}
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
   - **Windows**: Download from https://github.com/UB-Mannheim/tesseract/wiki
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

3. Run the Flask app:
```bash
python api/index.py
```

4. Test the API:
```bash
curl -X POST -F "file=@invoice.jpg" http://localhost:5000/api/process
```

## Vercel Deployment

See `DEPLOYMENT.md` for detailed deployment instructions.

## Project Structure

```
AI invoice automation/
├── api/
│   ├── index.py          # Flask API entry point
│   └── processor.py      # Invoice data extraction logic
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── README.md            # This file
```

## Supported File Formats

- PNG
- JPG/JPEG
- GIF
- BMP
- TIFF
- PDF

## Technologies Used

- **Flask**: Web framework
- **Pytesseract**: OCR engine
- **Pillow**: Image processing
- **FuzzyWuzzy**: Fuzzy string matching
- **Vercel**: Serverless deployment platform
