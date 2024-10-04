# flask-azure-demo
This is a demo repo for the python application

# azure portal
NOTE: you have to modify the inbound rule of 8080

# set up for linux
`sudo apt update && sudo apt upgrade -y`

## backend
- git clone <repo-url>
- git checkout <branch-name>
`cd flask-azure-demo`
`cd backend`
`sudo apt install python3`
`sudo apt install python3-pip`
`sudo apt install python3-venv`

`python3 -m venv .venv`

`. .venv/bin/activate`

`flask run -h 0.0.0.0 -p 8080`

# Frontend
`sudo apt install apache2`
`cd /var/www/html`
`git clone <repo-url>`
`git checkout <branch-name>`
`cd frontend`
NOTE: modify the action attribute in the index.html page `http://<public-url>:8080/add`

