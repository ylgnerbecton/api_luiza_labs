# Documentação API

Esta documentação descreve a estrutura da API de gerenciamento de produtos favoritos e clientes e exemplos de uso.


## Clientes
Os endpoints de clientes possuem a seguinte estrutura:

- `name`: nome do cliente
- `email`: email do cliente

É possível cadastrar, atualizar o nome, excluir e visualizar clientes.

# Cadastrar Cliente

``http://127.0.0.1:5000/client``

**Método**: POST

**Request**: 
```
{
	"name": "Ana", 
	"email": "ana@email.com"
}
```

**Response**:

```
{
  "message": "Client was successfully created.",
  "object": {
    "_id": 1,
    "email": "ana@email.com",
    "name": "Ana"
  }
}
```

# Atualizar Cliente

``http://127.0.0.1:5000/client/update/``

**Método**: PUT

**Request**: 
```
id = 1
name = Ana Maria
```

**Response**:

```
{
  "message": "Client was successfully updated.",
  "object": {
    "_id": 1,
    "email": "ana@email.com",
    "name": "Ana Maria"
  }
}
```

# Remover Cliente

``http://127.0.0.1:5000/client/remove/``

**Método**: DELETE

**Request**: 
```
id = 1
```

**Response**:

```
{
  "message": "Client was successfully removed.",
  "object": {
    "_id": 1,
    "email": "ana@email.com",
    "name": "Ana Maria"
  }
}
```

# Exibir Cliente

``http://127.0.0.1:5000/client/``

**Método**: GET

**Request**: 
```
id = 2
```

**Response**:

```
{
  "_id": 2,
  "email": "roberto@email.com",
  "name": "Roberto"
}
```

# Exibir todos os clientes

``http://127.0.0.1:5000/clients``

**Método**: GET

**Request**: 
\- 

**Response**:

```
[
  {
    "email": "roberto@email.com",
    "id": 2,
    "name": "Roberto"
  },
  {
    "email": "maria@email.com",
    "id": 3,
    "name": "Maria"
  }
]
```

## Produtos favoritos

Os endpoints de produtos favoritos são sempre acessados através do código do cliente. Eles possuem a seguinte estrutura:

- `_id`: código do cliente,
- `email`: email do cliente
- `name`: nome do cliente
- `product`: lista de produtos
- `brand`: marca do produto
- `id`: id do produto
- `image`: imagem do produto
- `price`: preço do produto
- `title`: nomd do produto
- `reviewScore`: média dos reviews para este produto (opcional)

É possível adicionar um ou vários produtos à lista de favoritos de um cliente.

# Adicionar produto como favorito

``http://127.0.0.1:5000/client/product/add/``

**Método**: GET

**Request**: 
```
client_id = 2
product_id = fe0f6c82-35a7-4963-95bb-f3d00a40224d 
```

**Response**:

```
{
  "message": "Favorite product was successfully added.",
  "object": {
    "brand": "inovox",
    "id": "fe0f6c82-35a7-4963-95bb-f3d00a40224d ",
    "image": "http://challenge-api.luizalabs.com/images/fe0f6c82-35a7-4963-95bb-f3d00a40224d .jpg",
    "price": 160.69,
    "title": "Farol Lado Esquerdo para Monza 88/90"
  }
}
```

# Remover produto favorito

``http://127.0.0.1:5000/client/product/remove/``

**Método**: DELETE

**Request**: 
```
client_id = 2
product_id = fe0f6c82-35a7-4963-95bb-f3d00a40224d 
```

**Response**:

```
{
  "message": "Favorite product was successfully removed.",
  "object": {
    "brand": "inovox",
    "id": "fe0f6c82-35a7-4963-95bb-f3d00a40224d ",
    "image": "http://challenge-api.luizalabs.com/images/fe0f6c82-35a7-4963-95bb-f3d00a40224d .jpg",
    "price": 160.69,
    "title": "Farol Lado Esquerdo para Monza 88/90"
  }
}
```

# Exibir produtos favoritos de um cliente

``http://127.0.0.1:5000/client/products/``

**Método**: GET

**Request**: 
```
client_id = 2
```

**Response**:

```
{
  "_id": 3,
  "email": "maria@email.com",
  "name": "Maria",
  "product": [
    {
      "brand": "mondial",
      "id": "571fa8cc-2ee7-5ab4-b388-06d55fd8ab2f",
      "image": "http://challenge-api.luizalabs.com/images/571fa8cc-2ee7-5ab4-b388-06d55fd8ab2f.jpg",
      "price": 159.0,
      "reviewScore": 4.352941,
      "title": "Churrasqueira Elétrica Mondial 1800W"
    },
    {
      "brand": "ruvolo",
      "id": "f6c094e1-f27d-677b-4187-cf6a5acd03aa",
      "image": "http://challenge-api.luizalabs.com/images/f6c094e1-f27d-677b-4187-cf6a5acd03aa.jpg",
      "price": 39.0,
      "title": "Taça para Vinho 1 Peça"
    }
  ]
}
```