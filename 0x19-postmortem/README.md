Postmortem: Web Server Outage
Issue Summary:
•	Duration: 1 hour (May 11, 2024, 08:00 AM - 09:00 AM UTC)
•	Impact: Website downtime, affecting 100% of users.
•	Root Cause: Configuration error in the web server.
Timeline:
•	08:00 AM UTC: Issue detected through monitoring alert.
•	08:02 AM UTC: Investigated web server logs for errors.
•	08:15 AM UTC: Assumed database connectivity issue, escalated to the database team.
•	08:30 AM UTC: Database team found no issues, escalated back to web server team.
•	08:45 AM UTC: Discovered misconfigured firewall settings.
•	09:00 AM UTC: Issue resolved by correcting firewall settings.
Root Cause:
•	Misconfigured firewall settings blocked incoming traffic to the web server.
Resolution:
•	Resolution: Firewall settings were corrected to allow incoming traffic on the required ports.
Corrective and Preventative Measures:
•	Improvements/Fixes:
•	Implement automated monitoring of firewall settings.
•	Regularly review and update firewall configurations.
•	Tasks:
1.	Implement automated firewall configuration monitoring.
2.	Conduct regular firewall configuration audits.
3.	Document firewall configuration best practices.

