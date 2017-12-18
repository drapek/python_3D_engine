# Grafika komputerowa 
## Projekt 1 - silnik 3D

### Opis
Projekt ten jest realizacją własnego silnika 3D, pozwalającą realizować
przedstawienie prostych brył bez algorytmów przesłaniania. Jego podstawowym 
zadaniem jest zapoznanie się z metodami rzutowania modeli 3d na obraz 2d
wyświetlany przez monitor.

### Licencja
Projekt ten został zrealizowany w ramach zajęć _Grafika komputerowa_ na wydziale 
Elektrycznym Politechniki Warszawskiej. 

## Instalacja
```bash
pip install -r requirements.txt
python src/main.py
```

### Sterowanie
*Poruszanie się*:
* w - przód
* s - tył
* a - lewo 
* d - prawo
* p - ruch w górę (unoszenie się)
* l - ruch w dół (opadanie)

*obroty kamery*:
* ← - obrót kamery w lewo
* → - obrót kamery w prawo
* ↑ - pochylenie kamery w przód
* ↓ - pochylenie kamery w tył
* q - pochylenie kamery w stronę lewego ramienia
* e - pochylenie kamery w stronę prawego ramienia

*zoom*:
* m - zoom in
* n - zoom out

*przemieszczanie źródła światła*
* SHIFT + w - obróć światło względem osi Y w górę
* SHIFT + s - obróć światło względem osi Y w dół
* SHIFT + a - obróć światło względem osi X w lewo
* SHIFT + d - obróć światło względem osi X w prawo

*dodatkowe*
* o - pokaż krawędzie pod-trójkątów tworzacych strukturę obiektu



### Screenshots
![screnshot](https://github.com/drapek/python_3D_engine/blob/master/docs/screenshot_1.png?raw=true)
![screnshot](https://github.com/drapek/python_3D_engine/blob/master/docs/screenshot_2.png?raw=true)
![screnshot](https://github.com/drapek/python_3D_engine/blob/master/docs/screenshot_3.png?raw=true)
![screnshot](https://github.com/drapek/python_3D_engine/blob/master/docs/screenshot_4.png?raw=true)
![screnshot](https://github.com/drapek/python_3D_engine/blob/master/docs/screenshot_5.png?raw=true)
![screnshot](https://github.com/drapek/python_3D_engine/blob/master/docs/screenshot_6.png?raw=true)

### Wymagania
* Python 3.6.3
* PyGame 1.9.3
* Numpy 1.13.3
