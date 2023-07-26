# Authentication

```python
authentication_controller = client.authentication
```

## Class Name

`AuthenticationController`


# Authenticate

#### Getting the bearer token via curl command

---


```
curl --location --request POST 'http://api.lis.eu/Auth' \
--header 'Authorization: Basic bXZsb2g6JFdpbjJrOHIy' \
--header 'Content-Type: application/json' \
--data-raw '{
  "companyId": 1,
  "divisionId": 1,
  "departmentId": 0
}'
```

The WinSped user credentials have to be encoded as a** Base64 String** instead of(user:password) its the Base64 string value ** Basic bXZsb2g6JFdpbjJrOHIy ** for test credentials.The request also needs your **company**, ** division** and** department id**.

#### Getting the bearer token via api endpoint:

---


Use the Basic Authentication Endpoint to receive your bearer token.

:information_source: **Note** This endpoint does not require authentication.

```python
def authenticate(self,
                request,
                authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`LISAuthenticationRequest`](../../doc/models/lis-authentication-request.md) | Body, Required | - |
| `authorization` | `string` | Header, Required | - |

## Response Type

[`LISResponseString`](../../doc/models/lis-response-string.md)

## Example Usage

```python
request = LISAuthenticationRequest(
    company_id=220
)

authorization = 'Authorization8'

result = authentication_controller.authenticate(
    request,
    authorization
)
print(result)
```

