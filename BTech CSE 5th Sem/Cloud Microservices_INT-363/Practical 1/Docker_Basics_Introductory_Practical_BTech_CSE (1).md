# Docker Basics — Introductory Practical Lab

**Course:** Cloud / DevOps / Cloud Microservices  
**Programme:** B.Tech CSE, 3rd Year  
**Lab Type:** Introductory Hands-on Practical  
**Suggested Duration:** 2 Hours  
**Tools Required:** Docker Desktop, Command Prompt / PowerShell / Terminal, Internet connection

---

## 1. Aim

To understand the basic concepts of Docker and perform fundamental Docker operations such as checking the Docker installation, pulling images, creating and running containers, listing containers and images, viewing logs, executing commands inside a container, stopping and removing containers, and working with ports and volumes.

---

## 2. Learning Outcomes

After completing this practical, students will be able to:

1. Explain why Docker is used.
2. Differentiate between a Docker image and a Docker container.
3. Understand the basic Docker architecture.
4. Verify a Docker installation.
5. Download images from Docker Hub.
6. Create and run containers.
7. View running and stopped containers.
8. Stop, start, restart, and remove containers.
9. View container logs.
10. Execute commands inside a running container.
11. Map host ports to container ports.
12. Understand Docker volumes for persistent data.
13. Explain how Docker supports DevOps and microservices.

---

## 3. What is Docker?

Docker is a platform used to **build, package, distribute, and run applications inside lightweight isolated environments called containers**.

A container contains the application along with the libraries and dependencies required to run it.

```text
Application
    +
Libraries
    +
Dependencies
    ↓
Docker Image
    ↓
Docker Container
```

Docker helps solve the common problem:

> “It works on my machine, but it does not work on another machine.”

Because the application and its dependencies are packaged together, the same container can run consistently on a developer laptop, testing server, or cloud platform.

---

## 4. Why Do We Need Docker?

Suppose a developer creates a Python web application requiring:

- Python 3.12
- Flask
- NumPy
- Specific operating-system libraries

Without Docker, these dependencies must be installed manually on every machine. This can cause version mismatches, missing libraries, configuration differences, and deployment problems.

With Docker:

```text
Application + Dependencies
          ↓
      Docker Image
          ↓
   Run Anywhere Docker
      is Available
```

---

## 5. Virtual Machine vs Docker Container

| Feature | Virtual Machine | Docker Container |
|---|---|---|
| Virtualizes | Hardware | Operating-system environment |
| Guest OS | Required | No complete guest OS required |
| Size | Usually larger | Usually smaller |
| Startup | Slower | Faster |
| Resource usage | Higher | Lower |
| Portability | Good | Very high |
| Common use | Full OS isolation | Application deployment |

Virtual machines:

```text
Physical Hardware
       ↓
Host Operating System
       ↓
Hypervisor
   ├── VM 1 → Guest OS → Application
   ├── VM 2 → Guest OS → Application
   └── VM 3 → Guest OS → Application
```

Docker containers:

```text
Physical Hardware
       ↓
Host Operating System
       ↓
Docker Engine
   ├── Container 1 → Application
   ├── Container 2 → Application
   └── Container 3 → Application
```

> Containers are not simply “small virtual machines.” They share the host kernel while isolating application processes.

---

## 6. Important Docker Terminology

### 6.1 Docker Image

A Docker image is a **read-only template used to create containers**.

Examples: `ubuntu`, `nginx`, `mysql`, `python`, `node`.

Think of an image as a **blueprint**.

### 6.2 Docker Container

A container is a **running or created instance of a Docker image**.

```text
Image
  ↓
docker run
  ↓
Container
```

Analogy:

```text
Class  → Image
Object → Container
```

### 6.3 Docker Engine

Docker Engine is the software responsible for building and running containers.

```text
Docker CLI
    ↓
Docker Daemon
    ↓
Container Runtime
    ↓
Containers
```

### 6.4 Docker Client

The Docker client is the command-line interface used by the user.

Examples:

```bash
docker run
docker ps
docker images
docker pull
```

### 6.5 Docker Daemon

The Docker daemon is the background service that manages images, containers, networks, and volumes.

### 6.6 Docker Registry

A Docker registry stores and distributes Docker images. The most common public registry is **Docker Hub**.

```text
Docker Hub
    ↓
docker pull nginx
    ↓
Local Computer
    ↓
Docker Image
    ↓
Container
```

### 6.7 Dockerfile

A Dockerfile is a text file containing instructions used to build a Docker image.

```dockerfile
FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python", "app.py"]
```

Dockerfiles can be covered in detail in a later practical.

---

## 7. Basic Docker Architecture

```text
                USER
                 |
                 v
            Docker CLI
                 |
                 v
           Docker Daemon
          /      |       \
         /       |        \
     Images   Containers   Networks
        |
        v
   Docker Registry
   (Docker Hub)
```

Typical workflow:

```text
docker pull
    ↓
Download Image
    ↓
docker run
    ↓
Create Container
    ↓
Application Runs
```

---

## 8. Verify Docker Installation

Open **PowerShell**, **Command Prompt**, or **Terminal**.

### Command 1: Check Docker version

```bash
docker --version
```

**Explanation:** Displays the installed Docker CLI version.

Example output:

```text
Docker version 29.x.x, build ...
```

### Command 2: View detailed Docker information

```bash
docker info
```

**Explanation:** Displays details about the Docker client/server, containers, images, storage driver, OS, CPU, memory, runtime, and networking.

---

## 9. Search for an Image

### Command 3

```bash
docker search nginx
```

**Explanation:** Searches Docker Hub for images related to `nginx`.

---

## 10. Pull a Docker Image

### Command 4

```bash
docker pull ubuntu
```

**Explanation:** Downloads the Ubuntu image from the configured registry.

### Command 5: Pull a specific version

```bash
docker pull ubuntu:24.04
```

The text after `:` is called a **tag**.

```text
ubuntu:24.04
   |      |
 Image   Tag
```

---

## 11. List Docker Images

### Command 6

```bash
docker images
```

Alternative:

```bash
docker image ls
```

**Explanation:** Displays locally available Docker images.

Typical columns:

```text
REPOSITORY
TAG
IMAGE ID
CREATED
SIZE
```

---

## 12. Run Your First Container

### Command 7: Hello World

```bash
docker run hello-world
```

What happens:

```text
docker run hello-world
        ↓
Check local system for image
        ↓
If missing, pull image
        ↓
Create container
        ↓
Start container
        ↓
Run program
        ↓
Display output
        ↓
Container stops
```

---

## 13. Run an Ubuntu Container Interactively

### Command 8

```bash
docker run -it ubuntu bash
```

**Explanation:**

- `docker run` → creates and starts a container
- `-i` → interactive mode
- `-t` → provides a terminal
- `ubuntu` → image name
- `bash` → command executed inside the container

Inside the container, try:

```bash
pwd
ls
cat /etc/os-release
whoami
```

To leave:

```bash
exit
```

---

## 14. List Running Containers

### Command 9

```bash
docker ps
```

**Explanation:** Shows only containers that are currently running.

---

## 15. List All Containers

### Command 10

```bash
docker ps -a
```

**Explanation:** Shows running, stopped, and exited containers. `-a` means **all**.

---

## 16. Container ID and Container Name

Every container gets a unique **container ID** and a **name**.

Example:

```text
CONTAINER ID   IMAGE    STATUS        NAMES
abc123456789   ubuntu   Exited        clever_morse
```

Either can be used in commands:

```bash
docker start abc123456789
```

or:

```bash
docker start clever_morse
```

---

## 17. Create a Container with Your Own Name

### Command 11

```bash
docker run --name myubuntu -it ubuntu bash
```

**Explanation:** `--name myubuntu` assigns a meaningful name to the container.

---

## 18. Start a Stopped Container

### Command 12

```bash
docker start myubuntu
```

**Explanation:** Starts an already-created stopped container.

```text
docker run   → create + start
docker start → start an existing container
```

---

## 19. Stop a Running Container

### Command 13

```bash
docker stop myubuntu
```

**Explanation:** Requests the container to stop gracefully.

---

## 20. Restart a Container

### Command 14

```bash
docker restart myubuntu
```

**Explanation:** Stops and starts the container again.

---

## 21. Remove a Container

### Command 15

```bash
docker rm myubuntu
```

**Explanation:** Deletes a stopped container.

Force removal:

```bash
docker rm -f myubuntu
```

**Caution:** `-f` forcibly removes a running container.

---

## 22. Remove an Image

### Command 16

```bash
docker rmi ubuntu
```

Alternative:

```bash
docker image rm ubuntu
```

**Explanation:** Removes an image from the local Docker host.

---

## 23. Run a Container in Background Mode

### Command 17

```bash
docker run -d nginx
```

**Explanation:** `-d` means **detached mode**. The container runs in the background.

---

## 24. Port Mapping

### Command 18

```bash
docker run -d -p 8080:80 --name webserver nginx
```

Meaning:

```text
8080 : 80
  |     |
Host  Container
Port    Port
```

Request flow:

```text
Browser
   ↓
localhost:8080
   ↓
Host Port 8080
   ↓
Docker Port Mapping
   ↓
Container Port 80
   ↓
Nginx
```

Open:

```text
http://localhost:8080
```

---

## 25. View Container Logs

### Command 19

```bash
docker logs webserver
```

**Explanation:** Displays output produced by the application running inside the container.

Follow logs continuously:

```bash
docker logs -f webserver
```

Press `Ctrl + C` to stop following.

---

## 26. Execute a Command Inside a Running Container

### Command 20

```bash
docker exec webserver ls
```

**Explanation:** Runs `ls` inside the running container.

### Command 21: Open a shell

```bash
docker exec -it webserver sh
```

or, if Bash is available:

```bash
docker exec -it webserver bash
```

Difference:

```text
docker run  → creates a new container
docker exec → runs a command inside an existing running container
```

---

## 27. Inspect a Container

### Command 22

```bash
docker inspect webserver
```

**Explanation:** Displays detailed JSON information such as container ID, image, ports, state, mounts, environment variables, and network settings.

---

## 28. View Container Resource Usage

### Command 23

```bash
docker stats
```

**Explanation:** Displays live CPU, memory, network I/O, and block I/O usage.

Press `Ctrl + C` to exit.

---

## 29. Docker Volumes

Docker volumes provide **persistent storage**.

```text
Container
    |
    v
Docker Volume
    |
Persistent Data
```

### Command 24: Create a volume

```bash
docker volume create mydata
```

### Command 25: List volumes

```bash
docker volume ls
```

### Command 26: Inspect a volume

```bash
docker volume inspect mydata
```

### Command 27: Attach a volume

```bash
docker run -it --name volume-demo -v mydata:/data ubuntu bash
```

Meaning:

```text
mydata : /data
   |       |
Docker   Directory
Volume   in Container
```

Inside the container:

```bash
echo "Docker Lab Data" > /data/test.txt
```

---

## 30. Docker Networks

### Command 28

```bash
docker network ls
```

**Explanation:** Displays available Docker networks.

Common networks include:

- `bridge`
- `host`
- `none`

---

## 31. Docker Help

### Command 29

```bash
docker --help
```

For command-specific help:

```bash
docker run --help
```

```bash
docker ps --help
```

---

## 32. Important Docker Commands Summary

| Command | Purpose |
|---|---|
| `docker --version` | Check Docker version |
| `docker info` | Display Docker environment information |
| `docker search image-name` | Search for images |
| `docker pull image-name` | Download an image |
| `docker images` | List local images |
| `docker run image-name` | Create and start a container |
| `docker run -it ubuntu bash` | Run an interactive Ubuntu container |
| `docker run -d nginx` | Run a container in background |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker start container` | Start a stopped container |
| `docker stop container` | Stop a running container |
| `docker restart container` | Restart a container |
| `docker rm container` | Remove a container |
| `docker rmi image` | Remove an image |
| `docker logs container` | View container logs |
| `docker exec -it container sh` | Open shell inside a running container |
| `docker inspect container` | Show detailed container information |
| `docker stats` | Show live resource usage |
| `docker volume create name` | Create a volume |
| `docker volume ls` | List volumes |
| `docker network ls` | List networks |
| `docker --help` | View Docker help |

---

## 33. Important Differences Students Should Remember

### Image vs Container

```text
IMAGE
Read-only template
       ↓
docker run
       ↓
CONTAINER
Running/created instance
```

### `docker run` vs `docker start`

```text
docker run
Image → Create Container → Start Container
```

```text
docker start
Existing Stopped Container → Start Container
```

### `docker ps` vs `docker ps -a`

```text
docker ps
→ only running containers
```

```text
docker ps -a
→ running + stopped containers
```

---

## 34. Docker and DevOps

Docker supports DevOps through:

- Consistent environments
- Faster deployment
- Application portability
- CI/CD pipelines
- Automated testing
- Infrastructure consistency
- Microservices
- Cloud-native deployment

Typical workflow:

```text
Developer
    ↓
Source Code
    ↓
Git
    ↓
CI Pipeline
    ↓
Build Docker Image
    ↓
Test Container
    ↓
Push Image to Registry
    ↓
Deploy Container
```

---

## 35. Docker and Microservices

An application can be divided into independent services:

```text
E-Commerce Application
        |
        +-- User Service
        +-- Product Service
        +-- Cart Service
        +-- Order Service
        +-- Payment Service
```

Each can be packaged separately:

```text
User Service     → Docker Container
Product Service  → Docker Container
Order Service    → Docker Container
Payment Service  → Docker Container
```

Benefits include independent deployment, scaling, portability, and isolation.

---

## 36. Mini Practical Activity

### Task 1: Verify Docker

```bash
docker --version
docker info
```

### Task 2: Pull Ubuntu

```bash
docker pull ubuntu
```

### Task 3: Check Images

```bash
docker images
```

### Task 4: Run Ubuntu

```bash
docker run -it --name student-ubuntu ubuntu bash
```

Inside:

```bash
cat /etc/os-release
pwd
ls
```

Exit:

```bash
exit
```

### Task 5: Check Container Status

```bash
docker ps
docker ps -a
```

### Task 6: Run Nginx Web Server

```bash
docker run -d -p 8080:80 --name student-web nginx
```

Check:

```bash
docker ps
```

Open:

```text
http://localhost:8080
```

### Task 7: View Logs

```bash
docker logs student-web
```

### Task 8: Enter Running Container

```bash
docker exec -it student-web sh
```

### Task 9: Stop and Remove Containers

```bash
docker stop student-web
docker rm student-web
docker rm student-ubuntu
```

---

## 37. Gamified Learning Activity — Container Commander

Students work individually or in pairs.

| Mission | Task | Points |
|---|---|---:|
| Mission 1 | Verify Docker installation | 10 |
| Mission 2 | Pull an image | 10 |
| Mission 3 | Run an interactive Ubuntu container | 15 |
| Mission 4 | Identify image ID and container ID | 10 |
| Mission 5 | Run Nginx in detached mode | 15 |
| Mission 6 | Access Nginx using port mapping | 20 |
| Mission 7 | View container logs | 10 |
| Mission 8 | Enter a running container using `docker exec` | 10 |

**Maximum Score: 100**

### Bonus Challenge

```bash
docker run -d -p 8081:80 --name web2 nginx
```

Then access:

```text
http://localhost:8081
```

**Bonus:** 10 points

---

## 38. Viva Questions

1. What is Docker?
2. What is a Docker image?
3. What is a Docker container?
4. What is Docker Hub?
5. What is the Docker daemon?
6. What is the difference between an image and a container?
7. What does `docker pull` do?
8. What does `docker run` do?
9. What is the difference between `docker ps` and `docker ps -a`?
10. What is detached mode?
11. What does `-p 8080:80` mean?
12. What is a Docker volume?
13. Why are volumes important?
14. What does `docker exec` do?
15. What does `docker logs` show?
16. What is the purpose of a Dockerfile?
17. How does Docker help DevOps?
18. How does Docker support microservices?
19. What is the difference between Docker and a virtual machine?
20. What is a Docker registry?

---

## 39. Student Submission

Students should submit screenshots of:

1. `docker --version`
2. `docker info`
3. `docker images`
4. `docker run hello-world`
5. Interactive Ubuntu container
6. `docker ps -a`
7. Nginx container running
8. Nginx page opened at `localhost:8080`
9. `docker logs student-web`
10. `docker exec` command output

---

## 40. Precautions

1. Ensure Docker Desktop is running before executing Docker commands.
2. Use unique container names.
3. Check `docker ps -a` before creating duplicate containers.
4. Do not expose unnecessary ports.
5. Do not remove important volumes without checking their contents.
6. Use official or trusted Docker images for classroom practice.
7. Stop unnecessary containers after the practical.
8. Use `docker rm -f` carefully.
9. Do not store passwords or secret keys directly in Docker images.
10. Use `docker --help` when unsure about command syntax.

---

## 41. Quick Revision

```text
Docker Image
    ↓
docker run
    ↓
Container
    ↓
docker ps
    ↓
docker logs / docker exec
    ↓
docker stop
    ↓
docker rm
```

For a web application:

```text
Docker Hub
    ↓
docker pull nginx
    ↓
Nginx Image
    ↓
docker run -d -p 8080:80 nginx
    ↓
Nginx Container
    ↓
Browser → localhost:8080
```

---

## 42. Key Takeaway

> **Docker packages applications and their dependencies into portable containers, allowing applications to run consistently across development, testing, production, and cloud environments.**

The five most important beginner commands are:

```bash
docker pull
docker run
docker ps
docker stop
docker rm
```

Before moving to Dockerfiles, Docker Compose, and Kubernetes, students should understand the lifecycle:

```text
Pull Image → Run Container → Inspect → Use → Stop → Remove
```
