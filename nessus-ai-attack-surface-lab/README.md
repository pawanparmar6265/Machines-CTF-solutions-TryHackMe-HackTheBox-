# Nessus-Based Traditional & AI/LLM Attack Surface Assessment Lab

## Overview

This project is a hands-on vulnerability assessment lab focused on understanding how Nessus can be used for both traditional infrastructure vulnerability scanning and modern AI/LLM attack surface detection.

The lab includes:

- Host discovery scan on a local lab network
- Basic Network Scan against Metasploitable 2
- AI/LLM exposure scan against an intentionally exposed Ollama API
- Manual validation of exposed AI API access
- Risk analysis and remediation documentation

The goal of this project was not only to run automated scans, but also to understand how vulnerabilities should be interpreted from both a technical and business-risk perspective.

---

## Project Objectives

- Set up a safe local vulnerability assessment lab
- Perform host discovery on a private IP range
- Run a Nessus Basic Network Scan against Metasploitable 2
- Identify vulnerable services, outdated software, and insecure configurations
- Set up an intentionally exposed AI/LLM runtime using Ollama
- Detect AI/LLM-related exposure using Nessus
- Validate exposed AI API access manually
- Document findings, evidence, risk, impact, and remediation steps

---

## Lab Environment

| Component | Description |
|---|---|
| Scanner Machine | Kali Linux |
| Scanner Tool | Nessus Essentials |
| Traditional Target | Metasploitable 2 |
| AI/LLM Target | Ollama API |
| AI Runtime Port | 11434 |
| Network Type | Local lab network |
| Report Formats | PDF, CSV, `.nessus` |

---

## Scans Performed

### 1. Host Discovery Scan

A host discovery scan was performed on the local lab IP range to identify active hosts before running vulnerability scans.

**Purpose:**

- Identify live systems in the lab network
- Confirm target availability
- Reduce unnecessary scanning
- Follow a realistic VAPT workflow

---

### 2. Basic Network Scan on Metasploitable 2

A Nessus Basic Network Scan was performed against Metasploitable 2.

Metasploitable 2 was used because it is an intentionally vulnerable virtual machine commonly used for security training and vulnerability assessment practice.

**Purpose:**

- Detect exposed services
- Identify known vulnerabilities
- Analyze severity levels
- Understand scanner-generated vulnerability reports
- Practice remediation planning

Common services found on Metasploitable 2 include:

- FTP
- SSH
- Telnet
- Apache
- Samba
- MySQL
- PostgreSQL
- Tomcat
- NFS

---

### 3. AI/LLM Exposure Scan using Ollama

An AI/LLM lab target was created using Ollama.

Ollama was intentionally configured to listen on the network interface:

```bash
OLLAMA_HOST=0.0.0.0:11434
