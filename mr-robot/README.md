# 🤖 Mr Robot CTF Writeup

## 📌 Overview
After getting bored with repetitive and duplicate findings in bug bounty programs, I decided to sharpen my practical hacking skills by solving the **Mr Robot CTF machine**.

This machine is a great combination of:
- Web Enumeration
- Credential Attacks
- Reverse Shell Exploitation
- Privilege Escalation

---

## 🎯 Objectives
- Gain initial access to the system  
- Escalate privileges  
- Capture all 3 keys  

---

## 🧭 Methodology

1. Reconnaissance & Enumeration  
2. Credential Bruteforce  
3. Initial Access (Reverse Shell)  
4. Lateral Movement  
5. Privilege Escalation  

---

## 🔍 Phase 1: Reconnaissance & Enumeration

### As every Pentester Do Run a Nmap Scan 

<img width="897" height="248" alt="image" src="https://github.com/user-attachments/assets/02ae7fa7-c7fb-4f68-aca8-f61f6854aae8" />

So now Port 80 and 443 are open its a web server 

### 🔸 Directory Bruteforce

Used tool:
- `dirsearch`

Discovered:
- `/robots.txt`
- `/wp-login.php`
- WordPress-related directories  

---

### 🔸 robots.txt Analysis

Accessing:

/robots.txt


<img width="914" height="283" alt="Screenshot 2026-03-17 175643" src="https://github.com/user-attachments/assets/3711a501-3e80-4f8e-b991-f1194ebdb2e4" />


Revealed:
- ✅ First Key  
- ✅ Large Wordlist  

💡 **Insight:**  
Always check `robots.txt` — it can expose sensitive data.

---

## 🔑 Phase 2: Credential Attack on wp-login 

### 🔸 Wordlist Preparation

- Cleaned the large wordlist   
- Sorted it for better efficiency  

---

### 🔸 WordPress Login Bruteforce

Target: /wp-login.php


- Used refined wordlist  
- Performed brute-force attack  

✅ Successfully obtained **Admin Credentials**

UserName = elliot
Password = 

---

## 💻 Phase 3: Initial Access (Reverse Shell)

After logging into WordPress:

### Steps:
1. Go to **Appearance → Theme Editor**  
2. Edit a theme file (e.g., `404.php`)  
3. Inject PHP reverse shell  
4. Trigger file via browser  

📡 **Result:**  
- Got reverse shell access  

---

## 🔐 Phase 4: Lateral Movement

### 🔸 Finding Credentials

- Located an **MD5 hash** for `robot` user  

---

### 🔸 Cracking Hash

Tools used:
- `john`
- `hashcat`

✅ Cracked password successfully  

---

### 🔸 Switch User
