# Print

```python
mprint_controller = client.mprint
```

## Class Name

`PrintController`


# Execute Print Command Server

Sends a print command request.

```python
def execute_print_command_server(self,
                                print_request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `print_request` | [`LISPublicPrintRequest`](../../doc/models/lis-public-print-request.md) | Body, Required | - |

## Response Type

[`LISResponseBoolean`](../../doc/models/lis-response-boolean.md)

## Example Usage

```python
print_request = LISPublicPrintRequest()

result = mprint_controller.execute_print_command_server(print_request)
print(result)
```

