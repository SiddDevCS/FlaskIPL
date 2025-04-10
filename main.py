from flask import Flask, request, render_template_string, make_response
from datetime import datetime
import logging


import requests
from user_agents import parse
import socket

app = Flask(__name__)

# config logging
logging.basicConfig(filename='visitor_logs.txt', level=logging.INFO)

# get IP location and network info function
def get_ip_data(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/', timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"[ERROR] IP data fetch failed: {e}")
    return {}

@app.route('/')


def logger():
    
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    
    user_agent_string = request.headers.get('User-Agent')
    referrer = request.referrer or "None"

    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    user_agent = parse(user_agent_string)
    ip_info = get_ip_data(ip)

    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except:
        hostname = "Unknown"

    log_data = {
        'Timestamp': timestamp,
        'IP Address': ip,
        'Hostname': hostname,
        'City': ip_info.get('city', 'Unknown'),
        'Region': ip_info.get('region', 'Unknown'),
        'Postal Code': ip_info.get('postal', 'Unknown'),
        'Country': ip_info.get('country_name', 'Unknown'),
        'Latitude': ip_info.get('latitude', 'Unknown'),
        'Longitude': ip_info.get('longitude', 'Unknown'),
        
        'Timezone': ip_info.get('timezone', 'Unknown'),
        'ASN': ip_info.get('asn', 'Unknown'),
        'ISP/Org': ip_info.get('org', 'Unknown'),
        'Browser': f"{user_agent.browser.family} {user_agent.browser.version_string}",
        'OS': f"{user_agent.os.family} {user_agent.os.version_string}",
        'Device': user_agent.device.family,
        'User-Agent': user_agent_string,
        'Referrer': referrer
    }

    # saving log file
    log_line = "\n".join(f"{k}: {v}" for k, v in log_data.items()) + "\n" + "-"*50 + "\n"

    
    logging.info(log_line)

    # custom html/css page
    html_content = """
    <html>
    <head>
        <title>You Got Doxed!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                color: #333;
                text-align: center;
                margin-top: 50px;
            }
            h1 {
                color: red;
                font-size: 48px;
            }
            p {
                font-size: 24px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>You Got Doxed!</h1>
        <p>We've logged your information. Be cautious online!</p>
    </body>
    </html>
    """

    response = make_response(html_content)
    response.headers['Referrer-Policy'] = 'no-referrer'
    response.headers['Cache-Control'] = 'no-store'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
