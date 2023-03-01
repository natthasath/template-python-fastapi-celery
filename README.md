# 🎉 Template Python FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It has a simple and easy to use API, is lightweight, and includes features like asynchronous support, dependency injection, and more.

![version](https://img.shields.io/badge/version-1.0-blue)
![rating](https://img.shields.io/badge/rating-★★★★★-yellow)
![uptime](https://img.shields.io/badge/uptime-100%25-brightgreen)

### 🏆 Run

- [http://localhost:8004](http://localhost:8004)
- [http://localhost:5556](http://localhost:5556)

```shell
docker-compose up -d
```

### 👉🏻 Try it out

```shell
curl http://localhost:8004/tasks -H "Content-Type: application/json" --data '{"type": 0}'
curl http://localhost:8004/tasks/<TASK_ID>
```