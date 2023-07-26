# Dispo

```python
dispo_controller = client.dispo
```

## Class Name

`DispoController`

## Methods

* [Get Tour](../../doc/controllers/dispo.md#get-tour)
* [Dispatch Tour](../../doc/controllers/dispo.md#dispatch-tour)
* [Set Tour State](../../doc/controllers/dispo.md#set-tour-state)
* [Get Transport Sections](../../doc/controllers/dispo.md#get-transport-sections)
* [Get Query Transport Section](../../doc/controllers/dispo.md#get-query-transport-section)
* [Get Query Tour](../../doc/controllers/dispo.md#get-query-tour)
* [Get Bordero by Id](../../doc/controllers/dispo.md#get-bordero-by-id)


# Get Tour

Get dispo tour. Only one Parameter is required to get the Tour.

## **Priority** | **Parameter name**
:---:|:---:
**1**| TourId
**2** | TourNo

```python
def get_tour(self,
            tour_id,
            tour_no)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tour_id` | `int` | Template, Required | The tour id. |
| `tour_no` | `int` | Template, Required | The tour id. |

## Response Type

[`LISResponseLISPublicTour`](../../doc/models/lis-response-lis-public-tour.md)

## Example Usage

```python
tour_id = 212

tour_no = 112

result = dispo_controller.get_tour(
    tour_id,
    tour_no
)
print(result)
```


# Dispatch Tour

Dispatch tour

```python
def dispatch_tour(self,
                 dispatch_request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dispatch_request` | [`LISPublicDispatchTourRequest`](../../doc/models/lis-public-dispatch-tour-request.md) | Body, Required | The request. |

## Response Type

[`LISResponseBoolean`](../../doc/models/lis-response-boolean.md)

## Example Usage

```python
dispatch_request = LISPublicDispatchTourRequest()

result = dispo_controller.dispatch_tour(dispatch_request)
print(result)
```


# Set Tour State

Set tour state

```python
def set_tour_state(self,
                  state_request)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state_request` | [`LISPublicTourStateRequest`](../../doc/models/lis-public-tour-state-request.md) | Body, Required | The request. |

## Response Type

[`LISResponseBoolean`](../../doc/models/lis-response-boolean.md)

## Example Usage

```python
state_request = LISPublicTourStateRequest()

result = dispo_controller.set_tour_state(state_request)
print(result)
```


# Get Transport Sections

Gets a list of `LISPublicTransportSectionShipment` and `LISPublicTransportSectionBordero` objects that are derived from `LISPublicTransportSectionBase` with one of the following parameters. These classes are described in the list of public services structures on the left side. If multiple parameters are filled, then the prameter priority is as shown below.

## **Priority** | **Parameter name**
:---:|:---:
**1**| TourId
**2** | OrderId
**3** | OrderNo
**4** | SectionIds

```python
def get_transport_sections(self,
                          section_ids,
                          tour_id,
                          order_id,
                          order_no)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `section_ids` | `List of int` | Query, Required | The ids for the coresponding sections |
| `tour_id` | `int` | Template, Required | The mandatory tour id for the sections |
| `order_id` | `int` | Template, Required | The Order id to use for its corresponding section ids. Any id for the corresponding OrderNo can be use. |
| `order_no` | `int` | Template, Required | The Order No to use for its corresponding section ids. Any id for the corresponding OrderNo can be use. |

## Response Type

[`LISResponseListLISPublicTransportSectionBase`](../../doc/models/lis-response-list-lis-public-transport-section-base.md)

## Example Usage

```python
section_ids = [
    203,
    204,
    205
]

tour_id = 212

order_id = 12

order_no = 110

result = dispo_controller.get_transport_sections(
    section_ids,
    tour_id,
    order_id,
    order_no
)
print(result)
```


# Get Query Transport Section

Gets Transport Sections

## **Numeric Value** | **Parameter name** | **Numeric Value** | **Parameter name**
:---:|:---:|:---:|:---:
**1**| IsLessThan | **10** | IsContainedIn
**2** | IsLessThanOrEqualTo | **11** | DoesNotContain
**3** | IsEqualTo | **12** | IsNull
**4** | IsNotEqualTo | **13** | IsNotNull
**5** | IsGreaterThanOrEqualTo | **14** | IsEmpty
**6** | IsGreaterThan | **15** | IsNotEmpty
**7** | StartsWith | **16** | IsNullOrEmpty
**8** | EndsWith | **17** | IsNotNullOrEmpty
**9** | Contains | | |

```python
def get_query_transport_section(self,
                               transport_section_query_search_properties,
                               query_object_maximum=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transport_section_query_search_properties` | `List of object` | Query, Required | The section properties to look for i.e.   {"propertyName": "OrderNo","propertyValue": "648","operator": "IsGreaterThan"} |
| `query_object_maximum` | `int` | Query, Optional | The QueryObjectMaximum |

## Response Type

[`LISResponseListLISPublicTransportSectionTourView`](../../doc/models/lis-response-list-lis-public-transport-section-tour-view.md)

## Example Usage

```python
transport_section_query_search_properties = [
    jsonpickle.decode('{"key1":"val1","key2":"val2"}')
]

result = dispo_controller.get_query_transport_section(transport_section_query_search_properties)
print(result)
```


# Get Query Tour

Gets Tour Query

## **Numeric Value** | **Parameter name** | **Numeric Value** | **Parameter name**
:---:|:---:|:---:|:---:
**1**| IsLessThan | **10** | IsContainedIn
**2** | IsLessThanOrEqualTo | **11** | DoesNotContain
**3** | IsEqualTo | **12** | IsNull
**4** | IsNotEqualTo | **13** | IsNotNull
**5** | IsGreaterThanOrEqualTo | **14** | IsEmpty
**6** | IsGreaterThan | **15** | IsNotEmpty
**7** | StartsWith | **16** | IsNullOrEmpty
**8** | EndsWith | **17** | IsNotNullOrEmpty
**9** | Contains | | |

```python
def get_query_tour(self,
                  transport_section_query_search_properties,
                  query_object_maximum=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transport_section_query_search_properties` | `List of object` | Query, Required | The section properties to look for i.e. {"propertyName": "TourId","propertyValue": "122","operator": "IsGreaterThan"} |
| `query_object_maximum` | `int` | Query, Optional | The QueryObjectMaximum |

## Response Type

[`LISResponseListLISPublicTourView`](../../doc/models/lis-response-list-lis-public-tour-view.md)

## Example Usage

```python
transport_section_query_search_properties = [
    jsonpickle.decode('{"key1":"val1","key2":"val2"}')
]

result = dispo_controller.get_query_tour(transport_section_query_search_properties)
print(result)
```


# Get Bordero by Id

Returns the bordero for the bordero id.

```python
def get_bordero_by_id(self,
                     bordero_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bordero_id` | `int` | Query, Required | - |

## Response Type

[`LISResponseLISPublicBordero`](../../doc/models/lis-response-lis-public-bordero.md)

## Example Usage

```python
bordero_id = 100

result = dispo_controller.get_bordero_by_id(bordero_id)
print(result)
```

