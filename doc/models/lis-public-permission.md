
# LIS Public Permission

## Structure

`LISPublicPermission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Gets or sets the name of the account. |
| `object_name` | `string` | Optional | Gets or sets the name of the object. |
| `granted_by_name` | `string` | Optional | Gets or sets the name of the granted by. |
| `granted_by_type` | [`GrantedByTypeEnum`](../../doc/models/granted-by-type-enum.md) | Optional | Gets or sets the type of the granted by. |
| `is_default_right` | `bool` | Optional | Gets or sets a value indicating whether this instance is default right. |
| `access_level` | [`AccessLevelEnum`](../../doc/models/access-level-enum.md) | Optional | Gets or sets the access level. |

## Example (as JSON)

```json
{
  "accountName": "accountName4",
  "objectName": "objectName0",
  "grantedByName": "grantedByName4",
  "grantedByType": "User",
  "isDefaultRight": false
}
```

