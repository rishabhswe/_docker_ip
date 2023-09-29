FROM python
COPY . .
RUN pip install flask
RUN pip install gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]
