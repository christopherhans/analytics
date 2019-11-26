# Analytics Framework
HTW PITB 1. Semester \
Ist nur bedingt anwendbar auf Datensätze, die wir nicht in der Vorlesung behandelt haben.

## Ausführen
````
python analytics.py -i <path/to/csv>

````
Optional: ``pip install -r requirements.txt``
### Parameter

| Kurz | Lang | Anwendung | Beschreibung |
|------|:----:|:---------:|:------------:|
| -i   | --inventory | Pfad zum CSV file | Gibt die Datei an, die eingelesen werden soll. |
| -s   | --scope | Für jedes Column, welches betrachtet werden muss, muss ein -s angehangen werden | Die Columns, die in das betrachtete Dataframe übernommen werden. |
| -r   | --report | / | Erzeugt einen kurzen Bericht in der Shell. |
| -d   | --debug | / | Erzeugt ein paar Print-Ausgaben, um den Programmablauf besser nachvollziehen zu können. |


### Klassen

![Class Diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/christopherhans/analytics/master/UML/data.puml?token=ADYAJWLGV7FS56UD5P7TMBS53TXFS)

Ein Objekt der Data-Klasse dient als modifizierbare/abfragbare Instanz des original Dataframes. \
``object = Data(<path to csv>)``

### Module

#### DataCleaning
Dient der Bereinigung der Daten:

Funktion | Nutzen 
--- | ---
remove_static_columns() | Entfernt alle Spalten die leer sind, oder nur den selben Wert enthalten.
remove_customs() | Entfernt alle Spalten, die der Funktion als Liste übergeben werden.
price_to_float() | Transformiert einen String in einen Floatwert, sofern der Wert einen Dollarwert darstellt.
remove_nan() | Entfernt alle Zeilen mit einem NaN Wert.
numeric() | Checkt, ob eine Spalte nur Strings enthält, die eine Zahl darstellen sollen und transformiert diese in einen Float.
remove_outlier() | Entfernt die Ausreißer aller Spalten mit numerischen Werten.

#### MachineLearning
Bereitet das Dataframe für Machine Learning Algorithmen vor.

Funktion | Nutzen
--- | ---
one_hot_encoding() | Encoded die übergebene Spalte. Drop_first ist möglich.
train_test() | Erstellt Trainings- und Testdatensatz.
scaler() | Skaliert den Trainings- und Testdatensatz.

#### KNN
Führt den k-Nearest-Neighbor Algorithmus durch.

Funktion | Nutzen
--- | ---
run() | Führt den Algorithmus aus. Kann mit oder ohne skalierten Werten durchgeführt werden.

#### LRegression
Führt eine Lineare Regression durch.

Funktion | Nutzen
--- | ---
run() | Führt den Algorithmus aus. Kann mit oder ohne skalierten Werden durchgeführt werden.

### Methoden
#### price_to_float
Entfernt Dollerzeichen und Kommatas (werden in der US Schreibweise genutzt) und wandelt den String in einen Float um.

#### remove_outlier_by_column
Entfernt die Zeilen, die in einer bestimmten Spalte Ausreißer haben. Dazu werden die Quantile der Spalten herangezogen.

#### report
Gibt zum Ende der Programmlaufzeit Werte in der Shell aus. Z.B. den Mean-Squared-Error oder einen Plot.
Kann beliebig angepasst werden. \
Wird mit dem Kommandozeilenparameter ``-r`` oder `--report` aktiviert.

#### print_debug
Gibt eine Nachricht aus, wenn der Debugmodus aktiviert ist. \
Wird mit dem Kommandozeilenparameter ``-d`` oder `--debug` aktiviert.
