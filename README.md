# EECE435L - Lab 8: Docker, Containers and Images

Author: Ali Naji (AUB username: `amn38`)

## Repository contents

| Path | What it is |
|---|---|
| [AliNaji_Lab8_Explanations.docx](AliNaji_Lab8_Explanations.docx) | Written explanations and screenshots (Activity 1 and Activity 2) |
| [Hello_Flask/](Hello_Flask/) | Sample "Hello World" Flask app, built as `flask_docker` (handout walkthrough) |
| [Lab5_Code/](Lab5_Code/) | Lab 5 Flask + SQLite user API with its Postman collection, **Image 1**, port 5000 |
| [Users_API/](Users_API/) | Small API exposing `GET /get_users`, **Image 2**, port 3000 |

Each folder has its own `Dockerfile`, `requirements` file and `.dockerignore`.

## Images

| Image | Source folder | Port |
|---|---|---|
| `amn38/lab8-ali_naji:0.0.1.RELEASE` | `Lab5_Code/` | 5000 |
| `amn38/lab8-ali_naji:0.0.2.RELEASE` | `Users_API/` | 3000 |
| `flask_docker:latest` | `Hello_Flask/` | 5000 |

## Build

Run from the repository root:

```bash
docker image build -t flask_docker Hello_Flask
docker image build -t amn38/lab8-ali_naji:0.0.1.RELEASE Lab5_Code
docker image build -t amn38/lab8-ali_naji:0.0.2.RELEASE Users_API
```

## Run

```bash
docker run -p 5000:5000 -d --name lab8_api amn38/lab8-ali_naji:0.0.1.RELEASE
docker run -p 3000:3000 -d --name lab8_users amn38/lab8-ali_naji:0.0.2.RELEASE
```

- Lab 5 API: <http://localhost:5000/api/users> (Postman collection in `Lab5_Code/postman/`)
- Names of all users: <http://localhost:3000/get_users> (returns e.g. `["Jane Doe"]`)

Port 5000 is used by both `flask_docker` and the Lab 5 image, so run only one of them at a time.

## Activity 1 commands

```bash
docker ps -a            # list all containers, running or stopped
docker stop lab8_api    # stop the container
docker logs lab8_api    # print the container's output
```

## Notes

- The images use `python:3.12-alpine`, not the handout's `3.8-alpine`, because the pinned Flask version needs Python 3.9 or newer.
- Docker image names must be lowercase, hence `lab8-ali_naji`.
