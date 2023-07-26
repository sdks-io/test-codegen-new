
# LIS Authentication Request

Request object of the authentication.

## Structure

`LISAuthenticationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `int` | Required | The identifier for the company.<br>Example value:1<br>**Constraints**: `>= 1`, `<= 2147483647` |
| `division_id` | `int` | Optional | The identifier for the division.<br>Example value:1 |
| `department_id` | `int` | Optional | The identifier for the department.<br>Example value:0 |

## Example (as JSON)

```json
{
  "companyId": 68,
  "divisionId": 106,
  "departmentId": 116
}
```

