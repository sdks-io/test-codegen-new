# Customer

```python
customer_controller = client.customer
```

## Class Name

`CustomerController`

## Methods

* [Get Customer](../../doc/controllers/customer.md#get-customer)
* [Get Customer Query](../../doc/controllers/customer.md#get-customer-query)
* [Save Customer](../../doc/controllers/customer.md#save-customer)


# Get Customer

Gets customer by Id

```python
def get_customer(self,
                customer_id,
                customer_scopes)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Query, Required | The id for the reqested customer |
| `customer_scopes` | [`List of CustomerScopeEnum`](../../doc/models/customer-scope-enum.md) | Query, Required | - |

## Response Type

[`LISResponseLISPublicCustomer`](../../doc/models/lis-response-lis-public-customer.md)

## Example Usage

```python
customer_id = 146

customer_scopes = [
    CustomerScopeEnum.CODEDTEXT
]

result = customer_controller.get_customer(
    customer_id,
    customer_scopes
)
print(result)
```


# Get Customer Query

Gets Transport Sections

## **Numeric Value** | **Parameter name** | **Numeric Value** | **Parameter name**
:---:|:---:|:---:|:---:
**1**| IsLessThan | **10** | IsContainedIn
**2** | IsLessThanOrEqualTo | **11** | DoesNotContain
**3** | IsEqualTo | **12** | IsNull
**4** | IsNotEqualTo | **13** | IsNotNull
**5** | IsGreaterThanOrEqualTo | **14** | IsEmpty
**6** | IsGreaterThan | **15** | IsNotEmpty
**7** | StartsWith | **16** | IsNullOrEmpty
**8** | EndsWith | **17** | IsNotNullOrEmpty
**9** | Contains | | |

```python
def get_customer_query(self,
                      transport_section_query_search_properties,
                      query_object_maximum=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transport_section_query_search_properties` | `List of object` | Query, Required | The section properties to look for i.e.{"propertyName": "CustomerId","propertyValue": "42","operator": "IsGreaterThan"} |
| `query_object_maximum` | `int` | Query, Optional | The QueryObjectMaximum |

## Response Type

[`LISResponseListLISPublicCustomerBaseView`](../../doc/models/lis-response-list-lis-public-customer-base-view.md)

## Example Usage

```python
transport_section_query_search_properties = [
    jsonpickle.decode('{"key1":"val1","key2":"val2"}')
]

result = customer_controller.get_customer_query(transport_section_query_search_properties)
print(result)
```


# Save Customer

Save or Update Customer

```python
def save_customer(self,
                 save_customer_request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `save_customer_request` | [`LISPublicCustomer`](../../doc/models/lis-public-customer.md) | Body, Required | The id for the reqested customer |

## Response Type

[`LISResponseLISPublicCustomer`](../../doc/models/lis-response-lis-public-customer.md)

## Example Usage

```python
save_customer_request = LISPublicCustomer()

result = customer_controller.save_customer(save_customer_request)
print(result)
```

