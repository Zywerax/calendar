FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# update data from apt-get repositories
RUN apt-get update && \
    apt-get -y install unzip && \
    apt-get -y install curl && \
    apt-get -y install gnupg && \
    apt-get -y install wget

# sql server drivers and bcp
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools18 && \
    echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc && \
    apt-get install -y unixodbc-dev && \
    apt-get install -y libgssapi-krb5-2

ENV PATH="$PATH:/opt/mssql-tools18/bin"

# 3. Instalacja Pythona
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kod aplikacji
COPY . .

# 5. Uruchomienie aplikacji
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
