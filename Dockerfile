FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
ENV PORT=5000
CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]
