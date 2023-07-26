
# LIS Public Query String Property

The QueryString property for query requests

## Structure

`LISPublicQueryStringProperty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `property_name` | `string` | Optional | - |
| `property_value` | `string` | Optional | Gets or sets the key item value from. |
| `operator` | [`OperatorEnum`](../../doc/models/operator-enum.md) | Optional | Gets or sets the key item value from. |

## Example (as JSON)

```json
{
  "propertyName": "propertyName4",
  "propertyValue": "propertyValue4",
  "operator": "IsNotEqualTo"
}
```

