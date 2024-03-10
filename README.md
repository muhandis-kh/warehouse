# Ombor loyihasi

> [!NOTE]
> Loyihadagi ma'lumotlar bazasidagi barcha ma'lumotlar qo'lda kiritilgan

Ma'lumotlar bazasiga mahsulotlar, xomashyolar va ombordagi maxsulotlar ko'rinishi shu holatda > 
* ![Screenshot 2024-03-11 015753](https://github.com/muhandis-kh/warehouse/assets/77358564/17d024ff-2c72-4768-ab34-6225551ae7ad)
  > Xomashyo turlari
* ![Screenshot 2024-03-11 015808](https://github.com/muhandis-kh/warehouse/assets/77358564/c4c94583-36de-41d0-8a0f-187cec418cbe)
  > Mahsulot turlari
* ![Screenshot 2024-03-11 015820](https://github.com/muhandis-kh/warehouse/assets/77358564/0352c179-c31f-43c6-b28f-16ed463494a1)
  > Mahsulot ishlab chiqarish uchun kerakli xomashyo ro'yhati
* ![Screenshot 2024-03-11 015834](https://github.com/muhandis-kh/warehouse/assets/77358564/9d323502-c5b4-4ef1-bf4c-ae3116d8ce05)
  > Ombordagi xomashyolar soni va narxi ko'rsatilgan ro'yhat

Loyihanidan kutilgan ma'lumotni olish uchun localhostda http://127.0.0.1:8000/api/check/ manziliga 
  ```
  {
    "products": [
      {
        "product_name": "Ko'ylak",
        "product_qty": 30
      },
      {
        "product_name": "Shim",
        "product_qty": 20
      }
    ]
  }
  ```
ushbu JSON ma'lumotlarini yuborish kerak 
