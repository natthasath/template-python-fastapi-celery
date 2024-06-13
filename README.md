# 🎉 Template Python FastAPI Celery

Celery is a distributed task queue for Python that helps you run tasks asynchronously across multiple worker nodes or machines, making it ideal for handling time-consuming or CPU-bound tasks in web applications, machine learning workflows, and other complex systems.

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

<br>

Trigger a new task:

```shell
curl http://localhost:8004/tasks -H "Content-Type: application/json" --data '{"type": 0}'
```

Check the status:

```shell
curl http://localhost:8004/tasks/<TASK_ID>
```
