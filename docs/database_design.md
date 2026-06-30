# ProcureSense Database Design

## Database Overview

The ProcureSense database is designed using a normalized structure to reduce redundancy and improve analytical performance.

The project follows a two-layer architecture:

1. Raw Layer
2. Analytics Layer

---

# Raw Layer

## raw_procurements

Stores the original dataset exactly as received from the CSV file.

| Column | Type |
|---------|------|
| tender_no | VARCHAR(50) |
| tender_description | TEXT |
| agency | VARCHAR(255) |
| award_date | VARCHAR(50) |
| tender_detail_status | VARCHAR(100) |
| supplier_name | VARCHAR(255) |
| awarded_amt | DECIMAL(15,2) |

---

# Analytics Layer

## Agencies

| Column | Type |
|---------|------|
| agency_id | INT (Primary Key) |
| agency_name | VARCHAR(255) |

---

## Suppliers

| Column | Type |
|---------|------|
| supplier_id | INT (Primary Key) |
| supplier_name | VARCHAR(255) |

---

## Procurements

| Column | Type |
|---------|------|
| procurement_id | INT (Primary Key) |
| tender_no | VARCHAR(50) |
| description | TEXT |
| award_date | DATE |
| status | VARCHAR(100) |
| award_amount | DECIMAL(15,2) |
| agency_id | INT (Foreign Key) |
| supplier_id | INT (Foreign Key) |
| created_at | TIMESTAMP |

---

## Risk Scores

| Column | Type |
|---------|------|
| risk_id | INT (Primary Key) |
| procurement_id | INT (Foreign Key) |
| risk_score | DECIMAL(5,2) |
| risk_level | VARCHAR(20) |
| remarks | TEXT |

---

# Relationships

Agencies (1) --------< Procurements >-------- (1) Suppliers

Procurements (1) -------- (1) Risk Scores

Raw Procurements is used only during the ETL process and is not queried directly for analytics.