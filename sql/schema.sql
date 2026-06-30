-- =====================================================
-- ProcureSense Database Schema
-- Version 2.0
-- =====================================================

DROP DATABASE IF EXISTS procuresense;

CREATE DATABASE procuresense;

USE procuresense;

-- =====================================================
-- RAW LAYER
-- =====================================================

CREATE TABLE raw_procurements (

    tender_no VARCHAR(50),

    tender_description TEXT,

    agency VARCHAR(255),

    award_date VARCHAR(50),

    tender_detail_status VARCHAR(100),

    supplier_name VARCHAR(255),

    awarded_amt DECIMAL(15,2)

);

-- =====================================================
-- AGENCIES
-- =====================================================

CREATE TABLE agencies (

    agency_id INT AUTO_INCREMENT PRIMARY KEY,

    agency_name VARCHAR(255) NOT NULL UNIQUE

);

-- =====================================================
-- SUPPLIERS
-- =====================================================

CREATE TABLE suppliers (

    supplier_id INT AUTO_INCREMENT PRIMARY KEY,

    supplier_name VARCHAR(255) NOT NULL UNIQUE

);

-- =====================================================
-- PROCUREMENT TRANSACTIONS
-- =====================================================

CREATE TABLE procurement_transactions (

    procurement_id INT AUTO_INCREMENT PRIMARY KEY,

    tender_no VARCHAR(50),

    tender_description TEXT,

    award_date DATE,

    award_status VARCHAR(100),

    contract_value DECIMAL(15,2),

    agency_id INT,

    supplier_id INT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (agency_id)
        REFERENCES agencies(agency_id),

    FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id)

);

-- =====================================================
-- RISK SCORES
-- =====================================================

CREATE TABLE risk_scores (

    risk_id INT AUTO_INCREMENT PRIMARY KEY,

    procurement_id INT UNIQUE,

    risk_score DECIMAL(5,2),

    risk_level VARCHAR(20),

    remarks TEXT,

    FOREIGN KEY (procurement_id)
        REFERENCES procurement_transactions(procurement_id)

);