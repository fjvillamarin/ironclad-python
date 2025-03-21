# ListAllWorkflowApprovals200ResponseRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**assignees** | [**List[ListAllWorkflowApprovals200ResponseRolesInnerAssigneesInner]**](ListAllWorkflowApprovals200ResponseRolesInnerAssigneesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_all_workflow_approvals200_response_roles_inner import ListAllWorkflowApprovals200ResponseRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllWorkflowApprovals200ResponseRolesInner from a JSON string
list_all_workflow_approvals200_response_roles_inner_instance = ListAllWorkflowApprovals200ResponseRolesInner.from_json(json)
# print the JSON string representation of the object
print(ListAllWorkflowApprovals200ResponseRolesInner.to_json())

# convert the object into a dict
list_all_workflow_approvals200_response_roles_inner_dict = list_all_workflow_approvals200_response_roles_inner_instance.to_dict()
# create an instance of ListAllWorkflowApprovals200ResponseRolesInner from a dict
list_all_workflow_approvals200_response_roles_inner_from_dict = ListAllWorkflowApprovals200ResponseRolesInner.from_dict(list_all_workflow_approvals200_response_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


