#import string
class Kost:
  def __init__(self, noKamar, kasur, kamarMandi):
    self.noKamar = noKamar
    self.kasur = kasur
    self.kamarMandi = kamarMandi

  def cekHarga(self):
    if self.kasur == "ya" and self.kamarMandi == "ya":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
      harga = 500000                                                                                                                  
      return harga
    elif self.kasur == "tidak" and self.kamarMandi == "ya":
      harga = 400000
      return harga
    elif self.kasur == "tidak" and self.kamarMandi == "ya":
      harga = 200000
      return harga

  def cekTotal(self):
    total = self.cekHarga()
    return total
noKamar = int(input("Masukkan nomor kamar: "))
kasur = input("Berapa kasur yang tersediakan? : ")   
kamarMandi = input("Berapa kamar mandi yang disediakan: ")
 
kost = Kost(noKamar, kasur, kamarMandi)
print("==============================================================")
print("Kamar Kost Dengan Kelengkapan:")
print("No.Kamar:", kost.noKamar)
print("Kasur:", kost.kasur)
print("Kamar Mandi:", kost.kamarMandi)
print("==============================================================")
print("Harga: Rp", kost.cekTotal())
