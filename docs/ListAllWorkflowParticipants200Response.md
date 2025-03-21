# ListAllWorkflowParticipants200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] [default to 0]
**page_size** | **int** |  | [optional] [default to 20]
**count** | **int** |  | [optional] 
**list** | [**List[ListAllWorkflowParticipants200ResponseListInner]**](ListAllWorkflowParticipants200ResponseListInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_participants200_response import ListAllWorkflowParticipants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowParticipants200Response from a JSON string
list_all_workflow_participants200_response_instance = ListAllWorkflowParticipants200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowParticipants200Response.to_json())

# convert the object into a dict
list_all_workflow_participants200_response_dict = list_all_workflow_participants200_response_instance.to_dict()
# create an instance of ListAllWorkflowParticipants200Response from a dict
list_all_workflow_participants200_response_from_dict = ListAllWorkflowParticipants200Response.from_dict(list_all_workflow_participants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


