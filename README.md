# A\* Puzzle Visualizer (Pygame)

Bu proje, **Python + Pygame** kullanılarak geliştirilmiş interaktif bir **A\*** algoritması görselleştirme uygulamasıdır. Kullanıcı grid üzerinde başlangıç noktası, hedef noktası ve engeller belirleyerek algoritmanın en kısa yolu nasıl bulduğunu canlı olarak izleyebilir.

## 🚀 Özellikler

- Başlangıç noktası seçme
- Hedef noktası seçme
- Engel (duvar) ekleme
- A\* algoritması ile en kısa yol bulma
- Pygame ile görsel animasyon
- Tek tuşla sıfırlama

## 📁 Proje Yapısı

```bash
project/
│── main.py
│── config.py
│── grid.py
│── astar.py
│── visualizer.py
│── README.md
```

## ⚙️ Kurulum

1. Python 3.10+ kurulu olmalıdır.
2. Gerekli paketi yükleyin:

```bash
pip install pygame
```

## ▶️ Çalıştırma

```bash
python main.py
```

Mac için:

```bash
python3 main.py
```

## 🎮 Kullanım

### Mouse Sol Tık

1. İlk tık: Başlangıç noktası
2. İkinci tık: Hedef noktası
3. Sonraki tıklar: Engel ekler

### Klavye Tuşları

- `SPACE` → A\* algoritmasını başlatır
- `R` → Grid'i sıfırlar

## 🧠 A\* Algoritması

```text
f(n) = g(n) + h(n)
```

- `g(n)` = başlangıçtan mevcut düğüme maliyet
- `h(n)` = hedefe tahmini uzaklık
- `f(n)` = toplam skor

En düşük skorlu düğüm seçilerek hedefe ulaşılır.

## 🎨 Hücre Renkleri (Örnek)

- Yeşil: Başlangıç
- Kırmızı: Hedef
- Siyah: Engel
- Mavi: Açık liste
- Sarı: En kısa yol

## 📚 Kullanım Alanları

- Harvard CS50 AI öğrencileri
- Pathfinding algoritmaları öğrenenler
- Python + Pygame pratiği yapmak isteyenler
- Oyun algoritmaları geliştirenler

## 🔧 Geliştirme Fikirleri

- DFS / BFS / Dijkstra ekleme
- Maze generator
- Speed slider
- Diagonal movement
- Sound effects

## ⭐ Katkı

Projeyi geliştirmek istersen fork edip katkıda bulunabilirsin.
