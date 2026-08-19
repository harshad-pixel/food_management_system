# AI-Powered Food Waste Reduction and Smart Donation Management System

A machine-learning-driven platform that connects food surplus donors (restaurants, hotels, caterers, households) with NGOs/shelters, predicts food waste before it happens, and optimizes pickup routing for donations — reducing food waste and improving last-mile donation logistics.

**Team:** 4 members | **Type:** Academic Software Engineering project (with Jira-based Agile workflow)

---

## 1. Problem Statement

Tons of edible food is wasted daily by restaurants, hostels, and event caterers while NGOs struggle to source consistent donations. There is no smart system that (a) predicts *when and how much* surplus food will be generated, (b) matches it to the *nearest, most relevant* receiving NGO, and (c) optimizes pickup logistics in real time.

## 2. Objectives

- Predict food surplus/waste using historical order & inventory data (ML regression/time-series).
- Auto-match surplus donations to nearby NGOs based on quantity, food type, perishability, and location.
- Classify food freshness/edibility from images (CNN) to flag donation safety.
- Optimize pickup routes for volunteers/NGO vehicles (shortest path / nearest-neighbor).
- Provide dashboards for donors, NGOs, and admins with real-time tracking and analytics.

## 3. Core Features (MVP)

| Module | Description |
|---|---|
| Auth & Roles | Donor / NGO / Admin / Volunteer login (JWT) |
| Donation Posting | Donor lists surplus food (type, qty, expiry, pickup window) |
| ML Waste Prediction | Forecast expected surplus per donor using past data |
| Smart Matching | Rule-based + ML scoring to match donation → nearest eligible NGO |
| Food Freshness Check | Optional image upload → CNN classifies fresh/spoiled |
| Route Optimization | Suggests optimal pickup route for volunteers |
| Notifications | Email/SMS alert to NGO when a match is found |
| Dashboard & Analytics | Waste-saved metrics, donation history, impact charts |

## 4. Stretch Features

- Chatbot for donors to log donations via natural language
- Predictive demand forecasting per NGO (what they'll need next week)
- Gamification / leaderboard for top donors
- Multi-language support

## 5. Tech Stack

| Layer | Technology | Why |
|---|---|---|
| Frontend | React.js + Tailwind CSS | Fast to build, component-based, good for dashboards |
| Backend API | Python (FastAPI) | Same language as ML layer → easy model integration, async, auto docs |
| Database | PostgreSQL | Relational data (users, donations, NGOs) with geo queries (PostGIS optional) |
| ML/DS | scikit-learn, pandas, numpy | Waste prediction (regression), matching score |
| Deep Learning (optional) | TensorFlow/Keras or PyTorch | Food image freshness classification (CNN, transfer learning e.g. MobileNetV2) |
| Auth | JWT (python-jose) + bcrypt | Stateless auth |
| Maps/Routing | OpenRouteService API or Google Maps Directions API | Route optimization, distance matrix |
| Notifications | SendGrid (email) / Twilio (SMS) | Alert NGOs |
| Containerization | Docker + docker-compose | Consistent dev/deploy environment |
| CI/CD | GitHub Actions | Auto lint/test on push |
| Hosting | Frontend: Vercel/Netlify · Backend: Render/Railway · DB: Supabase/Neon (free Postgres) | Free-tier friendly for academic projects |
| PM Tool | Jira | Sprint planning, backlog, board (see `docs/JIRA_SETUP.md`) |

## 6. System Architecture (high level)

```
[React Frontend] --> [FastAPI Backend] --> [PostgreSQL]
                              |
                              +--> [ML Service: waste prediction, matching score]
                              |
                              +--> [CNN Service: freshness classification]
                              |
                              +--> [Routing API: pickup optimization]
                              |
                              +--> [Notification Service: email/SMS]
```

Backend exposes REST endpoints; ML models are loaded as Python modules inside the same FastAPI app (`backend/app/ml_integration/`) for MVP simplicity — no need for a separate microservice unless load demands it later.

## 7. Repository Structure

```
food-waste-donation-system/
├── backend/
│   ├── app/
│   │   ├── routes/          # API endpoints (auth, donations, matching, ngo)
│   │   ├── models/          # DB models (SQLAlchemy)
│   │   ├── services/        # business logic (matching, notifications)
│   │   └── ml_integration/  # loads trained models, inference functions
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/           # Donor, NGO, Admin dashboards
│   │   └── services/        # API calls (axios)
│   └── package.json
├── ml-models/
│   ├── notebooks/           # EDA, training experiments
│   ├── src/                 # training scripts, preprocessing
│   ├── data/                # sample/mock datasets (real data gitignored if large)
│   └── requirements.txt
├── docs/
│   ├── PROJECT_PLAN.md
│   ├── JIRA_SETUP.md
│   ├── ER_DIAGRAM.md
│   └── API_SPEC.md
├── .github/workflows/       # CI pipelines
├── docker-compose.yml
├── .gitignore
└── README.md
```

<!-- ## 8. Team Roles (suggested split for 4 members)

| Role | Responsibility |
|---|---|
| Backend + DB Lead | FastAPI routes, PostgreSQL schema, auth, deployment |
| Frontend Lead | React UI, dashboards, API integration |
| ML/Data Lead | Waste prediction model, matching algorithm, optional CNN |
| QA + PM/Jira Lead | Testing, Jira board management, documentation, CI/CD, integration |

(Roles overlap in practice — everyone should touch Git and understand the full flow for the viva/demo.)

## 9. Getting Started (once repo is on GitHub)

```bash
git clone <your-repo-url>
cd food-waste-donation-system

# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd ../frontend
npm install
npm run dev
```

## 10. Suggested Timeline (12–14 week academic sem)

| Weeks | Milestone |
|---|---|
| 1–2 | Requirements finalize, ER diagram, Jira backlog, repo setup |
| 3–4 | Auth + basic donor/NGO CRUD (backend + frontend) |
| 5–6 | Donation posting flow + DB integration |
| 7–8 | ML waste prediction model (v1) + matching logic |
| 9 | Route optimization + notifications |
| 10 | Freshness classifier (stretch, if time permits) |
| 11 | Testing, bug fixes, dashboard polish |
| 12 | Deployment, documentation, demo prep |
| 13–14 | Buffer + report writing + presentation |

## 11. License

VIT-Pune — see `LICENSE`. -->
