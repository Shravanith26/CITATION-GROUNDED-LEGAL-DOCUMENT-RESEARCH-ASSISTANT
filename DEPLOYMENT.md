# 🚀 Deployment & Permanent Hosting Guide

This guide provides end-to-end instructions for deploying the **Citation-Grounded Legal Document Research Assistant & Citizen Rights Advisory System**.

Follow **Option 1** or **Option 2** for a **permanent, 24/7 cloud URL that never expires and never depends on your local computer being turned on**.

---

## 🌟 Option 1: Streamlit Community Cloud (Recommended — 100% Free, Official, Permanent 24/7)

Streamlit Community Cloud is the official, zero-cost cloud hosting platform by Snowflake. It runs directly from your GitHub repository.

### Prerequisites
* Your code is on GitHub: `https://github.com/Shravanith26/CITATION-GROUNDED-LEGAL-DOCUMENT-RESEARCH-ASSISTANT`
* A free Streamlit Community Cloud account at [share.streamlit.io](https://share.streamlit.io).

### Step-by-Step Setup (Takes 2 Minutes):
1. Navigate to **[share.streamlit.io](https://share.streamlit.io)** and log in with your GitHub account.
2. Click **"New app"** (or **"Create app"** in the top right).
3. Fill in the deployment details:
   - **Repository:** `Shravanith26/CITATION-GROUNDED-LEGAL-DOCUMENT-RESEARCH-ASSISTANT`
   - **Branch:** `main`
   - **Main file path:** `app_streamlit.py`
   - **App URL (optional):** Choose a custom subdomain (e.g., `citation-grounded-legal-assistant.streamlit.app`).
4. Click **"Deploy!"**.
5. Streamlit will automatically clone the repository, install `requirements.txt`, initialize the database, and launch your application.

---

### ⚠️ How to Prevent Common Issues on Streamlit Cloud

#### 1. Preventing "You do not have access to this app or it does not exist"
* **Cause**: The app is set to **Private** visibility, restricting access only to your logged-in GitHub account. When an outside user or evaluator opens the link, Streamlit displays: *"You do not have access to this app or it does not exist"*.
* **Fix**:
  1. Open your dashboard at [share.streamlit.io](https://share.streamlit.io).
  2. Click the **three vertical dots (`⋮`)** next to your app name.
  3. Click **Settings** ➔ navigate to **Sharing** (or **General**).
  4. Ensure the visibility is toggled to **"Public"** (or uncheck *"Restrict viewer access"*).
  5. Save changes. Now **anyone in the world can open the link directly with zero login required**.

#### 2. Preventing "This site can’t be reached"
* **Cause**: Trying to access a local computer tunnel (`trycloudflare.com`) after the laptop has gone to sleep, Wi-Fi disconnected, or the quick tunnel session ended.
* **Fix**: When deployed on **Streamlit Community Cloud**, the app runs on dedicated AWS/Snowflake servers. It does **not** run on your laptop, so **it never disconnects when you close your computer**.

#### 3. Preventing App Hibernation / Sleep
* Free Streamlit Cloud apps enter sleep mode if there are 0 visits over 7 consecutive days.
* If your app goes to sleep, visiting the URL will show a blue button: **"Yes, get this app back up!"**. Clicking it wakes the app in ~30 seconds.
* To keep it permanently awake, you can ping the URL periodically or set up a free uptime monitor (e.g. UptimeRobot or Cron-job.org).

---

## 🌟 Option 2: Hugging Face Spaces (100% Free, Never Sleeps, 16 GB RAM)

Hugging Face Spaces provides permanent 24/7 hosting with 16 GB RAM that does not sleep.

### Step-by-Step Setup:
1. Create a free account at [huggingface.co](https://huggingface.co).
2. Go to **New Space** (`https://huggingface.co/new-space`).
3. Set your Space details:
   - **Space Name:** `legal-document-research-assistant`
   - **License:** `mit`
   - **SDK:** `Streamlit`
   - **Space Hardware:** `CPU basic • 2 vCPU • 16GB` (Free)
   - **Visibility:** `Public`
4. Connect or duplicate from your GitHub repository `Shravanith26/CITATION-GROUNDED-LEGAL-DOCUMENT-RESEARCH-ASSISTANT`.
5. Hugging Face will automatically read `requirements.txt` and launch `app_streamlit.py`.
6. Your permanent link will be: `https://huggingface.co/spaces/<your-username>/legal-document-research-assistant`.

---

## 🐳 Option 3: Docker & Production Container

To run the containerized stack on any cloud VPS (AWS EC2, Google Cloud Run, DigitalOcean):

```bash
# Build the Docker image
docker build -t legal-research-assistant .

# Run the container on port 8501 (Streamlit) or 8000 (FastAPI)
docker run -d -p 8501:8501 --name legal_assistant legal-research-assistant
```

Or using Docker Compose:
```bash
docker-compose up -d --build
```

---

## 💻 Option 4: Local Demonstration & Stable Tunnel

If you want to present the app locally from your laptop with an external public link for judges/colleagues:

### Step 1: Start the Streamlit Application
```bash
./venv/bin/streamlit run app_streamlit.py --server.port 8501 --server.headless true
```

### Step 2: Start the Resilient HTTP/2 Auto-Reconnecting Tunnel
```bash
./scripts/start_stable_tunnel.sh 8501
```
* Uses **HTTP/2 (TCP)** instead of QUIC (UDP) to prevent connection drops caused by Wi-Fi route renegotiation.
* Automatically detects disconnections and reconnects within 3 seconds.
* Note: Keep your laptop screen awake and internet active during local demonstrations.
