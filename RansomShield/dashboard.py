import streamlit as st
import psutil
import pandas as pd
import plotly.express as px
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import os
import re

st.set_page_config(
    page_title="RansomShield Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Refresh every 2 seconds
st_autorefresh(interval=2000, key="refresh")


st.markdown("""
<style>

html, body, [class*="css"]{
    background-color:#0d1117;
    color:white;
}

.big-title{
    font-size:48px;
    font-weight:bold;
    color:#00ff99;
}

.section{
    background:#161b22;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
}

.alert{
    background:#ff0000;
    color:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    animation: blink 1s infinite;
}

@keyframes blink{
0%{opacity:1;}
50%{opacity:0.3;}
100%{opacity:1;}
}

</style>
""", unsafe_allow_html=True)


st.markdown(
'<p class="big-title">🛡️ RansomShield Security Dashboard</p>',
unsafe_allow_html=True
)



if os.path.exists("evidence.txt"):

    with open("evidence.txt","r") as f:
        evidence=f.read()

else:
    evidence=""


if os.path.exists("response_log.txt"):

    with open("response_log.txt","r") as f:
        response=f.read()

else:
    response=""


alert_count=evidence.count("RANSOMWARE ALERT")


matches = re.findall(r"Target File\s*:\s*(.*)", evidence)

last_file = os.path.basename(matches[-1]) if matches else "No alerts"

cpu=psutil.cpu_percent()

ram=psutil.virtual_memory().percent

processes=len(psutil.pids())

current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("🚨 Total Alerts",alert_count)

with col2:
    st.metric("💻 Running Processes",processes)

with col3:
    st.metric("📄 Last Target",last_file)

with col4:
    st.metric("🕒 Current Time",current_time)

st.divider()

if alert_count>0:

    st.markdown(
    """
    <div class="alert">
    🚨 RANSOMWARE DETECTED 🚨
    </div>
    """,
    unsafe_allow_html=True
    )

else:

    st.success("🟢 System Secure")

st.divider()

left,right=st.columns(2)

with left:

    st.subheader("🖥 CPU Usage")

    st.progress(int(cpu))

    st.write(f"Current CPU Usage : {cpu}%")

    st.subheader("💾 RAM Usage")

    st.progress(int(ram))

    st.write(f"Current RAM Usage : {ram}%")

with right:

    safe=max(processes-alert_count,0)

    chart_df=pd.DataFrame({
        "Status":["Safe","Alerts"],
        "Count":[safe,alert_count]
    })

    fig=px.pie(
        chart_df,
        names="Status",
        values="Count",
        hole=0.5,
        title="System Status Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

st.divider()

left,right=st.columns(2)

with left:

    st.subheader("📑 Evidence Log")

    st.text_area(
        "",
        evidence,
        height=350
    )

with right:

    st.subheader("⚡ Response Log")

    st.text_area(
        "",
        response,
        height=350
    )

    st.divider()

st.subheader("🖥 Live System Monitor")

disk = psutil.disk_usage("/")

col1, col2 = st.columns(2)

with col1:

    st.info(f"""
Operating System : Windows

CPU Cores : {psutil.cpu_count()}

Logical Processors : {psutil.cpu_count(logical=True)}

Boot Time :
{datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")}
""")

with col2:

    st.info(f"""
Disk Usage : {disk.percent} %

Available Memory :
{round(psutil.virtual_memory().available/1024/1024/1024,2)} GB

Total Memory :
{round(psutil.virtual_memory().total/1024/1024/1024,2)} GB

Running Processes :
{len(psutil.pids())}
""")

st.divider()

st.subheader("📌 RansomShield Features")

st.success("✔ Real-Time File Monitoring")
st.success("✔ Rapid File Modification Detection")
st.success("✔ Ransomware Alert Generation")
st.success("✔ Running Process Collection")
st.success("✔ Forensic Evidence Collection")
st.success("✔ Incident Response Logging")
st.success("✔ Desktop Notification")
st.success("✔ Dashboard Monitoring")

st.divider()

st.subheader("🎯 Detection Logic")

st.code("""
1. Monitor selected folder continuously
2. Detect file modifications
3. Count modifications within 10 seconds
4. If modifications >= 10
5. Generate ransomware alert
6. Save forensic evidence
7. Save running processes
8. Notify user
9. Display results on dashboard
""")

st.divider()

st.subheader("📊 System Health")

health = max(100 - alert_count * 10, 0)

st.progress(health/100)

if health >= 80:
    st.success(f"System Health : {health}%")

elif health >= 50:
    st.warning(f"System Health : {health}%")

else:
    st.error(f"System Health : {health}%")

st.divider()

st.caption(
"""
🛡️ RansomShield

Cybersecurity Minor Project

Technology Stack:
Python | Watchdog | Psutil | Plyer | Streamlit | Plotly

Developed by Het Patel
"""
)