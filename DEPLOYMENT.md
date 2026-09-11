# Deployment Guide: Citation-Grounded Legal Document Research Assistant

This guide covers all deployment options for the project:
1. **Option 1: 1-Click Free Cloud Deployment on Render (Recommended for online demos)**
2. **Option 2: 1-Click Free Frontend Hosting on Vercel / Netlify**
3. **Option 3: Containerized Deployment via Docker & Docker Compose**
4. **Option 4: Local Production Deployment (Zero-cost presentation mode on Mac/Windows)**

---

## Option 1: 1-Click Free Cloud Deployment on Render (Backend + UI)

[Render](https://render.com) offers a free tier for hosting web services that directly integrates with GitHub.

### Step-by-Step Instructions:
1. Go to [https://render.com](https://render.com) and log in with your GitHub account.
2. Click **New +** → **Web Service**.
3. Select your repository: `Shravanith26/CITATION-GROUNDED-LEGAL-DOCUMENT-RESEARCH-ASSISTANT`.
4. Configure the settings:
   - **Name:** `legal-research-assistant`
   - **Runtime:** `Python 3`
   - **Build Command:**
     ```bash
     pip install -r backend/requirements.txt && python scripts/build_index.py
     ```
   - **Start Command:**
     ```bash
     cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
     ```
   - **Instance Type:** `Free`
5. Click **Create Web Service**.
6. Render will automatically build the environment, index the legal documents, and provide you with a public HTTPS link (e.g. `https://legal-research-assistant.onrender.com`) where the web dashboard is live!

---

## Option 2: Deploy Frontend on Vercel (Optional)

If you want to host the React frontend separately:
1. Log into [https://vercel.com](https://vercel.com) with your GitHub account.
2. Click **Add New...** → **Project**.
3. Import `CITATION-GROUNDED-LEGAL-DOCUMENT-RESEARCH-ASSISTANT`.
4. Set **Root Directory** to `frontend`.
5. Under Environment Variables, set `VITE_API_URL` to your Render backend URL.
6. Click **Deploy**.

---

## Option 3: Docker & Docker Compose Deployment

Run the complete containerized stack locally or on any cloud VPS (AWS, GCP, DigitalOcean):

### Using Docker:
```bash
# Build the Docker image
docker build -t legal-research-assistant .

# Run the container
docker run -d -p 8000:8000 --name legal_assistant legal-research-assistant
```

### Using Docker Compose:
```bash
docker-compose up -d --build
```
Open [http://localhost:8000](http://localhost:8000) to access the application.

---

## Option 4: Local Production Deployment (On Your Mac/Laptop)

For offline college viva or evaluations without depending on cloud networks:

```bash
cd /Users/shravani/.gemini/antigravity/scratch/Citation-Grounded-Legal-Document-Research-Assistant

# Activate virtual environment
source venv/bin/activate

# Start production server with Uvicorn
cd backend
python run.py
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in Chrome/Safari.
