# REPORT-SERVICE

Service for sending email reports about servers to responsible persons

## Startup

Clone repository
```sh
git clone https://github.com/holodnyisiemens/report-service.git
```

```sh
cd report-service
```

Configure .env using template
```sh
cp app/.env.template app/.env
```

```sh
vi app/.env
```

Start service
```sh
docker compose up -d --build
```

## Examples of using

Get all responsible:
```sh
curl -Lu username:password http://localhost:8000/api/v1/responsible
```

Get all hosts:
```sh
curl -Lu username:password http://localhost:8000/api/v1/hosts
```

Get hosts of a responsible person without email message:
```sh
curl -Lu username:password http://localhost:8000/api/v1/hosts/RESPONSIBLE_NAME
```

Get hosts of a responsible person with email message:
```sh
curl -Lu username:password http://localhost:8000/api/v1/hosts/RESPONSIBLE_NAME?email_notify=1
```
Email address is composed of RESPONSIBLE_NAME and EMAIL__RECIEVERS_DOMAIN from .env

With Jenkins:
1. Configure Jenkins credentials "Username with password" for API access
2. Configure Jenkinsfile using template
3. Create a "Pipeline" job
4. Insert Jenkinsfile into the "Pipeline script" field
5. Build it
