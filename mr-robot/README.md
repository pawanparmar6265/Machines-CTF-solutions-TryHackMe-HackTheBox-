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
<img width="1615" height="635" alt="image" src="https://github.com/user-attachments/assets/e611e8a8-106a-40e4-980f-82bd891411eb" />

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
- <img width="891" height="242" alt="Screenshot 2026-03-17 175702" src="https://github.com/user-attachments/assets/4f21148e-04ca-4fb1-b6db-1535ab2821ac" />

- ✅ Large Wordlist  

💡 **Insight:**  
Always check `robots.txt` — it can expose sensitive data.

---

## 🔑 Phase 2: Credential Attack on wp-login 

### 🔸 Wordlist Preparation

- Cleaned the large wordlist   cmd = cat wordlist.txt | sort -u > sorted.txt
- Sorted it for better efficiency  

---

### 🔸 WordPress Login Bruteforce

Target: /wp-login.php

tool used = wp-scan to bruteforce the login page 

- Used refined wordlist  
- Performed brute-force attack  

✅ Successfully obtained **Admin Credentials**
<img width="1916" height="513" alt="image" src="https://github.com/user-attachments/assets/6ab52192-21f3-4178-a894-ac36e412a626" />


UserName = elliot
Password = ER28-0652

---

## 💻 Phase 3: Initial Access (Reverse Shell)

After logging into WordPress: Pooking around each corner and searching on internet what i can do wiht this admin panel i found out that a reverse shell can be deployed using theme edit feature 

### Steps:
1. Go to **Appearance → Theme Editor**  
2. Edit a theme file (in my case i used 404.php`)  
3. Inject PHP reverse shell  
4. Trigger file via browser  

📡 **Result:**  
- Got reverse shell access  
<img width="1298" height="271" alt="image" src="https://github.com/user-attachments/assets/563945c6-5540-46d2-b1a1-99e25f89115d" />

---

## 🔐 Phase 4: Lateral Movement

### 🔸 Finding Credentials

after getting reverse shell i started looking files and directory in home dir of use robot i found two files the second key and a md5 hashed password 
- Located an **MD5 hash** for `robot` user

- for accessing the 2nd key i need to crack that md5 hash to get robot user password for that i used simple way instead using hashcat i used crackstation i got password in seconds 

<img width="496" height="103" alt="image" src="https://github.com/user-attachments/assets/60840e5c-f081-4777-8faa-10bf6f19d114" />
<img width="426" height="79" alt="image" src="https://github.com/user-attachments/assets/f3876d94-2468-4e7c-b917-76618757bac5" />
✅ Cracked password successfully  
<img width="1365" height="120" alt="image" src="https://github.com/user-attachments/assets/7567b328-1e0d-4b50-a2c2-af775daee1c5" />

after getting password logged as robot and got the second key 
<img width="671" height="260" alt="Screenshot 2026-03-17 175935" src="https://github.com/user-attachments/assets/475bc5d9-7d43-4f62-b046-2986d5637937" />


🏁 Retrieved **Second Key**

---

## ⚡ Phase 5: Privilege Escalation

for this i searched on internet i got some usefull methods to escalate privileges in linux system one of them worked 

source = https://safe.security/wp-content/uploads/a-hands-on-approach-to-linux-privilege-escalation.pdf 

used this cmd = find / -perm -4000 -type f 2>/dev/null

Found:
- Older version of **Nmap with SUID permissions**
- <img width="901" height="277" alt="image" src="https://github.com/user-attachments/assets/dffb09e7-9490-4b0f-b461-18214807b3cb" />

### 🔸 Exploiting Nmap for accessing root and 3rd key 

nmap --interactive

! sh 

got root shell 

🚀 **Result:**
- Root shell obtained (no password required)

---

## 👑 Phase 6: Root Access

### 🔸 Capture Final Key

Location: /root/3rdkey.txt

<img width="1919" height="1079" alt="Screenshot 2026-03-17 175248" src="https://github.com/user-attachments/assets/93e59069-16df-4d58-8ce8-4079349a16d2" />

🏁 Retrieved **Third Key**

---

## 🧠 Key Learnings

- 🔎 Enumeration is everything  
- 📄 `robots.txt` can leak sensitive info  
- 🔑 Wordlist optimization improves brute-force success  
- 🌐 WordPress admin access can lead to RCE  
- 🔓 Misconfigured SUID binaries are critical vulnerabilities  
- ⚡ Old tools (like Nmap interactive mode) can be exploited  

---

## 🧰 Tools Used

- Gobuster / Dirsearch  
- Hydra / WP brute-force  
- John the Ripper / Hashcat  
- Netcat (reverse shell)  
- Nmap  


