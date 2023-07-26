# Order

```python
order_controller = client.order
```

## Class Name

`OrderController`

## Methods

* [Get Order](../../doc/controllers/order.md#get-order)
* [Save Order](../../doc/controllers/order.md#save-order)
* [Get Order Status History](../../doc/controllers/order.md#get-order-status-history)
* [Get Order Query](../../doc/controllers/order.md#get-order-query)


# Get Order

Gets the order with for the specified id. Only one parameter is required.

## **Priority** | **Parameter name**
:---:|:---:
**1**| OrderId
**2** | OrderNo

```python
def get_order(self,
             order_id,
             order_no)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `int` | Template, Required | The id of the order. |
| `order_no` | `int` | Template, Required | The number of the order. |

## Response Type

[`LISResponseLISPublicOrder`](../../doc/models/lis-response-lis-public-order.md)

## Example Usage

```python
order_id = 12

order_no = 110

result = order_controller.get_order(
    order_id,
    order_no
)
print(result)
```


# Save Order

Saves an order.Changes for the order aggregates won't be carried because they represent just a summary of the order.

```python
def save_order(self,
              public_order,
              skip_relation_refresh=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_order` | [`LISPublicOrder`](../../doc/models/lis-public-order.md) | Body, Required | The Public Order that has to be saved |
| `skip_relation_refresh` | `bool` | Query, Optional | Additional save option for the saving process. |

## Response Type

[`LISResponseLISPublicOrder`](../../doc/models/lis-response-lis-public-order.md)

## Example Usage

```python
public_order = LISPublicOrder()

result = order_controller.save_order(public_order)
print(result)
```


# Get Order Status History

Gets the order status history with the specified order id and one of the optional parameters

## **Priority** | **Parameter name**
:---:|:---:
**1**| OrderId
**2** | OrderNo
**3**| DossierNo
**4** | Tourid

```python
def get_order_status_history(self,
                            order_id,
                            order_no,
                            dossier_no,
                            tour_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `int` | Template, Required | The OrderId for the order status history. |
| `order_no` | `int` | Template, Required | The OrderNo for the order status history. |
| `dossier_no` | `string` | Template, Required | The DossierNo for the order status history. |
| `tour_id` | `int` | Template, Required | The TourId for the order status history. |

## Response Type

[`LISResponseListLISPublicOrderStatusHistory`](../../doc/models/lis-response-list-lis-public-order-status-history.md)

## Example Usage

```python
order_id = 12

order_no = 110

dossier_no = 'DossierNo4'

tour_id = 212

result = order_controller.get_order_status_history(
    order_id,
    order_no,
    dossier_no,
    tour_id
)
print(result)
```


# Get Order Query

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
def get_order_query(self,
                   transport_section_query_search_properties,
                   query_object_maximum=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transport_section_query_search_properties` | `List of object` | Query, Required | The section properties to look for i.e.   {"propertyName": "ShipmentId","propertyValue": "647","operator": "IsGreaterThan"} |
| `query_object_maximum` | `int` | Query, Optional | The QueryObjectMaximum |

## Response Type

[`LISResponseListLISPublicOrderView`](../../doc/models/lis-response-list-lis-public-order-view.md)

## Example Usage

```python
transport_section_query_search_properties = [
    jsonpickle.decode('{"key1":"val1","key2":"val2"}')
]

result = order_controller.get_order_query(transport_section_query_search_properties)
print(result)
```

