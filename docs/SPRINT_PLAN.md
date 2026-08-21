# FWMS — 3-Month Sprint Plan
**Project:** AI-Powered Food Waste Reduction and Smart Donation Management System
**Cadence:** Weekly sprints, 12 sprints total
**Start:** 21 Aug 2026 → **End:** 16 Nov 2026

> Sprints 1–3 already exist in Jira (FWMS-38 to FWMS-65). Sprints 4–12 below are new — create these as Jira issues under new sprints when ready.

**Folder legend:** ✅ already exists in scaffold · 🆕 create this folder when you reach this task

---

## MONTH 1 — Foundation & MVP (Weeks 1–4)
**Goal:** Working end-to-end product — auth, core CRUD, dashboards, baseline ML.

### Sprint 1 — Foundation *(due 31 Aug 2026)*
| Component | Task | Folder |
|---|---|---|
| Backend | User model (Donor/NGO/Volunteer roles) + JWT auth | `backend/app/models/` ✅ |
| Backend | Donation model + CRUD APIs | `backend/app/models/`, `backend/app/routes/` ✅ |
| Backend | NGO verification & profile endpoints | `backend/app/routes/` ✅ |
| Frontend | Connect Login/Register UI to auth API | `frontend/src/services/` ✅ |
| Frontend | Donor Dashboard (create donation, my-donations list) | `frontend/src/pages/` ✅ |
| Frontend | NGO Dashboard (browse/claim donations) | `frontend/src/pages/` ✅ |
| ML | EDA notebook — identify features | `ml-models/notebooks/` ✅ |
| ML | Preprocess dataset | `ml-models/src/`, `ml-models/data/` ✅ |
| PM/Docs | ER diagram update | `docs/` ✅ |

### Sprint 2 — Core Features *(due 7 Sep 2026)*
| Component | Task | Folder |
|---|---|---|
| Backend | Volunteer model + pickup assignment logic | `backend/app/models/`, `backend/app/services/` ✅ |
| Backend | Donation matching algorithm (proximity/quantity) | `backend/app/services/` ✅ |
| Backend | Notification service (email + in-app) | `backend/app/services/` ✅ |
| Frontend | Volunteer Dashboard | `frontend/src/pages/` ✅ |
| Frontend | Map view (Leaflet/Google Maps) | `frontend/src/components/` ✅ |
| Frontend | Donation status tracking UI | `frontend/src/components/` ✅ |
| ML | Train baseline waste-prediction model | `ml-models/src/` ✅ |
| ML | Evaluate model, document metrics | `docs/ML_REPORT.md` ✅ |
| PM/Docs | Mid-project demo prep + integration testing | `docs/` ✅ |

### Sprint 3 — MVP Integration *(due 14 Sep 2026)*
| Component | Task | Folder |
|---|---|---|
| Backend | Wire ml_integration → serve prediction API | `backend/app/ml_integration/` ✅ |
| Backend | API testing (pytest) + validation | `backend/tests/` 🆕 |
| Backend | Dockerize backend + docker-compose | project root: `Dockerfile`, `docker-compose.yml` 🆕 |
| Frontend | Polish UI/UX (responsive, loading/error states) | `frontend/src/components/`, `frontend/src/pages/` ✅ |
| Frontend | Integrate prediction insights into NGO dashboard | `frontend/src/pages/` ✅ |
| Frontend | Frontend testing + bug fixes | `frontend/src/tests/` 🆕 |
| ML | Optimize/tune model, save final artifact | `ml-models/models/` 🆕 (create to store `.pkl` files separately from `src/`) |
| ML | Write ML documentation | `docs/` ✅ |
| PM/Docs | Final QA + README + demo script | root: `README.md` 🆕 (if not already created) |
| PM/Docs | CI workflow (lint/test on push) | `.github/workflows/` ✅ |

**🎯 Milestone: MVP Demo — end of Sprint 3**

### Sprint 4 — MVP Stabilization *(due 21 Sep 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | Fix bugs found in MVP demo; input validation & error handling pass | `backend/app/routes/`, `backend/app/services/` ✅ |
| Backend | Basic Admin APIs (view all users/donations, deactivate account) | `backend/app/routes/admin.py` — reuse `backend/app/routes/` ✅ |
| Frontend | Fix UI bugs from demo feedback; empty/error states audit | `frontend/src/pages/`, `frontend/src/components/` ✅ |
| Frontend | Admin panel — basic UI (user list, donation list) | `frontend/src/pages/Admin/` 🆕 (new subfolder inside `pages/`) |
| ML | Address model weaknesses found during demo (edge cases, bad predictions) | `ml-models/src/` ✅ |
| ML | Set up model versioning (save models with version tags) | `ml-models/models/` ✅ (created in Sprint 3) |
| PM/Docs | Collect demo feedback, write retrospective, re-prioritize backlog | `docs/` ✅ |

---

## MONTH 2 — Feature Expansion & ML Maturity (Weeks 5–8)
**Goal:** Move beyond MVP — analytics, smarter ML, security, performance.

### Sprint 5 — Analytics & Reporting *(due 28 Sep 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | Analytics API — donations over time, waste saved, top NGOs | `backend/app/routes/analytics.py` — reuse `backend/app/routes/` ✅ |
| Backend | Export data endpoint (CSV/PDF report) | `backend/app/services/` ✅ |
| Frontend | Analytics dashboard UI (charts: donations trend, impact stats) | `frontend/src/pages/Analytics/` 🆕 |
| Frontend | NGO impact report page | `frontend/src/pages/` ✅ |
| ML | Feature importance analysis — explain model predictions | `ml-models/notebooks/` ✅ |
| ML | Build a simple recommendation logic (best NGO match ranking) | `ml-models/src/` ✅ |
| PM/Docs | Sprint review + Jira backlog grooming | `docs/` ✅ |

### Sprint 6 — Advanced ML *(due 5 Oct 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | API endpoint for retraining trigger / scheduled retraining job | `backend/app/ml_integration/` ✅ |
| Frontend | Surface model confidence scores in donor/NGO UI | `frontend/src/components/` ✅ |
| ML | Try 2–3 alternative models (Random Forest / XGBoost / Logistic Regression), compare | `ml-models/notebooks/` ✅ |
| ML | Hyperparameter tuning (GridSearch/RandomSearch), pick best model | `ml-models/src/` ✅ |
| ML | Build retraining pipeline script | `ml-models/src/retrain.py` — reuse `ml-models/src/` ✅ |
| PM/Docs | Validate ML results align with project objectives; update ML_REPORT.md | `docs/` ✅ |

### Sprint 7 — UX Refinement & Routing *(due 12 Oct 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | Volunteer route optimization (shortest path / nearest pickup first) | `backend/app/services/` ✅ |
| Backend | Rate-limiting & pagination on list APIs | `backend/app/routes/` ✅ |
| Frontend | UX refinement round 2 — accessibility, mobile responsiveness | `frontend/src/components/`, `frontend/src/pages/` ✅ |
| Frontend | In-app notification center (bell icon, notification list) | `frontend/src/components/Notifications/` 🆕 |
| ML | Model monitoring — log prediction accuracy over time | `ml-models/src/monitor.py` — reuse `ml-models/src/` ✅ |
| PM/Docs | Cross-browser/device testing checklist | `docs/` ✅ |

### Sprint 8 — Security & Performance *(due 19 Oct 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | Security hardening — rate limiting, JWT refresh tokens, password policies, SQL injection checks | `backend/app/services/`, `backend/app/routes/` ✅ |
| Backend | Load/performance testing on key APIs | `backend/tests/` ✅ (created Sprint 3) |
| Frontend | Frontend performance audit (lazy loading, bundle size) | `frontend/src/` ✅ |
| ML | Stress-test ML endpoint under load; add caching if needed | `backend/app/ml_integration/` ✅ |
| PM/Docs | **Mid-term full demo + review** | `docs/` ✅ |

**🎯 Milestone: Mid-Term Review Demo — end of Sprint 8**

---

## MONTH 3 — Hardening, Deployment & Final Delivery (Weeks 9–12)
**Goal:** Production-ready, deployed, tested by real users, fully documented.

### Sprint 9 — Deployment Setup *(due 26 Oct 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | Deploy backend to cloud (Render/Railway/AWS), set up environment configs | project root: `deployment/` 🆕 (e.g. `deployment/render.yaml`) |
| Backend | Set up production database (managed Postgres) | `backend/app/` ✅ (update DB config) |
| Frontend | Deploy frontend (Vercel/Netlify), connect to production backend | `deployment/` 🆕 (e.g. `deployment/vercel.json`) |
| ML | Package ML model for production serving (reproducible environment) | `ml-models/models/` ✅ |
| PM/Docs | Extend CI/CD — auto-deploy on merge to main; staging vs prod branches | `.github/workflows/` ✅ |

### Sprint 10 — User Acceptance Testing *(due 2 Nov 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | Fix backend bugs from UAT feedback | `backend/app/` ✅ |
| Frontend | Fix frontend bugs from UAT feedback | `frontend/src/` ✅ |
| ML | Validate model predictions against real/test user scenarios | `ml-models/notebooks/` ✅ |
| PM/Docs | Recruit test users, run UAT sessions, log issues in Jira | `docs/` ✅ |
| PM/Docs | Bug triage — prioritize by severity | `docs/` ✅ |

### Sprint 11 — Final Polish & Documentation *(due 9 Nov 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| Backend | Finalize API documentation (Swagger/OpenAPI) | `docs/` ✅ |
| Frontend | Final visual polish, consistent branding/theme | `frontend/src/` ✅ |
| ML | Finalize ML documentation + inference guide | `docs/` ✅ |
| PM/Docs | Write full README, user manual, architecture diagram, project report | root: `README.md`, `docs/` ✅ |
| PM/Docs | Prepare final presentation slides + demo script | `docs/` ✅ |

### Sprint 12 — Buffer & Final Submission *(due 16 Nov 2026)* 🆕
| Component | Task | Folder |
|---|---|---|
| All | Buffer for spillover bugs/tasks from Sprint 11 | — |
| Backend | Final backend smoke test | `backend/tests/` ✅ |
| Frontend | Final frontend smoke test | `frontend/src/tests/` ✅ |
| ML | Final model validation, freeze model artifact | `ml-models/models/` ✅ |
| PM/Docs | Final QA pass, tag release (`v1.0`), submit project, rehearse demo | root ✅ |

**🎯 Milestone: Final Submission & Demo Day — end of Sprint 12**

---

## New Folders Needed Over the 3 Months (in order they're needed)

| Folder | Needed by | Purpose |
|---|---|---|
| `backend/tests/` | Sprint 3 | pytest test files |
| `frontend/src/tests/` | Sprint 3 | frontend test files |
| `ml-models/models/` | Sprint 3 | saved trained model artifacts (`.pkl`), separate from `src/` scripts |
| `Dockerfile`, `docker-compose.yml` (project root) | Sprint 3 | containerize the full stack |
| `README.md` (project root) | Sprint 3 | top-level project overview |
| `frontend/src/pages/Admin/` | Sprint 4 | admin panel screens |
| `frontend/src/pages/Analytics/` | Sprint 5 | analytics dashboard screens |
| `frontend/src/components/Notifications/` | Sprint 7 | notification center UI |
| `deployment/` (project root) | Sprint 9 | cloud deployment configs (Render/Vercel/AWS files) |

Everything else reuses folders already in your scaffold (`backend/app/models/`, `routes/`, `services/`, `ml_integration/`; `frontend/src/pages/`, `components/`, `services/`; `ml-models/data/`, `notebooks/`, `src/`; `.github/workflows/`; `docs/`).

## Key Milestones Summary

| Date | Milestone |
|---|---|
| 14 Sep 2026 | MVP Demo (Sprint 3) |
| 21 Sep 2026 | Stabilized MVP (Sprint 4) |
| 19 Oct 2026 | Mid-Term Review Demo (Sprint 8) |
| 2 Nov 2026 | UAT complete (Sprint 10) |
| 16 Nov 2026 | Final Submission & Demo (Sprint 12) |
