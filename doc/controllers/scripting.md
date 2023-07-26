# Scripting

```python
scripting_controller = client.scripting
```

## Class Name

`ScriptingController`

## Methods

* [Get Script for Execution](../../doc/controllers/scripting.md#get-script-for-execution)
* [Get Script for Execution 1](../../doc/controllers/scripting.md#get-script-for-execution-1)
* [Get Scripts by Request](../../doc/controllers/scripting.md#get-scripts-by-request)
* [Get Script Infos by Request](../../doc/controllers/scripting.md#get-script-infos-by-request)


# Get Script for Execution

Gets the script including sub scripts for the specified event and implementation.

```python
def get_script_for_execution(self,
                            event_type,
                            implementation_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventType2Enum`](../../doc/models/event-type-2-enum.md) | Query, Required | The event type. |
| `implementation_type` | `string` | Query, Required | The implementation type. |

## Response Type

[`LISResponseLISPublicScript`](../../doc/models/lis-response-lis-public-script.md)

## Example Usage

```python
event_type = EventType2Enum.NOTSET

implementation_type = 'implementationType0'

result = scripting_controller.get_script_for_execution(
    event_type,
    implementation_type
)
print(result)
```


# Get Script for Execution 1

Gets the script including sub scripts for the script id.

```python
def get_script_for_execution_1(self,
                              event_type,
                              implementation_type,
                              script_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventType2Enum`](../../doc/models/event-type-2-enum.md) | Query, Required | The event type. |
| `implementation_type` | `string` | Query, Required | The implementation type. |
| `script_id` | `string` | Template, Required | The script id. |

## Response Type

[`LISResponseLISPublicScript`](../../doc/models/lis-response-lis-public-script.md)

## Example Usage

```python
event_type = EventType2Enum.NOTSET

implementation_type = 'implementationType0'

script_id = 'scriptId6'

result = scripting_controller.get_script_for_execution_1(
    event_type,
    implementation_type,
    script_id
)
print(result)
```


# Get Scripts by Request

Gets all scripts that match the specified criteria.

```python
def get_scripts_by_request(self,
                          implementation_type=None,
                          event_type=None,
                          external_key=None,
                          product=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `implementation_type` | `string` | Query, Optional | The implementation type (optional). |
| `event_type` | [`List of EventType2Enum`](../../doc/models/event-type-2-enum.md) | Query, Optional | The event type (optional). |
| `external_key` | `string` | Query, Optional | The external key (optional). |
| `product` | [`Product1Enum`](../../doc/models/product-1-enum.md) | Query, Optional | The product (optional). |

## Response Type

[`LISResponseListLISPublicScript`](../../doc/models/lis-response-list-lis-public-script.md)

## Example Usage

```python
result = scripting_controller.get_scripts_by_request()
print(result)
```


# Get Script Infos by Request

Gets meta information for all scripts that match the specified criteria.

```python
def get_script_infos_by_request(self,
                               implementation_type=None,
                               event_type=None,
                               external_key=None,
                               product=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `implementation_type` | `string` | Query, Optional | The implementation type (optional). |
| `event_type` | [`List of EventType2Enum`](../../doc/models/event-type-2-enum.md) | Query, Optional | The event type (optional). |
| `external_key` | `string` | Query, Optional | The external key (optional). |
| `product` | [`Product1Enum`](../../doc/models/product-1-enum.md) | Query, Optional | The product (optional). |

## Response Type

[`LISResponseListLISPublicScriptInfo`](../../doc/models/lis-response-list-lis-public-script-info.md)

## Example Usage

```python
result = scripting_controller.get_script_infos_by_request()
print(result)
```

