FROM python

WORKDIR /tests_project/
RUN apk update
RUN apk chromium chromium-chromedriver

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-v"]