FROM mongo

COPY titanic.csv /titanic.csv
CMD mongoimport --host mongodb --db titanic --collection titanic --type csv --headerline --file /titanic.csv --headerline