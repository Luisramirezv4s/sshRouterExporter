# sshRouterExporter
A Python tool to connect to Cisco routers via SSH, retrieve interface status information, and export the results to **Excel (.xlsx)** or **SQL (.sql)** formats.  
This project uses **Paramiko** for SSH communication and **OpenPyXL** for Excel file generation.

---

# Features
- 🔑 SSH connection to Cisco routers using Paramiko.  
- 🌐 Executes `show ip interface brief` to retrieve interface details.  
- 📊 Export results to:
  - Excel workbook (`.xlsx`)
  - SQL script (`.sql`) for database import.  
- 🛠️ Simple CLI menu for choosing export formats.  

---

# Environment Setup
This work was carried out in a **virtualized network environment**:  
1. **VMware Fusion** was used as the virtualizer.  
2. **GNS3** (both client and server) was configured to provide a graphical network simulation.  

⚠️ Make sure your GNS3 client and server are properly configured to allow communication between the host machine and the virtualized devices.

---

# Requirements
- Python 3.8+  
- [VMware Fusion](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion)  
- [GNS3](https://www.gns3.com/software/download)

Install dependencies with:  
pip install paramiko openpyxl

---

# USAGE
1. Clone the repository

	git clone https://github.com/your-username/sshRouterExporter.git
	cd sshRouterExporter

2. Edit the script to configure your router’s IP, username, and password:

	router_ip = "192.168.56.129"
	username = "admin"
	password = "admin"

3. Run the script:

	python sshRouterExporter.py

4. Choose the export format when prompted:

	1 → Excel file (interface_status.xlsx)
	2 → SQL script (interface_status.sql)
	0 → Exit
   
---

# Note:
This project is intended for educational purposes (network automation and scripting practice).

MIT License.
Feel free to use and adapt this project for learning and research purposes.
  
