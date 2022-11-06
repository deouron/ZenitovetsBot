FROM python:3-onbuild
EXPOSE 8888
CMD ["python", "main.py", "utils.py", "parser.py"]