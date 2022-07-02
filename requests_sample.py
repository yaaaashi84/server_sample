import requests


def main():
    res = requests.get("http://127.0.0.1:8000/sample.html")
    print(res.headers)


if __name__ == "__main__":
    main()