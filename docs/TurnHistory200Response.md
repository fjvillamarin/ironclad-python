# TurnHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**page_size** | **int** |  | [optional] [default to 20]
**count** | **int** |  | [optional] 
**list** | [**List[TurnHistory200ResponseListInner]**](TurnHistory200ResponseListInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.turn_history200_response import TurnHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TurnHistory200Response from a JSON string
turn_history200_response_instance = TurnHistory200Response.from_json(json)
# print the JSON string representation of the object
print(TurnHistory200Response.to_json())

# convert the object into a dict
turn_history200_response_dict = turn_history200_response_instance.to_dict()
# create an instance of TurnHistory200Response from a dict
turn_history200_response_from_dict = TurnHistory200Response.from_dict(turn_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


