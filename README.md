# GhostRecon
GhostRecon – A Passive Reconnaissance Tool leveraging the Wayback Machine to gather historical URLs of a target domain for security research and analysis.


📦 How to Run GhostRecon
Follow these steps to get GhostRecon up and running on your machine:

1️⃣ **Clone the Repository**

git clone https://github.com/yourusername/GhostRecon.git
cd GhostRecon

2️⃣ **Install Requirements**
GhostRecon only needs one Python library: **requests**.

_Install it using pip:_
pip install requests


3️⃣ **Run the Tool**

Now you're ready to run it! Just execute the Python script:

**python ghostrecon.py**


4️⃣ **Enter the Target Domain**
When prompted, input the domain you want to gather archived URLs for (without http:// or https://):

🔍 Enter the target domain (e.g. example.com): **maveera.rf.gd**


5️⃣ **View the Output**
You'll see a list of historical URLs printed in the terminal.

A text file named **maveera.rf.gd_wayback_urls.txt** (or your domain name) will be created with all the URLs saved inside.

**✅ Done!**

You've just passively gathered recon data from the Wayback Machine using GhostRecon.
