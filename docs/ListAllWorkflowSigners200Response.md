# ListAllWorkflowSigners200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**signers** | [**List[ListAllWorkflowSigners200ResponseSignersInner]**](ListAllWorkflowSigners200ResponseSignersInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_signers200_response import ListAllWorkflowSigners200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowSigners200Response from a JSON string
list_all_workflow_signers200_response_instance = ListAllWorkflowSigners200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowSigners200Response.to_json())

# convert the object into a dict
list_all_workflow_signers200_response_dict = list_all_workflow_signers200_response_instance.to_dict()
# create an instance of ListAllWorkflowSigners200Response from a dict
list_all_workflow_signers200_response_from_dict = ListAllWorkflowSigners200Response.from_dict(list_all_workflow_signers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


