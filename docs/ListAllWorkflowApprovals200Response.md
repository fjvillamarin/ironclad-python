# ListAllWorkflowApprovals200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**approval_groups** | [**List[ListAllWorkflowApprovals200ResponseApprovalGroupsInner]**](ListAllWorkflowApprovals200ResponseApprovalGroupsInner.md) |  | [optional] 
**roles** | [**List[ListAllWorkflowApprovals200ResponseRolesInner]**](ListAllWorkflowApprovals200ResponseRolesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_approvals200_response import ListAllWorkflowApprovals200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowApprovals200Response from a JSON string
list_all_workflow_approvals200_response_instance = ListAllWorkflowApprovals200Response.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowApprovals200Response.to_json())

# convert the object into a dict
list_all_workflow_approvals200_response_dict = list_all_workflow_approvals200_response_instance.to_dict()
# create an instance of ListAllWorkflowApprovals200Response from a dict
list_all_workflow_approvals200_response_from_dict = ListAllWorkflowApprovals200Response.from_dict(list_all_workflow_approvals200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


