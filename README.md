# botnet infrastructure scalable to up to 300 simulated bot clients where each bot is simulated using a docker container 
# bots are grouped behind gateways, each gateway simulating a unique IP, enabling scalable and diverse traffic generation up to 300 bots.

# contents : 
- 'server.py' local http test server with rate limiting 
- 'bot.py' bot client that generates traffic
- 'Dockerfile.server' docker image definition for the server
- 'Dockerfile.bot' Docker image definition for bot clients
- 'docker-compose.yml' Multi-container orchestration and scaling
- gateway/
├── 'Dockerfile' Docker image definition for gateway
└── 'default.conf' Gateway configuration (proxy & headers)

# start the infrastructure : 
docker compose up --build
docker compose up -d

# Check running containers : 
docker ps

# View logs : 
docker compose logs
docker compose logs server
docker compose logs gateway1

# Verify fake IPs inside a gateway :
docker exec -it <gateway_container_name> env | grep FAKE_IP

# stop the infrastructure : 
docker compose down

# Clean containers + networks :
docker compose down -v
