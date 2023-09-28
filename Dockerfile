FROM python
COPY . .
RUN pip install flask
CMD ["flask", "run", "--host", "0.0.0.0"]
