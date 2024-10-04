# Statystyczna analiza języka łotewskiego z wykorzystaniem prawa Zipfa i sieci słów

Projekt przeprowadza statystyczną analizę artykułów w języku łotewskim z wykorzystaniem prawa Zipfa oraz wizualizuje powiązania między słowami za pomocą grafu słów. Analiza bazuje na danych tekstowych pobranych z łotewskiej Wikipedii i obejmuje:

- **Przetwarzanie tekstu**: Czyszczenie, tokenizacja i analiza częstości słów.
- **Wykorzystanie prawa Zipfa**: Obliczanie i wizualizacja zależności między rangą a częstością występowania słów.
- **Grafy słów**: Tworzenie i wizualizacja grafów, gdzie wierzchołkami są słowa, a krawędziami ich współwystępowanie w tekście.

Projekt pozwala na lepsze zrozumienie rozkładu słów w języku łotewskim oraz ich wzajemnych powiązań. Do analizy zostały wykorzystane teksty o różnej tematyce, zaczynając od ustaw ze stron rządowych, poprzez łotewskie powieści i bajki, kończąc na artykułach naukowych. Wybierając materiały starałyśmy się, żeby nie zawierały zbyt specjalistycznego słownictwa, co mogłoby wpłynąć negatywnie na wyniki. 

**Kroki realizacji projektu**:
1. Na początku podzieliłyśmy tekst na zdania (funkcja sent_tokenize). Następnie przeprowadziłyśmy czyszczenie tekstu: usunięcie znaków interpunkcyjnych, zamienienie wszystkich liter na małe.
2. Przekształciłyśmy tekst na listy słów (funkcja split()), wyznaczyłyśmy częstości ich występowania (obiekt Counter). Umożliwiło to wygenerowanie tabeli (pandas.DataFrame), w której wykorzystałyśmy prawo Zipfa. Została ona zapisana do pliku csv.
3. Na podstawie tabeli (korzystając z matplotlib) stworzyłyśmy wykres zależności rangi słów od ich częstości.
4. Następnie wygenerowałyśmy graf słów (Graf 1) przy użyciu biblioteki networkx. Graf został zwizualizowany, a jego obraz zapisany do pliku.
5. Na podstawie stworzonego grafu zbadałyśmy liczbę połączeń (krawędzi) dla każdego węzła (słowa). Węzły o największej liczbie połączeń zostały uznane za najważniejsze dla rdzenia języka. Wyodrębniłyśmy 100 słów o największej liczbie krawędzi.
6. Najważniejsze słowa zostały wypisane w formie tabeli. Ich podgraf uznałyśmy za rdzeń języka.

**Wyniki**

Sporządziłyśmy tabelę najpopularniejszych słów. W pierwszej kolumnie znajdują się słowa posortowane w kolejności od największej liczby wystąpień (kolumna druga). Rangi ( kolumna trzecia) zostały przedstawione jako kolejne liczby całkowite zaczynając od 1 (dla słowa o największej liczbie wystąpień w tekście). Ostatnia kolumna tabeli zawiera iloczyn częstotliwości i rangi. 

_Pełna tabela dostępna pod:_ https://github.com/ajochymczyk/Analiza-statystyczna-lotewskiego/blob/master/zipf_table.csv

Wygenerowałyśmy graf w którym każdy z wierzchołków jest występującym w tekście słowem, krawędzie występują w miejscach, gdzie dwa słowa występują po sobie w zdaniu. Graf pokazuje zależności współwystępowania słów.

![Graf 1](https://github.com/ajochymczyk/Analiza-statystyczna-lotewskiego/blob/master/graph.png)

Następnie ograniczyłyśmy wyniki do najczęściej występujących słów stanowiących rdzeń języka, co pokazałyśmy na drugim grafie:

![Graf 2](https://github.com/ajochymczyk/Analiza-statystyczna-lotewskiego/blob/master/core_graph.png)


**Wnioski**

Projekt potwierdził, że prawo Zipfa dobrze opisuje rozkład częstości słów w tekście łotewskim. Tworzenie sieci współwystępujących słów pozwoliło na identyfikację wyrazów stanowiących rdzeń języka.

