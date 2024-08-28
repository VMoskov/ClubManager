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