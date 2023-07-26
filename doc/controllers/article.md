# Article

```python
article_controller = client.article
```

## Class Name

`ArticleController`

## Methods

* [Get Article](../../doc/controllers/article.md#get-article)
* [Get New Article](../../doc/controllers/article.md#get-new-article)
* [Save Article](../../doc/controllers/article.md#save-article)


# Get Article

Gets the article via customer number and article nummber

```python
def get_article(self,
               customer_no,
               article_no)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_no` | `int` | Query, Required | - |
| `article_no` | `string` | Query, Required | - |

## Response Type

[`LISResponseLISPublicArticle`](../../doc/models/lis-response-lis-public-article.md)

## Example Usage

```python
customer_no = 238

article_no = 'ArticleNo6'

result = article_controller.get_article(
    customer_no,
    article_no
)
print(result)
```


# Get New Article

Creates a new article that includes ExtendedDataFields///

```python
def get_new_article(self)
```

## Response Type

[`LISResponseLISPublicArticle`](../../doc/models/lis-response-lis-public-article.md)

## Example Usage

```python
result = article_controller.get_new_article()
print(result)
```


# Save Article

```python
def save_article(self,
                article)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `article` | [`LISPublicArticle`](../../doc/models/lis-public-article.md) | Body, Required | - |

## Response Type

[`LISResponseLISPublicArticle`](../../doc/models/lis-response-lis-public-article.md)

## Example Usage

```python
article = LISPublicArticle()

result = article_controller.save_article(article)
print(result)
```

