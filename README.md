# 📰 Verifi.AI - AI-Powered Fake News Detector

Verifi.AI is a modern full-stack Machine Learning web application that uses Natural Language Processing (NLP) and Machine Learning classifiers to analyze and predict the authenticity (Real vs Fake) of news articles, social media posts, or statements.

---

## 🚀 Features

- **Futuristic UI & Glassmorphism Design:** Built with Next.js 14, Tailwind CSS, Lucide Icons, and dynamic animations in a sleek dark-themed interface.
- **Instant News Verification:** Delivers fast and accurate verdicts using NLP TF-IDF vectorization and an ML classifier.
- **Authenticity Meter & Stats:** Displays a verdict indicator along with a live character and word counter.
- **RESTful Machine Learning API:** Ultra-fast backend service powered by FastAPI with full CORS support.
- **Sample Presets:** Pre-configured test sample buttons for quick, one-click testing.

---
## 📸 Application Preview

<img width="860" height="569" alt="image" src="https://github.com/user-attachments/assets/505354a7-444b-4ee8-91ce-d1093533dc63" />



## 🏗️ System Architecture

The following visual diagram illustrates the complete flow between the User, Next.js Frontend, FastAPI Backend, and Machine Learning Model Artifacts:

```mermaid
flowchart TD
    %% Custom Styling for High-Contrast & Wide Architecture Diagram
    classDef darkBox fill:#0f172a,stroke:#38bdf8,stroke-width:3px,color:#ffffff,font-weight:bold,rx:12px,ry:12px;
    classDef purpleBox fill:#581c87,stroke:#c084fc,stroke-width:3px,color:#ffffff,font-weight:bold,rx:12px,ry:12px;
    classDef modelBox fill:#6b21a8,stroke:#e9d5ff,stroke-width:3px,color:#ffffff,font-weight:bold,rx:12px,ry:12px;
    classDef dbBox fill:#064e3b,stroke:#34d399,stroke-width:3px,color:#ffffff,font-weight:bold,rx:12px,ry:12px;

    User["👤 User / Browser<br/><sub>Text Input</sub>"]:::darkBox
    Frontend["💻 Next.js UI (app/page.tsx)<br/><sub>Tailwind CSS + Glassmorphism</sub>"]:::darkBox
    Backend["⚡ FastAPI Backend (app.py)<br/><sub>/predict endpoint + CORS</sub>"]:::purpleBox
    
    TFIDF["🔤 TF-IDF Vectorizer<br/><sub>tfidf_vectorizer.pkl</sub>"]:::modelBox
    Model["🧠 ML Classifier Model<br/><sub>fake_news_model.pkl</sub>"]:::modelBox
    Storage[("🗄️ Model Artifacts<br/><sub>joblib files</sub>")]:::dbBox

    %% Interactions and Connections
    User -->|1. Type & Submit| Frontend
    Frontend -->|2. HTTP POST Request| Backend
    Backend -.->|6. JSON Prediction Response| Frontend

    Backend -->|3. Raw Text| TFIDF
    TFIDF -->|4. Feature Vector| Model
    Model -->|5. Output Result| Backend

    Storage -->|Load| TFIDF
    Storage -->|Load| Model
```


---

## 🛠️ Tech Stack

### **Frontend**
- **Framework:** Next.js (React)
- **Styling:** Tailwind CSS, Glassmorphism UI
- **Icons:** Lucide React

### **Backend**
- **Framework:** FastAPI (Python)
- **Server:** Uvicorn
- **ML & Data Processing:** Scikit-Learn, Joblib, TF-IDF Vectorizer
- **Middleware:** CORSMiddleware, python-multipart

---

## 📁 Project Structure

```text
fake-news-detector/
├── fake-news-backend/
│   ├── app.py                   # FastAPI Application & Endpoints
│   ├── fake_news_model.pkl      # Trained ML Classifier Model
│   ├── tfidf_vectorizer.pkl     # Trained TF-IDF Vectorizer
│   └── requirements.txt         # Python Dependencies
└── fake-news-frontend/
    ├── app/
    │   └── page.tsx             # Next.js UI Main Component
    ├── public/
    └── package.json
```

---

## ⚙️ Installation & Setup

### **1. Backend Setup (FastAPI)**

```bash
# Navigate to backend directory
cd fake-news-backend

# Create virtual environment (Optional but Recommended)
python -m venv venv

# Activate Virtual Environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app:app --reload --port 8000
```
Backend API will be running live at: `https://fake-news-api-fvab.onrender.com/`

---

### **2. Frontend Setup (Next.js)**

```bash
# Navigate to frontend directory
cd fake-news-frontend

# Install packages
npm install

# Run Development Server
npm run dev
```
Frontend will be running live at: `https://fake-news-frontend-wine.vercel.app/`

---

## 🔌 API Endpoint

### `POST /predict`

- **Content-Type:** `application/x-www-form-urlencoded`
- **Body:** `news` (string)

#### **Example Response:**
```json
{
  "prediction": "Real News"
}
```

---

## 🛡️ License

Distributed under the MIT License.
