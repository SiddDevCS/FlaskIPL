# Visitor Info Logger (Educational Use Only)

This is a Flask-based web application that logs detailed visitor information, such as IP address, geolocation, user agent, and more. It is intended **only for learning and cybersecurity awareness purposes**.

> **Disclaimer: This project is for educational and ethical use only. Do not deploy or use it in a way that violates privacy, consent, or applicable laws. Unauthorized tracking or logging of individuals may be illegal.**

---

## Features

* Logs:

  * IP address and hostname
  * Geolocation data (city, region, country, latitude, longitude)
  * ISP and ASN info
  * Device/browser/OS details
  * Referrer URL
* Uses [ipapi.co](https://ipapi.co) for IP geolocation
* Parses user agent strings using `user_agents` library
* Stores logs in `visitor_logs.txt`
* Displays a warning page to visitors
* Designed with simple HTML/CSS response for demonstration

---

## Requirements

* Python 3.x
* Flask
* Requests
* user\_agents

Install dependencies:

```bash
pip install flask requests pyyaml user-agents
```

---

## How to Run

```bash
python script_name.py
```

Then visit `http://localhost:5001` or host it externally for remote testing.

---

## File Logging

All captured data is logged into `visitor_logs.txt` in a human-readable format for review and analysis.
