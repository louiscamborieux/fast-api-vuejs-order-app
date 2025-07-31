# How to start the application

## 1. Install Dependencies

1. [Python](https://www.python.org/downloads/)
2. [Python3-pip](https://pip.pypa.io/en/stable/installation/)
2. [FastAPI](https://fastapi.tiangolo.com/tutorial/#run-the-code)
3. [nodeJS (min 22.12.0)](https://nodejs.org/en/download)

## 2. Install modules
In /frontend root do:
```npm install ```

In /backend root do:
``` 
pip install "fastapi[standard]"
pip install pytest
```

## 3. Start the application
1. Start backend : in /backend do
```
fastapi dev app/main.py
```
2. Start front-end : in /frontend do
```
npm run dev
```