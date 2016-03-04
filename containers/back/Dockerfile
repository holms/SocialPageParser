FROM holms/jessie:py3-latest
ADD . /var/www/project
WORKDIR /var/www/project
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
