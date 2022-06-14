# backend-huno

host:
https://grupohuno-backend.herokuapp.com
or
http://localhost:8000

## Endpoints

#### Get all the product:

GET {host}/api/v1/products/

#### Get specific product:

GET {host}/api/v1/products/{:id}

#### Get specific category:

GET {host}/api/v1/products/category/{:category}

#### Search

GET {host}/api/v1/product-search/?keyword={word searching}

#### Update products

POST {host}/api/v1/update-products/

Body:

```
{
    "store": "lider",
    "products_list": [{...}]
} 
```

Body example:

```
{
    "store": "lider",
    "products_list": [{
      "name": "Cerveza Lager Botellin",
      "store": "lider",
      "category": "cerveza",
      "sku": "1111111224545",
      "brand": "Corona",
      "size": "330cc",
      "image_url": "https://images.lider.cl/wmtcl?source=url%5Bfile:/productos/993393b.jpg%5D&viewport=color%5Bwhite%5D,height%5B800%5D,seed%5B1633617940%5D,vsize%5B524%5D,width%5B800%5D,x%5B0%5D,y%5B0%5D&sink",
      "page_url": "https://www.lider.cl/supermercado/product/Corona-Cerveza-Lager-Botellin/993393",
      "price": 1990,
      "is_promotion": true
  },
  {

      "name": "Pisco especial 35° Botella",
      "store": "lider",
      "category": "pisco",
      "sku": "2222222",
      "brand": "Alto del Carmen",
      "size": "1L",
      "image_url": "https://images.lider.cl/wmtcl?source=url%5Bfile:/productos/468481a.jpg%5D&viewport=color%5Bwhite%5D,height%5B800%5D,seed%5B1652203843%5D,vsize%5B524%5D,width%5B800%5D,x%5B0%5D,y%5B0%5D&sink",
      "page_url": "https://www.lider.cl/supermercado/product/Alto-del-Carmen-Pisco-especial-35-Botella/468481",
      "price": 2990
  },
  {
      "name": "Bebida Light Botella",
      "store": "A",
      "category": "bebida",
      "sku": "3333333",
      "brand": "Coca-Cola",
      "size": "2,5L",
      "image_url": "https://images.lider.cl/wmtcl?source=url%5Bfile:/productos/7415a.jpg%5D&viewport=color%5Bwhite%5D,height%5B1000%5D,seed%5B1652238315%5D,vsize%5B524%5D,width%5B1000%5D,x%5B0%5D,y%5B0%5D&sink",
      "page_url": "https://www.lider.cl/supermercado/product/Coca-Cola-Bebida-Light-Botella/7415",
      "price": 3990
  }]
}
```
