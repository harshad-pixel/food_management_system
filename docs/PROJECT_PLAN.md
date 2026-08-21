# Project Plan — AI-Powered Food Waste Reduction and Smart Donation Management System

## 1. Functional Requirements

- FR1: Donor can register, log in, and post a surplus food listing (type, quantity, expiry/best-before time, pickup address, photo).
- FR2: NGO/receiver can register, set service area & food preferences, and view/accept matched donations.
- FR3: System auto-matches a new donation to the best-fit NGO(s) using a scoring function (distance, quantity fit, food-type match, urgency).
- FR4: ML module predicts expected surplus quantity for a donor based on historical listings (regression).
- FR5: Optional CNN module classifies an uploaded food image as fresh/consumable vs. spoiled.
- FR6: System notifies the matched NGO (email/SMS) and lets them accept/reject within a time window.
- FR7: Volunteer/NGO gets an optimized pickup route when multiple donations are accepted in a session.
- FR8: Admin dashboard shows total food saved, active donors/NGOs, donation history, and waste-prediction accuracy.
- FR9: All users can view their donation/pickup history.

## 2. Non-Functional Requirements

- **Performance:** Matching + notification should complete within a few seconds of a new listing.
- **Scalability:** Should handle growth from a handful of donors/NGOs (demo scale) to city-scale without redesign (stateless API, indexed DB queries).
- **Security:** Passwords hashed (bcrypt), JWT-based auth, role-based access control.
- **Usability:** Simple dashboard flows for non-technical NGO staff.
- **Reliability:** Graceful fallback if ML service fails — fall back to rule-based matching (distance + food type only).
- **Maintainability:** Modular backend (routes/services/models separated), documented API (FastAPI auto Swagger docs).

## 3. ML Component Details

### 3.1 Waste/Surplus Prediction
- **Type:** Regression / time-series forecasting.
- **Input features:** day of week, past donation quantities, event flags (holidays/festivals), donor category (restaurant/hostel/event).
- **Models to try:** Linear Regression baseline → Random Forest Regressor → (stretch) simple LSTM if time series data is rich enough.
- **Dataset:** No public dataset fits exactly — plan to generate a **synthetic dataset** (documented as such in the report) modeled on realistic restaurant waste patterns, or adapt a public food-waste/retail-demand dataset (e.g., Kaggle "Restaurant Waste" or "Food Demand Forecasting" datasets) for feature-engineering practice.

### 3.2 Matching Algorithm
- **Type:** Weighted scoring function (not necessarily deep ML — a hybrid of rules + a learned weight model is fine and defensible for an SE project).
- **Score = w1·(1/distance) + w2·(quantity fit) + w3·(food type match) + w4·(NGO reliability score)**
- Weights can start hand-tuned, then optionally learned via logistic regression on historical accept/reject outcomes (stretch).

### 3.3 Freshness Classification (stretch)
- **Type:** Image classification, transfer learning.
- **Model:** MobileNetV2 or EfficientNet-B0 (lightweight, fine-tunable on small datasets).
- **Dataset:** Public "Fruits Fresh and Rotten" / "Food Freshness" datasets on Kaggle for prototype; clearly labeled as a proof-of-concept, not production-grade food safety detection.

## 4. Database Schema (core entities)

- **User**(id, name, email, password_hash, role[donor/ngo/admin/volunteer], phone)
- **Donor**(id, user_id FK, org_name, address, lat, lng, category)
- **NGO**(id, user_id FK, org_name, address, lat, lng, service_radius_km, food_prefs)
- **Donation**(id, donor_id FK, food_type, quantity, unit, expiry_time, status, image_url, created_at)
- **Match**(id, donation_id FK, ngo_id FK, score, status[pending/accepted/rejected], matched_at)
- **Pickup**(id, match_id FK, volunteer_id FK, route_order, picked_at, delivered_at)
- **WastePrediction**(id, donor_id FK, predicted_qty, predicted_date, model_version)

(Full ER diagram to be added in `docs/ER_DIAGRAM.md` — draw.io or dbdiagram.io recommended.)

## 5. API Endpoints (initial spec — expand in `docs/API_SPEC.md`)

```
POST   /auth/register
POST   /auth/login
POST   /donations                 # donor creates listing
GET    /donations/{id}
GET    /donations/nearby?lat=&lng=
POST   /donations/{id}/match      # trigger matching
POST   /matches/{id}/accept
POST   /matches/{id}/reject
GET    /ngo/{id}/matches
POST   /ml/predict-waste
POST   /ml/classify-freshness
GET    /routes/optimize?ngo_id=
GET    /admin/stats
```

## 6. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| No real donation data available | Use synthetic + public proxy datasets; document clearly |
| ML model overfits on small data | Keep models simple (RF/linear), emphasize matching-logic engineering over model complexity |
| Team coordination across 4 members | Jira board + weekly standup + GitHub branch protection (see below) |
| Scope creep | MVP first (auth + posting + matching); stretch features only after MVP is demo-stable |

## 7. Git Workflow

- `main` — always deployable/demo-ready
- `dev` — integration branch
- `feature/<name>` — one branch per feature, PR into `dev`
- PRs require at least 1 teammate review before merge (set as GitHub branch protection rule)
- Commit convention: `feat:`, `fix:`, `docs:`, `chore:`, `test:` prefixes
