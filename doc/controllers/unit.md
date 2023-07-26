# Unit

```python
unit_controller = client.unit
```

## Class Name

`UnitController`

## Methods

* [Get Unit](../../doc/controllers/unit.md#get-unit)
* [Get New Unit](../../doc/controllers/unit.md#get-new-unit)
* [Save Unit](../../doc/controllers/unit.md#save-unit)


# Get Unit

Gets the unit

```python
def get_unit(self,
            unit_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit_id` | `string` | Query, Required | - |

## Response Type

[`LISResponseLISPublicUnit`](../../doc/models/lis-response-lis-public-unit.md)

## Example Usage

```python
unit_id = 'UnitId6'

result = unit_controller.get_unit(unit_id)
print(result)
```


# Get New Unit

Create and get a new Unit.

```python
def get_new_unit(self)
```

## Response Type

[`LISResponseLISPublicUnit`](../../doc/models/lis-response-lis-public-unit.md)

## Example Usage

```python
result = unit_controller.get_new_unit()
print(result)
```


# Save Unit

Saves the Unit

```python
def save_unit(self,
             unit)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit` | [`LISPublicUnit`](../../doc/models/lis-public-unit.md) | Body, Required | - |

## Response Type

[`LISResponseLISPublicUnit`](../../doc/models/lis-response-lis-public-unit.md)

## Example Usage

```python
unit = LISPublicUnit()

result = unit_controller.save_unit(unit)
print(result)
```

