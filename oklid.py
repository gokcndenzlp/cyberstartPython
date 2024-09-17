import math

# Öklid mesafesi hesaplayan fonksiyon
def öklidMesafe(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 2D uzaydaki noktaların listesi
points = [(1, 2), (4, 6), (5, 3), (2, 8), (7, 1)]

# Mesafeleri saklayacağımız liste
mesafe = []

# Tüm nokta çiftleri arasındaki mesafeleri hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktalar arasında mesafe hesaplamamak için j=i+1'den başlıyoruz
        distance = öklidMesafe(points[i], points[j])
        mesafe.append(distance)
        print(f"Distance between {points[i]} and {points[j]}: {distance}")

# En küçük mesafeyi bul
min_mesafe = min(mesafe)
print(f"\nMinimum distance: {min_mesafe}")
