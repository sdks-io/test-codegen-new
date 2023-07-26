
# LIS Public Bordero Appointment

The LISBorderoAppointment data contract.

## Structure

`LISPublicBorderoAppointment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object_id` | `uuid\|string` | Optional | - |
| `is_new` | `bool` | Optional | - |
| `original_hash_snapshot` | `string` | Optional | - |
| `original_snapshot` | `object` | Optional | - |
| `current_snapshot` | `object` | Optional | - |
| `meta_info` | [`LISMetaInfoCollection`](../../doc/models/lis-meta-info-collection.md) | Optional | - |

## Example (as JSON)

```json
{
  "objectId": "00000000-0000-0000-0000-000000000000",
  "isNew": false,
  "originalHashSnapshot": "originalHashSnapshot0",
  "originalSnapshot": {
    "key1": "val1",
    "key2": "val2"
  },
  "currentSnapshot": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

