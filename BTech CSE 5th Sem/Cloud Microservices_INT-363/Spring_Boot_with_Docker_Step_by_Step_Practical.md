# INT363 — CLOUD MICROSERVICES

# Practical: Spring Boot with Docker

## 1. Aim

To create a simple Spring Boot web application, test it on the local computer, package it as a JAR file, create a Docker image for the application, and run the Spring Boot application inside a Docker container.

---

# 2. Introduction to Spring Boot

## What is Spring Boot?

**Spring Boot** is a Java-based framework used to develop stand-alone web applications, REST APIs, and microservices.

Normally, creating a Java web application requires several configurations. Spring Boot simplifies these configurations and allows us to create and run a web application quickly.

A Spring Boot application can contain its own web server. Therefore, we do not have to separately install Tomcat for this practical.

A simple workflow is:

```text
Write Java Code
       ↓
Spring Boot Application
       ↓
Create JAR File
       ↓
Create Docker Image
       ↓
Run Docker Container
       ↓
Access Application from Browser
```

In this practical, we will create only one simple REST endpoint:

```text
/hello
```

It will display:

```text
Hello from Spring Boot with Docker!
```

---

# 3. What is Docker?

Docker is used to package an application together with the environment required to run it.

Instead of saying:

> "The application works on my computer."

Docker helps us package the application so that it can run in a similar environment on another computer.

For this practical:

```text
Spring Boot Application
        ↓
JAR File
        ↓
Docker Image
        ↓
Docker Container
```

### Docker Image

A Docker image is the packaged template of our application.

### Docker Container

A Docker container is a running instance of a Docker image.

---

# 4. Software Required

For this practical, we need:

1. Java JDK
2. Docker Desktop
3. Visual Studio Code
4. Web browser
5. Internet connection during initial project creation/build

We will use the **Maven Wrapper supplied with the Spring Boot project**, so students do not need to separately configure Maven for this experiment.

---

# PART A — VERIFY JAVA AND DOCKER

# Step 1: Check Java

Open **PowerShell**.

Run:

```powershell
java -version
```

You should see a Java version.

For example:

```text
java version "21"
```

Also run:

```powershell
javac -version
```

Example:

```text
javac 21
```

### Explanation

`java` is required to run Java applications.

`javac` is the Java compiler.

If both commands work, Java is properly available.

---

# Step 2: Check Docker

First, start **Docker Desktop**.

Wait until Docker Desktop indicates that the Docker Engine is running.

Now open PowerShell and execute:

```powershell
docker --version
```

Then execute:

```powershell
docker info
```

### Explanation

`docker --version` checks whether Docker is installed.

`docker info` checks whether Docker Desktop and the Docker Engine are actually running.

Do not continue until `docker info` works successfully.

---

# PART B — CREATE THE SPRING BOOT PROJECT

# Step 3: Open Spring Initializr

Open your browser and go to:

```text
https://start.spring.io
```

Spring Initializr is used to generate a basic Spring Boot project.

---

# Step 4: Configure the Project

Use the following settings.

| Option | Select/Enter |
|---|---|
| Project | Maven |
| Language | Java |
| Spring Boot | Keep the stable version displayed |
| Group | com.example |
| Artifact | demo |
| Name | demo |
| Description | Spring Boot with Docker |
| Package Name | com.example.demo |
| Packaging | Jar |
| Java | 21 |

### Very Important

Select:

```text
Project = Maven
```

Do **not** select Gradle.

We are using Maven in this practical.

---

# Step 5: Add Spring Web

Click:

```text
ADD DEPENDENCIES
```

Search for:

```text
Spring Web
```

Select:

```text
Spring Web
```

### Why are we adding Spring Web?

Spring Web allows us to create web applications and REST endpoints such as:

```text
/hello
```

---

# Step 6: Generate the Project

Click:

```text
GENERATE
```

A ZIP file will be downloaded.

The file should normally be:

```text
demo.zip
```

---

# Step 7: Extract the ZIP File

Go to the Downloads folder.

Right-click:

```text
demo.zip
```

Select:

```text
Extract All
```

After extraction, open the extracted:

```text
demo
```

folder.

---

# Step 8: VERY IMPORTANT — Check the Project Files

Before writing any program, verify the files.

Inside the **demo** folder you should see something similar to:

```text
demo
│
├── .mvn
├── src
├── .gitignore
├── mvnw
├── mvnw.cmd
└── pom.xml
```

### Important explanation

These names can be confusing.

#### `pom.xml`

This is the Maven project configuration file.

It contains information about:

- project
- dependencies
- Java version
- Spring Boot
- build process

The file is:

```text
pom.xml
```

NOT:

```text
.pom
```

---

### `.mvn`

`.mvn` is a **folder**.

Because it begins with a dot, Windows or VS Code may sometimes make it less noticeable.

---

### `mvnw`

This is the Maven Wrapper for:

```text
Linux / macOS
```

---

### `mvnw.cmd`

This is the Maven Wrapper for:

```text
Windows
```

Therefore, throughout this Windows practical we will use:

```powershell
.\mvnw.cmd
```

---

### What is `mvn` then?

`mvn` is different.

```powershell
mvn
```

is the command used when Maven has been separately installed on the computer.

We do **not** need to use it in this practical.

We will use:

```powershell
.\mvnw.cmd
```

instead.

---

# STOP HERE IF `pom.xml` IS MISSING

If the extracted project does **not** contain:

```text
pom.xml
```

do not continue with the practical.

Go back to:

```text
https://start.spring.io
```

and make sure:

```text
Project = Maven
```

Then generate the project again.

A Spring Boot Maven project must contain its Maven project configuration.

---

# Step 9: Verify the Files from PowerShell

Open the `demo` folder.

Click in the address bar of File Explorer.

Type:

```text
powershell
```

Press Enter.

PowerShell should open directly inside your `demo` folder.

Run:

```powershell
dir
```

You should see:

```text
mvnw
mvnw.cmd
pom.xml
src
```

To also see hidden files/folders, run:

```powershell
dir -Force
```

You should now also see:

```text
.mvn
```

### Check individually

Run:

```powershell
Test-Path .\pom.xml
```

Expected:

```text
True
```

Run:

```powershell
Test-Path .\mvnw.cmd
```

Expected:

```text
True
```

Only continue when these return `True`.

---

# PART C — OPEN THE PROJECT IN VS CODE

# Step 10: Open the Correct Folder

Start Visual Studio Code.

Select:

```text
File
→ Open Folder
```

Select the extracted:

```text
demo
```

folder.

### Important

Open the folder that directly contains:

```text
pom.xml
```

Do not open only:

```text
src
```

and do not open the entire:

```text
Downloads
```

folder.

Your VS Code Explorer should approximately show:

```text
DEMO
│
├── .mvn
├── src
├── mvnw
├── mvnw.cmd
└── pom.xml
```

---

# PART D — UNDERSTAND THE GENERATED SPRING BOOT APPLICATION

# Step 11: Locate `DemoApplication.java`

Expand:

```text
src
  → main
     → java
        → com
           → example
              → demo
```

You should see:

```text
DemoApplication.java
```

Notice that we deliberately selected:

```text
Artifact = demo
Package = com.example.demo
```

That is why the generated file is called:

```text
DemoApplication.java
```

We will use this same name throughout the practical.

---

# Step 12: Open `DemoApplication.java`

The generated code will look similar to:

```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

You do **not** need to change this file.

### Explanation

The following:

```java
@SpringBootApplication
```

marks this as the main Spring Boot application.

The following:

```java
public static void main(String[] args)
```

is where the Java program starts.

And:

```java
SpringApplication.run(DemoApplication.class, args);
```

starts Spring Boot.

---

# PART E — CREATE A SIMPLE REST API

# Step 13: Create `HelloController.java`

In VS Code, right-click the package:

```text
com.example.demo
```

Select:

```text
New File
```

Enter:

```text
HelloController.java
```

The two Java files should now be in the same location:

```text
com.example.demo
│
├── DemoApplication.java
└── HelloController.java
```

---

# Step 14: Write the Controller

Open:

```text
HelloController.java
```

Enter:

```java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello from Spring Boot with Docker!";
    }
}
```

Save the file.

---

# Step 15: Understand the Program

## `@RestController`

```java
@RestController
```

tells Spring Boot that this class will handle web requests.

---

## `@GetMapping("/hello")`

```java
@GetMapping("/hello")
```

means:

> If somebody sends a GET request to `/hello`, execute the method below it.

Therefore, when we enter:

```text
http://localhost:8080/hello
```

the following method executes:

```java
public String hello()
```

and returns:

```text
Hello from Spring Boot with Docker!
```

---

# PART F — RUN SPRING BOOT WITHOUT DOCKER

It is important to first make sure that the Spring Boot application works normally.

Only after that will we use Docker.

---

# Step 16: Open the Terminal

In VS Code select:

```text
Terminal
→ New Terminal
```

Make sure the terminal is inside the folder containing:

```text
pom.xml
```

Run:

```powershell
dir
```

You should see:

```text
pom.xml
mvnw
mvnw.cmd
src
```

---

# Step 17: Run Spring Boot

On Windows execute:

```powershell
.\mvnw.cmd spring-boot:run
```

### What does this command mean?

```text
.\mvnw.cmd
```

means:

> Use the Maven Wrapper included with this project.

And:

```text
spring-boot:run
```

means:

> Start the Spring Boot application.

The first execution may download required Maven dependencies.

---

# Step 18: Wait for Spring Boot to Start

After a successful startup, the terminal should eventually display a message similar to:

```text
Started DemoApplication
```

You may also see:

```text
Tomcat started on port 8080
```

At this point the application is running.

Do not close this terminal.

---

# Step 19: Test the Application

Open your browser.

Enter:

```text
http://localhost:8080/hello
```

Expected result:

```text
Hello from Spring Boot with Docker!
```

If you see this message, your Spring Boot application is working correctly.

### Important

Use:

```text
localhost:8080
```

for this practical.

Do not use port `8081` if another application such as Jenkins is already using it.

---

# Step 20: Stop Spring Boot

Return to the terminal.

Press:

```text
Ctrl + C
```

The Spring Boot application stops.

We stop it before continuing to Docker.

---

# PART G — CREATE THE JAR FILE

Docker will run our packaged Spring Boot application.

Therefore, the next step is to create a JAR file.

---

# Step 21: Build the Spring Boot Application

In the project terminal run:

```powershell
.\mvnw.cmd clean package -DskipTests
```

Wait until Maven displays:

```text
BUILD SUCCESS
```

### Explanation

`clean`

removes old build files.

`package`

compiles the Java application and creates a JAR file.

`-DskipTests`

skips tests for this simple classroom practical.

---

# Step 22: Check the JAR File

After a successful build, a new folder will appear:

```text
target
```

Run:

```powershell
dir target
```

You should see a file similar to:

```text
demo-0.0.1-SNAPSHOT.jar
```

Therefore:

```text
Java Source Code
      ↓
Maven Build
      ↓
JAR File
```

---

# PART H — CREATE THE DOCKERFILE

# Step 23: Create a Dockerfile

In the root `demo` folder, create a new file:

```text
Dockerfile
```

### Very Important

The filename must be exactly:

```text
Dockerfile
```

Do NOT create:

```text
Dockerfile.txt
```

Your project should now look approximately like:

```text
demo
│
├── .mvn
├── src
├── target
├── Dockerfile
├── mvnw
├── mvnw.cmd
└── pom.xml
```

---

# Step 24: Write the Dockerfile

Enter the following:

```dockerfile
FROM eclipse-temurin:21-jre

WORKDIR /app

COPY target/*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]
```

Save the file.

---

# PART I — UNDERSTAND THE DOCKERFILE

# Step 25: Understand `FROM`

```dockerfile
FROM eclipse-temurin:21-jre
```

Our Spring Boot application requires Java.

This line tells Docker to start with an image containing a Java 21 runtime.

---

# Step 26: Understand `WORKDIR`

```dockerfile
WORKDIR /app
```

This creates/uses:

```text
/app
```

as the working directory inside the Docker image.

---

# Step 27: Understand `COPY`

```dockerfile
COPY target/*.jar app.jar
```

This takes the JAR file created inside:

```text
target
```

and copies it into the Docker image.

Inside the image, the JAR will simply be called:

```text
app.jar
```

---

# Step 28: Understand `EXPOSE`

```dockerfile
EXPOSE 8080
```

Our Spring Boot application listens on port:

```text
8080
```

inside the container.

---

# Step 29: Understand `ENTRYPOINT`

```dockerfile
ENTRYPOINT ["java", "-jar", "app.jar"]
```

This tells Docker what command to execute when the container starts.

It is effectively executing:

```text
java -jar app.jar
```

---

# PART J — BUILD THE DOCKER IMAGE

# Step 30: Check Docker Desktop Again

Make sure Docker Desktop is running.

Execute:

```powershell
docker info
```

Continue only if Docker responds successfully.

---

# Step 31: Build the Docker Image

Make sure the terminal is still inside the `demo` directory.

Run:

```powershell
docker build -t springboot-docker-demo .
```

### Very Important

Do not forget the final:

```text
.
```

The complete command is:

```powershell
docker build -t springboot-docker-demo .
```

---

# Step 32: Understand the Command

```text
docker build
```

means:

> Build a Docker image.

```text
-t
```

means:

> Give the image a name.

Our image name is:

```text
springboot-docker-demo
```

The final:

```text
.
```

means:

> Use the current folder containing the Dockerfile.

---

# Step 33: Verify the Image

Run:

```powershell
docker images
```

You should see an image named:

```text
springboot-docker-demo
```

At this stage:

```text
Spring Boot Source Code
         ↓
      JAR File
         ↓
     Dockerfile
         ↓
     Docker Image
```

---

# PART K — RUN THE SPRING BOOT APPLICATION IN DOCKER

# Step 34: Create and Start the Container

Run:

```powershell
docker run -d --name springboot-container -p 9090:8080 springboot-docker-demo
```

Docker should return a long container ID.

---

# Step 35: Understand the Command

The command:

```powershell
docker run -d --name springboot-container -p 9090:8080 springboot-docker-demo
```

contains several parts.

### `docker run`

Creates and starts a container.

### `-d`

Runs the container in the background.

### `--name springboot-container`

Gives our container the name:

```text
springboot-container
```

### `-p 9090:8080`

Maps:

```text
Host Port        Container Port
9090       →     8080
```

Therefore:

```text
Browser
   ↓
localhost:9090
   ↓
Docker
   ↓
Container port 8080
   ↓
Spring Boot
```

### `springboot-docker-demo`

This is the Docker image from which the container is created.

---

# Step 36: Check the Running Container

Run:

```powershell
docker ps
```

You should see:

```text
springboot-container
```

Its status should show that it is running.

---

# PART L — TEST SPRING BOOT INSIDE DOCKER

# Step 37: Test from the Browser

Open:

```text
http://localhost:9090/hello
```

Expected output:

```text
Hello from Spring Boot with Docker!
```

Congratulations.

The same Spring Boot application is now running inside a Docker container.

---

# Step 38: Understand What Just Happened

Earlier we tested:

```text
http://localhost:8080/hello
```

That was Spring Boot running directly on our computer.

Now we are testing:

```text
http://localhost:9090/hello
```

This request follows:

```text
Browser
   ↓
localhost:9090
   ↓
Docker Host Port 9090
   ↓
Container Port 8080
   ↓
Spring Boot Application
   ↓
/hello
```

This is the main objective of the practical.

---

# PART M — VIEW THE CONTAINER LOGS

# Step 39: View Logs

Run:

```powershell
docker logs springboot-container
```

You should see Spring Boot startup messages.

### Explanation

The Spring Boot program is running inside the container.

Therefore, its output can be viewed using:

```text
docker logs
```

---

# PART N — STOP THE CONTAINER

# Step 40: Stop the Docker Container

Run:

```powershell
docker stop springboot-container
```

Now execute:

```powershell
docker ps
```

The container should no longer appear among the running containers.

---

# Step 41: Check All Containers

Run:

```powershell
docker ps -a
```

You should still see:

```text
springboot-container
```

but its status will indicate that it has stopped.

### Important

Stopping a container does not delete it.

```text
STOPPED ≠ DELETED
```

---

# Step 42: Remove the Container

Run:

```powershell
docker rm springboot-container
```

Verify:

```powershell
docker ps -a
```

---

# COMPLETE PRACTICAL WORKFLOW

The entire practical can now be understood using the following sequence:

```text
1. Create Spring Boot Maven Project
                ↓
2. Add Spring Web
                ↓
3. Create HelloController.java
                ↓
4. Run Spring Boot Locally
                ↓
5. Test localhost:8080/hello
                ↓
6. Create JAR Using Maven Wrapper
                ↓
7. Create Dockerfile
                ↓
8. Build Docker Image
                ↓
9. Run Docker Container
                ↓
10. Test localhost:9090/hello
```

---

# IMPORTANT FILES USED IN THIS PRACTICAL

| File/Folder | Purpose |
|---|---|
| `pom.xml` | Maven configuration file |
| `.mvn` | Maven Wrapper configuration folder |
| `mvnw` | Maven Wrapper for Linux/macOS |
| `mvnw.cmd` | Maven Wrapper for Windows |
| `src` | Java source code |
| `DemoApplication.java` | Main Spring Boot application |
| `HelloController.java` | REST controller created by us |
| `target` | Contains compiled application/JAR |
| `Dockerfile` | Instructions for building Docker image |

---

# IMPORTANT COMMANDS

| Purpose | Command |
|---|---|
| Check Java | `java -version` |
| Check Docker | `docker info` |
| Run Spring Boot | `.\mvnw.cmd spring-boot:run` |
| Build JAR | `.\mvnw.cmd clean package -DskipTests` |
| Check JAR | `dir target` |
| Build Docker image | `docker build -t springboot-docker-demo .` |
| List Docker images | `docker images` |
| Run container | `docker run -d --name springboot-container -p 9090:8080 springboot-docker-demo` |
| Check container | `docker ps` |
| View logs | `docker logs springboot-container` |
| Stop container | `docker stop springboot-container` |
| Show all containers | `docker ps -a` |
| Remove container | `docker rm springboot-container` |

---

# TROUBLESHOOTING

## Problem 1: `pom.xml` is not present

Do not proceed.

Go back to Spring Initializr and make sure:

```text
Project = Maven
```

Generate and extract the project again.

---

## Problem 2: I cannot see `.mvn`

`.mvn` begins with a dot and may be hidden.

In PowerShell run:

```powershell
dir -Force
```

---

## Problem 3: `mvn` command is not recognized

That is not a problem for this practical.

Do not use:

```powershell
mvn spring-boot:run
```

Use the Maven Wrapper:

```powershell
.\mvnw.cmd spring-boot:run
```

---

## Problem 4: `mvnw.cmd` cannot be found

First execute:

```powershell
dir
```

Make sure you are inside the folder containing:

```text
pom.xml
mvnw.cmd
src
```

If `mvnw.cmd` is genuinely absent, regenerate the Maven project from Spring Initializr rather than continuing with an incomplete project.

---

## Problem 5: Browser displays Jenkins

Check the port.

For Spring Boot running locally in this practical use:

```text
http://localhost:8080/hello
```

For the Docker container use:

```text
http://localhost:9090/hello
```

Do not use:

```text
localhost:8081
```

if Jenkins is already using that port.

---

## Problem 6: Port 8080 is already occupied

Find the program occupying it or use another Spring Boot port.

For this basic practical, first make sure no previous Spring Boot application is still running.

Press:

```text
Ctrl + C
```

in any terminal where an earlier Spring Boot application is running.

---

## Problem 7: Docker says JAR file is missing

Make sure you executed:

```powershell
.\mvnw.cmd clean package -DskipTests
```

Then check:

```powershell
dir target
```

You must have a `.jar` file before executing:

```powershell
docker build -t springboot-docker-demo .
```

---

## Problem 8: Docker container is not running

Check:

```powershell
docker ps -a
```

Then examine its logs:

```powershell
docker logs springboot-container
```

---

# OBSERVATION TABLE

| Observation | Result |
|---|---|
| Java working | Yes / No |
| Docker working | Yes / No |
| `pom.xml` available | Yes / No |
| `mvnw.cmd` available | Yes / No |
| Spring Boot started successfully | Yes / No |
| `/hello` working locally | Yes / No |
| JAR created | Yes / No |
| Docker image created | Yes / No |
| Docker container running | Yes / No |
| `/hello` working through Docker | Yes / No |

---

# SCREENSHOTS TO SUBMIT

Students should take screenshots of:

1. Spring Initializr configuration.
2. Extracted `demo` project showing `pom.xml` and `mvnw.cmd`.
3. `HelloController.java`.
4. Terminal showing successful Spring Boot startup.
5. Browser showing:

```text
http://localhost:8080/hello
```

6. Successful Maven build showing:

```text
BUILD SUCCESS
```

7. `Dockerfile`.
8. Successful `docker build`.
9. Output of:

```powershell
docker images
```

10. Output of:

```powershell
docker ps
```

11. Browser showing Dockerized application:

```text
http://localhost:9090/hello
```

---

# VIVA QUESTIONS

### Q1. What is Spring Boot?

Spring Boot is a Java framework that simplifies the development of stand-alone web applications, REST APIs, and microservices.

### Q2. What is `pom.xml`?

`pom.xml` is the Maven configuration file containing project information, dependencies, and build configuration.

### Q3. What is Maven Wrapper?

Maven Wrapper allows a Maven project to run Maven commands using project-provided wrapper scripts.

### Q4. Which Maven Wrapper file is used in Windows?

```text
mvnw.cmd
```

### Q5. What is `@RestController`?

It tells Spring Boot that the Java class handles REST/web requests.

### Q6. What is `@GetMapping("/hello")`?

It maps an HTTP GET request for `/hello` to a Java method.

### Q7. What is a JAR file?

A JAR is a Java archive containing the compiled application and its resources.

### Q8. What is Docker?

Docker is a platform for packaging and running applications inside containers.

### Q9. What is a Docker image?

A Docker image is a packaged template used to create containers.

### Q10. What is a Docker container?

A Docker container is a running instance of a Docker image.

### Q11. What is a Dockerfile?

A Dockerfile contains instructions used to build a Docker image.

### Q12. What does `docker build` do?

It creates a Docker image from a Dockerfile.

### Q13. What does `docker run` do?

It creates and starts a container from a Docker image.

### Q14. What does `-p 9090:8080` mean?

It maps port `9090` of the host computer to port `8080` inside the Docker container.

### Q15. What is the difference between Docker image and Docker container?

An image is a template, while a container is a running instance of that image.

---

# RESULT

A simple Spring Boot application was successfully created and tested locally. The application was then packaged as an executable JAR, converted into a Docker image using a Dockerfile, and executed inside a Docker container.

The practical demonstrated the complete workflow:

```text
Spring Boot
     ↓
REST Endpoint
     ↓
Local Execution
     ↓
JAR
     ↓
Dockerfile
     ↓
Docker Image
     ↓
Docker Container
     ↓
Spring Boot Application Running in Docker
```

Thus, the practical **Spring Boot with Docker** was successfully completed.
