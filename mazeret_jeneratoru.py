#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bürokratik Gecikme Mazeret Jeneratörü
Her çalıştırmada mazeretinizi 3 seviyede şişirir.
Sonunda varoluşsal bir kriz yaratır.
"""

import random
import sys

seviye1 = [
    "trafik çok yoğundu, herkes aynı anda aynı yere gidiyor gibiydi",
    "otobüs şoförü birden durup çay molası verdi",
    "yolda bir kedi geçti, mecburen durdum ve ona selam verdim",
    "telefonum şarjı bitti, saat kaç olduğunu bilemedim"
]

seviye2 = [
    "asıl sorun şu ki, devlet daireleri arasında evraklar ışık hızından yavaş ilerliyor",
    "zamanın kendisi bürokratik onay bekliyor, bu yüzden geç kaldım",
    "evrenin genişlemesi yüzünden yollar uzadı, fizik yasaları suçlu",
    "bir memur imza atmayı unuttu, o imza olmadan zaman akmıyor"
]

seviye3 = [
    "bu gecikme aslında varoluşsal bir sorgulamanın sonucu, belki de hiç gitmemeliydim",
    "zamanın ötesinde bir bürokrat, evrenin sonunu onaylamadığı için geç kaldık",
    "her şey bir simülasyon, simülasyonun admini kahve molasında",
    "belki de ben hiç var olmadım, bu yüzden yetişemedim"
]

def mazeret_uret(sebep="bilinmeyen bir sebep"):
    print(f"\n=== BÜROKRATİK MAZERET RAPORU ===")
    print(f"Başlangıç sebebi: {sebep}\n")
    
    print(f"Seviye 1 (Sıradan): {random.choice(seviye1)}")
    print(f"Seviye 2 (Bürokratik): {random.choice(seviye2)}")
    print(f"Seviye 3 (Varoluşsal): {random.choice(seviye3)}")
    
    print("\nSonuç: Geç kaldınız çünkü evren onay vermedi.")
    print("Lütfen bir sonraki sefere zamanın kendisinden izin alın.\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sebep = " ".join(sys.argv[1:])
    else:
        sebep = input("Neden geç kaldınız? (boş bırakabilirsiniz): ") or "hiçbir sebep yok"
    mazeret_uret(sebep)
