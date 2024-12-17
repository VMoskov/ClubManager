# ClubManager
This is a simple club manager application that allows you to manage clubs and their members and their coach. It is built using Flask and SQLAlchemy.

## Installation
1. Clone the repository
```bash
git clone https://github.com/VMoskov/ClubManager.git
```
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Ensure that you have a Docker container running with a PostgreSQL database
```bash
# position yourself into the database folder
cd ClubManager/database
# build the docker container
docker-compose up
```
4. Run the application
```bash
# position yourself back into the ClubManager (root) folder
cd ..
# run the application
bash run.sh
```
5. Open your browser and navigate to `http://localhost:5000/` or test the API using Postman or any other API testing tool.
   
## Currently supported user roles:
- Admin
- User
  
## Example users:
- Admin: 
  - username: admin
  - password: admin
  - email: admin@admin.com
  - first name: Admin
  - last name: Admin
  - birth date: 26/02/2003

- User:
  - username: user
  - password: user
  - email: user@user.com
  - first name: User
  - last name: User
  - birth date: 26/02/2003

## Authorisation
### TODO: Login endpoint which returns a JWT token for authorisation
The application uses JWT tokens for authorisation. To access the API, you need to provide a valid JWT token in the header of your request. You can obtain a token by using www.jwt.io with the following payload:
```json
{
    "sub": "<user_id>",
    "username": "<username>",
    "password": "<password>",
    "roles": "<role>"
}
```
Current placeholder secret key is "your secret jwt key". You can change it in the `config.py` file or in the `run.sh` file.
### Examples:
```json
{
    "sub": "1",
    "email": "admin@admin.com",
    "password": "admin",
    "role": "admin"
}
```
The above payload will return a JWT token that you can use to access the API as an admin: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJhZG1pbkBhZG1pbi5jb20iLCJwYXNzd29yZCI6ImFkbWluIiwicm9sZSI6ImFkbWluIn0.SF60_BhOvGHjX7tHIPxrFuZ0ScrL11vx-jrW7WthEU4`
```json
{
    "sub": "2",
    "email": "user@user.com",
    "password": "user",
    "role": "user"
}
```
The above payload will return a JWT token that you can use to access the API as a user: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ1c2VyQHVzZXIuY29tIiwicGFzc3dvcmQiOiJ1c2VyIiwicm9sZSI6InVzZXIifQ.svQSZTXWoF3RvNHAIDEBPtftKlOsbD6IpOcbp_NVz8U`

## API Documentation
The API documentation is available at `http://localhost:5000/apidocs` and it is generated using Swagger UI.