FROM python
WORKDIR workdir
COPY . .
CMD make
