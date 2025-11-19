# Vercel Deployment Guide

## Prerequisites

Before deploying, you need Git installed on your system. Choose one of the following:

### **Option A: Install Git for Windows**

1. Download Git from: https://git-scm.com/download/win
2. Run the installer with default settings
3. Restart PowerShell after installation
4. Verify installation: `git --version`

### **Option B: Deploy Without Git (Direct Vercel CLI)**

If you prefer not to install Git, you can deploy directly using Vercel CLI (see Alternative Deployment Method below).

---

## 5-Step Deployment Process (Using Git/GitHub)

Follow these exact steps to deploy your Intelligent Invoice Processing API to Vercel using Git/GitHub.

---

### **Step 1: Initialize Git Repository and Connect to GitHub**

**First, ensure Git is installed** (see Prerequisites above).

If you haven't already created a GitHub repository, do so now:

1. Go to https://github.com and create a new repository named `invoice-processing-api`
2. **Do NOT** initialize with README, .gitignore, or license (your local project already has files)

Then, in your project directory, initialize Git and push to GitHub:

```powershell
# Initialize git repository (if not already done)
git init

# Create .gitignore file to exclude unnecessary files
echo "__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.env
.venv
*.log
.DS_Store
.vercel" | Out-File -FilePath .gitignore -Encoding utf8

# Add all files to git
git add .

# Commit the files
git commit -m "Initial commit: Invoice Processing API"

# Add your GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/invoice-processing-api.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**What this does:** Creates version control for your project and uploads your code to GitHub, which Vercel will use for deployment.

---

### **Step 2: Install Vercel CLI (If Not Already Installed)**

Verify or install the Vercel CLI:

```powershell
# Check if Vercel CLI is installed
vercel --version

# If not installed, install it globally via npm
npm install -g vercel
```

**What this does:** Ensures you have the Vercel command-line tool available for deployment.

---

### **Step 3: Log In to Vercel**

Authenticate your Vercel CLI with your Vercel account:

```powershell
vercel login
```

This will:
- Open a browser window asking you to log in
- Authenticate your CLI session with your Vercel account
- Link your local machine to your Vercel account

**What this does:** Connects your local development environment to your Vercel account so you can deploy projects.

---

### **Step 4: Link Your Project to Vercel**

Navigate to your project directory and run:

```powershell
cd "d:\Study\Projects\AI invoice automation"
vercel
```

You'll be prompted with several questions:

```
? Set up and deploy "d:\Study\Projects\AI invoice automation"? [Y/n] Y
? Which scope do you want to deploy to? [Your Vercel Account]
? Link to existing project? [y/N] N
? What's your project's name? invoice-processing-api
? In which directory is your code located? ./
```

**Answer the prompts as follows:**
1. **Set up and deploy**: Press `Y` (Yes)
2. **Which scope**: Select your Vercel account
3. **Link to existing project**: Press `N` (No - this is a new project)
4. **Project name**: `invoice-processing-api` (or your preferred name)
5. **Code directory**: `./ ` (current directory - just press Enter)

Vercel will then:
- Analyze your project structure
- Detect the `vercel.json` configuration
- Build and deploy your serverless function
- Provide you with deployment URLs

**What this does:** Creates a new project on Vercel, analyzes your code, and performs the first deployment.

---

### **Step 5: Configure Environment and Deploy to Production**

After the initial deployment, push to production:

```powershell
# Deploy to production
vercel --prod
```

**Important Note About Tesseract:**

⚠️ **Vercel Limitation**: Standard Vercel deployments do not include Tesseract OCR binaries. You have two options:

**Option A - Use Docker-based Deployment:**
You'll need to create a `Dockerfile` and use Vercel's container support. This is more complex but allows full Tesseract support.

**Option B - Switch to Alternative OCR Service (Recommended for Vercel):**
Use a cloud-based OCR service like:
- **Google Cloud Vision API**
- **AWS Textract**
- **Azure Computer Vision**
- **OCR.space API** (free tier available)

To use Option B, modify `api/processor.py` to call an external OCR API instead of pytesseract.

**Optional - Add Environment Variables:**

If you need API keys or configuration:

```powershell
# Add environment variables via CLI
vercel env add VENDOR_LIST

# Or add them via Vercel Dashboard:
# 1. Go to vercel.com/dashboard
# 2. Select your project
# 3. Go to Settings > Environment Variables
# 4. Add your variables
```

**What this does:** Deploys your API to Vercel's production environment with a permanent URL.

---

## Verification

After deployment, Vercel will provide URLs like:

- **Production**: `https://invoice-processing-api.vercel.app`
- **Preview**: `https://invoice-processing-api-git-main-yourname.vercel.app`

Test your API:

```powershell
# Health check
curl https://invoice-processing-api.vercel.app/api/health

# Process an invoice (using PowerShell)
$form = @{
    file = Get-Item -Path "path\to\invoice.jpg"
}
Invoke-RestMethod -Uri "https://invoice-processing-api.vercel.app/api/process" -Method Post -Form $form
```

---

## Continuous Deployment

Once linked to GitHub, any push to your `main` branch will automatically trigger a new deployment:

```powershell
# Make changes to your code
git add .
git commit -m "Updated invoice extraction logic"
git push origin main
```

Vercel will automatically:
1. Detect the push
2. Build your project
3. Deploy to a preview URL
4. Promote to production (if pushing to main branch)

---

## Alternative Deployment Method (Without Git)

If you don't want to install Git or use GitHub, you can deploy directly:

```powershell
# Navigate to your project directory
cd "d:\Study\Projects\AI invoice automation"

# Deploy directly to Vercel
vercel --prod
```

This will:
- Upload your local files directly to Vercel
- Skip GitHub integration
- Deploy immediately to production

**Limitation:** You won't get automatic deployments on code changes. You'll need to run `vercel --prod` manually each time you update your code.

---

## Troubleshooting

### Issue: "Build failed" errors

**Solution:** Check the Vercel deployment logs in your dashboard at vercel.com/dashboard

### Issue: Module import errors

**Solution:** Ensure all dependencies are listed in `requirements.txt`

### Issue: Tesseract not found

**Solution:** See "Important Note About Tesseract" above - switch to cloud-based OCR

### Issue: File upload size limits

**Solution:** Vercel has a 4.5MB request body limit for serverless functions. For larger files, consider using Vercel Blob storage or S3.

---

## Next Steps

1. **Add Authentication**: Implement API key validation for security
2. **Database Integration**: Store processed invoices in a database
3. **Webhook Support**: Add callbacks for asynchronous processing
4. **Rate Limiting**: Implement request throttling
5. **Custom Domain**: Connect your own domain in Vercel settings

---

## Resources

- Vercel Documentation: https://vercel.com/docs
- Vercel Python Runtime: https://vercel.com/docs/functions/serverless-functions/runtimes/python
- GitHub Integration: https://vercel.com/docs/concepts/git/vercel-for-github
