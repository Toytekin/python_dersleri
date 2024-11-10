class Calisan():
        def __init__(self, isim,maas,departman):
                self.isim=isim
                self.maas=maas
                self.departman=departman
                
                
        def bilgileriGoster(self):
                 print("""
                       İsim: {}
                       Maaş: {}
                       Departman: {} TL
                       """.format(self.isim,self.maas, self.departman))  
                 
        def departmanDegistir(self,yeni_departman):
                print('Departman Değiştirildi ')
                self.departman=yeni_departman               

class Yonetici(Calisan):
        
        
        def __init__(self, isim,maas,departman,hisssedurumu):
                self.isim=isim
                self.maas=maas
                self.departman=departman
                self.hissseDurumu=hisssedurumu
        
        def zamYap(self,zam_miktari):
                print('Zam yapıldı...')
                self.maas=self.maas+zam_miktari
                
        def hisse_durumu_goster(self):
                        if self.hissseDurumu==True:
                                print('Hisse durumu YÜKSELİŞTE')
                        else:
                               print('Hisse durumu ALÇALIŞTA')
        
        def hisse_durumu_guncelle(self,yeni_hisse_durumu):
                 self.hissseDurumu=yeni_hisse_durumu
                
                    
 


yonetici1=Yonetici("İbrahim TOYTEKİN",90000,"patron",True)
 
yonetici1.bilgileriGoster()  
yonetici1.departmanDegistir('KASA')   
yonetici1.bilgileriGoster() 
yonetici1.zamYap(10000)
yonetici1.bilgileriGoster() 
yonetici1.hisse_durumu_goster()
yonetici1.hisse_durumu_guncelle(False)
yonetici1.hisse_durumu_goster()
