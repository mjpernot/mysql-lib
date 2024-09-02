# MySQL Configuration file
# Classification (U)
# Unclassified until filled in.
user = "USER"
japd = 'PSWORD'
# Replication user information
rep_user = "REP_USER"
rep_japd = 'REP_PSWORD'
# MySQL DB host information
# DO NOT USE 127.0.0.1 or localhost for the master, use actual IP.
host = "HOST_IP"
name = "HOST_NAME"
# MySQL database server id - unique to each database
sid = SERVER_ID
# MySQL Definition configuration file
extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
# Server running OS
serv_os = "Linux"
# MySQL database port (default is 3306)
port = 3306
# MySQL configuration settings
cfg_file = "/etc/my.cnf"
# SSL Configuration settings
# If not set will connect to MySQL without using SSL connections.
# File containing the SSL certificate authority.
# Example: ssl_client_ca = "/opt/mysql/certs/ca.pem"
ssl_client_ca = None
# Path to the directory containing CA certificates.
# Example: ssl_ca_path = "/opt/mysql/certs"
ssl_ca_path = None
# File containing the SSL key.
# Example:  ssl_client_key = "/opt/mysql/certs/client-key.pem"
ssl_client_key = None
# File containing the SSL certificate file.
# Example: ssl_client_cert = "/opt/mysql/certs/client-cert.pem"
ssl_client_cert = None
# Type of SSL connection mode being requested.
# Mode types:  DISABLED|PREFERRED|REQUIRED|VERIFY_CA|VERIFY_IDENTITY
# Example: ssl_mode = REQUIRED
ssl_mode = "PREFERRED"
# SSL Client Flag Value.
# If not set, will take the default value of mysql.connector.ClientFlag.SSL
#   (typically 2048).
ssl_client_flag = None
# SSL Disabled
# Will disable SSL for connection if set to True.
ssl_disabled = False
# SSL Verify Identity
# Will verify the hostname of the destination with the certifcation.
ssl_verify_id = False
# SSL Verify Certification
# Will validate the CA certification.
ssl_verify_cert = False
# TLS Version settings
# TLS Version(s) allowed to be used to connect to MySQL.
# If an empty list, then will use the default TLS version provided by the MySQL
#   server.
# Example: tls_versions = ["TLSv1.1", "TLSv1.2"]
tls_versions = []
