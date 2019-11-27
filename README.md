# Analytics Framework
HTW PITB 1. Semester \
Ist nur bedingt anwendbar auf Datensätze, die wir nicht in der Vorlesung behandelt haben.

## Ausführen
````
python analytics.py -i <path/to/csv> -y <column>

````
Optional: ``pip install -r requirements.txt``
### Parameter

|Pflicht| Kurz | Lang | Anwendung | Beschreibung |
|---|------|:----:|:---------:|:------------:|
| x | -i   | --inventory | Pfad zum CSV file | Gibt die Datei an, die eingelesen werden soll. |
| x | -y   | --result | Name der Ziel-Spalte | Welcher Wert ist y/f(x) |
|   | -s   | --scope | Für jedes Column, welches betrachtet werden muss, muss ein -s angehangen werden | Die Columns, die in das betrachtete Dataframe übernommen werden. |
|   | -r   | --report | / | Erzeugt einen kurzen Bericht in der Shell. |
|   | -d   | --debug | / | Erzeugt ein paar Print-Ausgaben, um den Programmablauf besser nachvollziehen zu können. |
|   | -S   | --scaled| / | Nutzt sklaierte Werte für ML |
|   | -D   | --drop_first | / | Setzt drop_first beim OneHotEncoding auf True |
|   | -k   | --knn | Anzahl der Nachbarn | Aktiviert den k-Nearest-Neighbor Algorithmus |
|   | -l   | --linear_regression | / | Aktiviert den Linearen Regressionsalgorithmus |

---
### Klassen

![Class Diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/christopherhans/analytics/master/UML/data.puml?token=ADYAJWIDVQTFTEP45EHOBTK53TXQ4)

Ein Objekt der Data-Klasse dient als modifizierbare/abfragbare Instanz des original Dataframes. \
``object = Data(pd.DataFrame())``

---
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
property_type_() | Kategorisiert den property_type anhand des Durchschnittspreises.

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

---
### Methoden
#### price_to_float
Entfernt Dollerzeichen und Kommatas (werden in der US Schreibweise genutzt) und wandelt den String in einen Float um.

#### remove_outlier_by_column
Entfernt die Zeilen, die in einer bestimmten Spalte Ausreißer haben. Dazu werden die Quantile der Spalten herangezogen.

#### process_property_type
Berechnet den Durchschnittspreis für jeden Propertytype. Teil diese dann anhand des Durchschnittspreises in 4 Kategorien ein.

#### report
Gibt zum Ende der Programmlaufzeit Werte in der Shell aus. Z.B. den Mean-Squared-Error oder einen Plot.
Kann beliebig angepasst werden. \
Wird mit dem Kommandozeilenparameter ``-r`` oder `--report` aktiviert.

#### print_debug
Gibt eine Nachricht aus, wenn der Debugmodus aktiviert ist. \
Wird mit dem Kommandozeilenparameter ``-d`` oder `--debug` aktiviert.
