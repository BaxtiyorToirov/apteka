###########################################   APTEKA   ###################################################################### 


# from time import sleep                              
# from os import system

# class Dori:

#     lst=[]
#     narxi={"trimol":5000,"sitramol":10000,"nimisil":12000,"tabletka":8000,"noshpa":6000}
#     dct={"trimol":5,"sitramol":10,"nimisil":12,"tabletka":8,"noshpa":5}
#     def sklat(self):
#         self.salom=12
#         a=0
#         for i in self.dct:
#             a+=1
#             self.lst.append(i)
#             print(f"{a}-{i},narxi={self.narxi[i]}")
                

# class Apteka(Dori):
#     a=0
#     def __init__(self):
#         print("Assalomu alaykim Aptekaga xush kelibsiz!!!\n")
#         print("1-Dorilarni ruyhatini kurish\n2-Dori sotib olish\n3-olingan dorini qaytarish")
#         print("4-chiqish")
#         menyu=int(input(">>>"))
#         # system("cls")
#         if menyu ==1:
#             super().sklat()
#             print("\n  Dori sotib olish uchun ortga qayting")
#             print("0-Ortga qaytish")
#             qaytish=int(input(">>>"))
#             if qaytish==0:
#                 # system("cls")
#                 self.__init__()
#             else:
#                 print("Tugri raqam kiriting!!!")
#             # system("cls")
#         elif menyu==2:
#             if len(self.lst)==0:
#                 print("Birinchi dorilar ruyhatini kuring!!!")
#                 sleep(5)
#                 # system("cls")
#                 self.__init__()
#             else:
#                 self.olish()
#         elif menyu==3:
#             self.qaytar()
#         elif menyu==4:
#             print("Hayr sog' buling")
#             exit()
#     lst2=[]
#     lst3=[]
#     def olish(self):
#             print("qaysi dorini sotib olmoqchisiz?")
#             dori=input(">>>")
#             if dori in self.lst:
#                 print(f"Nechta  {dori}  olasiz")
#                 dori2=int(input(">>>"))
#                 # self.lst3.append(self.narxi[dori]*dori2)
#                 self.a=dori2
#                 if dori2<=self.dct[dori]:
#                     print("Dori oldingiz!!!")
#                     self.lst2.append([dori,self.dct[dori]])
#                     self.dct[dori]-=dori2
#                     self.qushimcha()
                    
#                 else:
#                     print("bizda bunday miqdordagi dori yetarli emas!!!")
#                     self.qushimcha()

#             else:
#                 print("bunday dori mavjud emas!!!")
#     def hisoblash(self):
#         if len(self.lst2)>0:
#             print("Siz olgan dorilar:")
#             for j in self.lst2:
#                 print(f"     {j[0]}")
                
#                 self.lst3.append(self.a*self.narxi[j[0]])
            
#             print(f"Sizdan {sum(self.lst3)} so'm buldi")
            
#         else:
#             print("Sizda hali dori mavjud emas!!!")
#     def qushimcha(self):
#         print("Yana dori olasizmi?")
#         print("1-XA\n2-YUQ")
#         yana=int(input(">>>"))
#         if yana ==1:
#             self.olish()
#         else:
#             print("mobodo dori qaytarmaysizmi!!!")
#             print("1-XA\n2-YUQ")
#             qayt=int(input(">>>"))
#             if qayt==1:
#                 for k in self.lst2:
#                     print(k[0])
#                 print("qaysi dorini qaytarmoqchisiz?")
#                 qayt2=input(">>>")
#                 for i in self.lst2:
#                     if qayt2==i[0]:
#                         self.lst2.remove(i)
#                 print(f"Siz {qayt2} qaytardingiz!")
#                 self.qushimcha()

#                 # print(self.lst2)
#             else:
#                 self.hisoblash()
#     def qaytar(self):
#         self.hisoblash() 
#         print("Dori olish uchun 1-bosing va dorilar ruyhatiga kiring!")
#         qaytar=int(input(">>>"))
#         if qaytar==1:
#             self.__init__()
#         else:
#             print("tug'ri raqam kiriting!!!")
#             self.qaytar()   
            
            
            
                
# ap1=Apteka()














# from time import sleep


# class Apteka:
#     def init(self, lokatsiya, nomi, ishchilar_soni, telefon_raqami):
#         self.lokatsiya = lokatsiya
#         self.nomi = nomi
#         self.ishchilar_soni = ishchilar_soni
#         self.telefon_raqami = telefon_raqami
#         self.dct = {}

#     def dorilar_ruyxati(self):
#         self.dori = [{
#             "Parasetamol": {"nomi": "Parasetomol",
#                             "muddati": 12,
#                             "narxi": 8000
#                             }
#         }, {
#             "Sitramon": {"nomi": "Sitramon",
#                          "muddati": 10,
#                          "narxi": 6000}
#         }, {
#             "Valerianka": {"nomi": "Valerianka",
#                            "muddati": 12,
#                            "narxi": 15000}
#         }, {
#             "Taylol-hot": {"nomi": "Taylol-hot",
#                            "muddati": 3,
#                            "narxi": 18000}
#         }, {
#             "Nemisil": {"nomi": "Valerianka",
#                         "muddati": 2,
#                         "narxi": 5000}
#         }, {
#             "Kupen": {"nomi": "Kupen",
#                       "muddati": 3,
#                       "narxi": 10000}
#         }, {
#             "Pankreatin": {"nomi": "Pankreatin",
#                            "muddati": 5,
#                            "narxi": 5000}
#         }, {
#             "Mezim": {"nomi": "Mezim",
#                       "muddati": 3,
#                       "narxi": 8000}
#         }, {
#             "Loratal": {"nomi": "Loratal",
#                         "muddati": 3,
#                         "narxi": 15000}
#         }, {
#             "Sifloks": {"nomi": "Sifloks",
#                         "muddati": 2,
#                         "narxi": 2000}
#         }]
#         return self.dori

#     def get_ishchi(self):
#         return self.ishchilar_soni
#     lst=[]
#     def get_nomi(self):
#         self.zakaz = input("\nZakaz kiriting: ")
#         # for i in self.dorilar_ruyxati():
#         #     if self.zakaz in i:
#         #         for j in i:
#         #             self.dct[self.zakaz]
#         self.lst.append(self.zakaz)
#         print(f"Nechta {self.zakaz} olasiz")
#         zakaz1=int(input(">>> "))
#         self.lst.append(zakaz1)
#         self.sura()
#         # return self.lst
#     def sura(self):
#         print("Yana zakaz kiritasizmi? ")
#         print("1-XA\n2-YUQ")
#         tanla=int(input(">>> "))
#         if tanla==1:
#             self.get_nomi()
#         else:
#             print(f"Siz olgan dorilar {self.lst}")
#     def get_hisob(self):
#         self.b = 0
#         for i in self.dorilar_ruyxati():
#             if self.zakaz in i:
#                 for j in i:
#                     self.b += i[j]["narxi"]
#         return self.b

#     def get_narxi(self):
#         self.lst_narx = []
#         for i in self.dorilar_ruyxati():
#             for j in i:
#                 self.lst_narx.append()

#     def raqam(self):
#         return self.telefon_raqami

#     def get_info(self):
#         print(f"""
# Apteka lokatsiyasi: {self.lokatsiya}
# Apteka nomi: {self.nomi}
# Ishchilar soni: {len(self.ishchilar_soni)} ta
# Telefon raqami: {self.telefon_raqami}
# """)


# # dori = Apteka("Toshkent", "Pharm", ["Dilshod", "Ilyos", "Azam"], 998912226444)
# # print(dori.get_info())


# class Tanish(Apteka):
#     def init(self,lokatsiya, nomi, ishchilar_soni, telefon_raqami):
#         super().init(lokatsiya, nomi, ishchilar_soni, telefon_raqami)
#         print("""
#     [1] -> Apteka
#     [2] -> Ishchilar ro'yxati
#     [3] -> Dorilar ro'yxati
#     [4] -> Hisob-Kitob
#     [5] -> Narxlar
#     """)
#         while True:
#             choice = int(input("--> "))
#             if choice == 1:
#                 self.get_info()
#             elif choice == 2:
#                 print(self.get_ishchi())
#             elif choice == 3:
#                 a=self.dorilar_ruyxati()
#                 for i in a:
#                     print(i)
#                 print(self.get_nomi())
#             elif choice == 4:
#                 count=0
#                 print(self.lst)
#                 for j in self.lst:
#                     # self.sura()
#                     if count%2!=0:
#                         # if self.dori['nomi'] == 
#                         # print(f"Siz xarid qilgan dorilar: {self.dori}")
#                         b=j
#                         print(b)
#                     else:
#                         print(j)
#                         for i in self.dori:

#                             print(i[j])


#                     count+=1

#             elif choice == 5:
#                 self.lst_narx()
#             else:
#                 exit()
# tanish1=Tanish()
# # tanish1.init("Toshkent", "Pharm", ["Dilshod", "Ilyos", "Azam"], 998912226444)
#     # print(dori.get_nomi())
# # print(dori.raqam())