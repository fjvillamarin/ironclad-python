# ListAllWorkflowSigners200ResponseSignersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 
**signature_status** | **str** |  | [optional] 
**delegates** | [**List[ListAllWorkflowSigners200ResponseSignersInnerDelegatesInner]**](ListAllWorkflowSigners200ResponseSignersInnerDelegatesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_signers200_response_signers_inner import ListAllWorkflowSigners200ResponseSignersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowSigners200ResponseSignersInner from a JSON string
list_all_workflow_signers200_response_signers_inner_instance = ListAllWorkflowSigners200ResponseSignersInner.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowSigners200ResponseSignersInner.to_json())

# convert the object into a dict
list_all_workflow_signers200_response_signers_inner_dict = list_all_workflow_signers200_response_signers_inner_instance.to_dict()
# create an instance of ListAllWorkflowSigners200ResponseSignersInner from a dict
list_all_workflow_signers200_response_signers_inner_from_dict = ListAllWorkflowSigners200ResponseSignersInner.from_dict(list_all_workflow_signers200_response_signers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


