# Special Invoice

```python
special_invoice_controller = client.special_invoice
```

## Class Name

`SpecialInvoiceController`

## Methods

* [Create Accrual Special Invoice](../../doc/controllers/special-invoice.md#create-accrual-special-invoice)
* [Create Special Invoice](../../doc/controllers/special-invoice.md#create-special-invoice)


# Create Accrual Special Invoice

Creates a special invoice for Accruals

```python
def create_accrual_special_invoice(self,
                                  request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`LISCreateSpecialInvoiceRequest`](../../doc/models/lis-create-special-invoice-request.md) | Body, Required | The request |

## Response Type

[`LISResponseLISPublicSpecialInvoice`](../../doc/models/lis-response-lis-public-special-invoice.md)

## Example Usage

```python
request = LISCreateSpecialInvoiceRequest()

result = special_invoice_controller.create_accrual_special_invoice(request)
print(result)
```


# Create Special Invoice

Creates a special invoice

```python
def create_special_invoice(self,
                          request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`LISCreateSpecialInvoiceRequest`](../../doc/models/lis-create-special-invoice-request.md) | Body, Required | The request |

## Response Type

[`LISResponseLISPublicSpecialInvoice`](../../doc/models/lis-response-lis-public-special-invoice.md)

## Example Usage

```python
request = LISCreateSpecialInvoiceRequest()

result = special_invoice_controller.create_special_invoice(request)
print(result)
```

