
# LIS Public Order Detail Unit

The LISOrderDetailUnit data contract.

## Structure

`LISPublicOrderDetailUnit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit_type` | [`UnitType1Enum`](../../doc/models/unit-type-1-enum.md) | Optional | Gets or sets UnitType. |
| `unit_id` | `string` | Optional | Gets or sets UnitId. |
| `quantity` | `float` | Optional | Gets or sets Quantity. |
| `created_on` | `datetime` | Optional | Gets or sets CreatedOn. |
| `created_by` | `string` | Optional | Gets or sets CreatedBy. |
| `changed_on` | `datetime` | Optional | Gets or sets ChangedOn. |
| `changed_by` | `string` | Optional | Gets or sets ChangedBy. |

## Example (as JSON)

```json
{
  "unitType": "Pallette",
  "unitId": "unitId8",
  "quantity": 149.16,
  "createdOn": "2016-03-13T12:52:32.123Z",
  "createdBy": "createdBy2"
}
```

