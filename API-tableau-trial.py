import tableauserverclient as TSC

# Define Tableau Server information
server_url = 'https://your-tableau-server.com'
api_version = '3.6'

# Define authentication information
username = 'your_username'
password = 'your_password'

# Connect to Tableau Server
tableau_auth = TSC.TableauAuth(username, password)
server = TSC.Server(server_url, api_version)
server.auth.sign_in(tableau_auth)

# Get list of projects
all_projects, pagination_item = server.projects.get()
for project in all_projects:
    print(project.name)

# Sign out of Tableau Server
server.auth.sign_out()
