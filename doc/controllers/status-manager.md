# Status Manager

```python
status_manager_controller = client.status_manager
```

## Class Name

`StatusManagerController`

## Methods

* [Create Order Status](../../doc/controllers/status-manager.md#create-order-status)
* [Get Status Order Text List](../../doc/controllers/status-manager.md#get-status-order-text-list)


# Create Order Status

Creates an order status.

```python
def create_order_status(self,
                       request,
                       order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`LISCreateOrderStatusRequest`](../../doc/models/lis-create-order-status-request.md) | Body, Required | The request. |
| `order_id` | `int` | Template, Required | The Id oth the order. |

## Response Type

[`LISResponseListInt32`](../../doc/models/lis-response-list-int-32.md)

## Example Usage

```python
request = LISCreateOrderStatusRequest(
    status_id=38,
    order_id=226
)

order_id = 62

result = status_manager_controller.create_order_status(
    request,
    order_id
)
print(result)
```


# Get Status Order Text List

Gets the StatusOrderTexts with specific language translation.

```python
def get_status_order_text_list(self,
                              language_id,
                              status_id,
                              get_all)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language_id` | `int` | Template, Required | The id for the chosen language |
| `status_id` | `int` | Template, Required | The Id for order status text. Status Id will be ignored when GetAll is set. |
| `get_all` | `bool` | Template, Required | Gets all order status texts. This option shouldn't be used frequently because a full table scan will be executed for the data table. |

## Response Type

[`LISResponseListLISPublicOrderStatusText`](../../doc/models/lis-response-list-lis-public-order-status-text.md)

## Example Usage

```python
language_id = 96

status_id = 44

get_all = False

result = status_manager_controller.get_status_order_text_list(
    language_id,
    status_id,
    get_all
)
print(result)
```

