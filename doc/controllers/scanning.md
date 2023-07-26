# Scanning

```python
scanning_controller = client.scanning
```

## Class Name

`ScanningController`


# Move SSCC to HD Place

```python
def move_sscc_to_hd_place(self,
                         scan_request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scan_request` | [`LISPublicScanRequest`](../../doc/models/lis-public-scan-request.md) | Body, Required | - |

## Response Type

[`LISResponseBoolean`](../../doc/models/lis-response-boolean.md)

## Example Usage

```python
scan_request = LISPublicScanRequest()

result = scanning_controller.move_sscc_to_hd_place(scan_request)
print(result)
```

