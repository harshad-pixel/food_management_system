# Jira Setup Guide (for SE subject formality + real coordination)

## 1. Project Setup
- Create a **Scrum** project (not Kanban) in Jira — maps well to a semester with sprints for the report.
- Project key suggestion: `FWDS` (Food Waste Donation System).
- Link the GitHub repo: Jira → Project Settings → GitHub for Jira app → connect repo (enables commit/PR → issue linking with `FWDS-12` in commit messages).

## 2. Epics (map directly to README modules)

1. `FWDS-E1` Auth & User Management
2. `FWDS-E2` Donation Posting Module
3. `FWDS-E3` Smart Matching Engine
4. `FWDS-E4` ML Waste Prediction
5. `FWDS-E5` Route Optimization
6. `FWDS-E6` Notifications
7. `FWDS-E7` Admin Dashboard & Analytics
8. `FWDS-E8` Freshness Classification (stretch)
9. `FWDS-E9` Testing & QA
10. `FWDS-E10` Deployment & DevOps

## 3. Sample Backlog (Sprint 1)

| Issue | Type | Epic | Assignee area |
|---|---|---|---|
| Set up repo structure + CI skeleton | Task | E10 | Backend/QA |
| Design ER diagram & finalize schema | Task | E1 | Backend |
| Implement user registration/login API | Story | E1 | Backend |
| Build login/register UI | Story | E1 | Frontend |
| Set up PostgreSQL + SQLAlchemy models | Task | E1 | Backend |
| Collect/prepare synthetic dataset for ML | Task | E4 | ML |

## 4. Sprint Cadence
- Sprint length: 2 weeks (aligns with 12–14 week timeline → ~6 sprints)
- Sprint ceremonies (lightweight, for 4-person team): 15-min standup (async on WhatsApp/Discord is fine), sprint planning at start, sprint review/retro at end.

## 5. Board Columns
`Backlog → To Do → In Progress → In Review (PR open) → Done`

## 6. Reporting for Submission
- Use Jira's **Burndown Chart** and **Sprint Report** — export screenshots for your SE subject report/viva to show Agile process was followed.
- Keep a `docs/sprint-reports/` folder with 1-page summaries per sprint (what was planned vs done) — useful evidence for grading.
