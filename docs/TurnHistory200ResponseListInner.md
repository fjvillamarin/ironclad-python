# TurnHistory200ResponseListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turn_party** | **str** |  | [optional] 
**turn_start_time** | **str** |  | [optional] 
**turn_location** | **str** |  | [optional] 
**turn_user_id** | **str** |  | [optional] 
**turn_end_time** | **str** |  | [optional] 
**turn_number** | **int** |  | [optional] 
**turn_user_email** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.turn_history200_response_list_inner import TurnHistory200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of TurnHistory200ResponseListInner from a JSON string
turn_history200_response_list_inner_instance = TurnHistory200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print(TurnHistory200ResponseListInner.to_json())

# convert the object into a dict
turn_history200_response_list_inner_dict = turn_history200_response_list_inner_instance.to_dict()
# create an instance of TurnHistory200ResponseListInner from a dict
turn_history200_response_list_inner_from_dict = TurnHistory200ResponseListInner.from_dict(turn_history200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


