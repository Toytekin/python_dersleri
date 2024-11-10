

class Araba():
        """docstring for Araba."""
        def __init__(self, beygir,model,renk,silindir,fiyat):
                print('------------------------------------\n')
                
                print('----------------İNİT ÇAĞRILDI--------------------')
                self.model=model
                self.beygir=beygir
                self.renk=renk
                self.silindir=silindir
                self.fiyat=fiyat
        
        def bilgileriGoster(self):
                print(""" 
                      
                      Model: {}
                      Beygir: {}
                      Renk: {}
                      Silindir: {}
                      Fiyat: {} TL
                      
                      """.format(self.model,self.beygir,self.renk,self.silindir,self.fiyat))
        
        def zamYap(self,zam_miktari):
                 print("Zam Yapılıyor....")  
                 self.fiyat=self.fiyat+zam_miktari   
                 print("İşlme tamamlandı. Yeni fiyat {} TL".format(self.fiyat))                         
    


araba1=Araba(100,"Toyata corolla","Siyah",4, 130000)

araba1.bilgileriGoster()
araba1.zamYap(100000)
        

