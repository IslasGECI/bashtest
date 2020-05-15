FROM python
WORKDIR /workdir
COPY . .
RUN pip install pytest
CMD make
