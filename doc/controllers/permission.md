# Permission

```python
permission_controller = client.permission
```

## Class Name

`PermissionController`

## Methods

* [Get Account Programm Permissions](../../doc/controllers/permission.md#get-account-programm-permissions)
* [Get All Account Names](../../doc/controllers/permission.md#get-all-account-names)


# Get Account Programm Permissions

Gets the permissions for the account name.

```python
def get_account_programm_permissions(self,
                                    account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | - |

## Response Type

[`LISResponseListLISPublicPermission`](../../doc/models/lis-response-list-lis-public-permission.md)

## Example Usage

```python
account_name = 'AccountName0'

result = permission_controller.get_account_programm_permissions(account_name)
print(result)
```


# Get All Account Names

Gets all account names.

```python
def get_all_account_names(self)
```

## Response Type

[`LISResponseListLISPublicUser`](../../doc/models/lis-response-list-lis-public-user.md)

## Example Usage

```python
result = permission_controller.get_all_account_names()
print(result)
```

