# UpdateWorkflowApprovalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UpdateWorkflowApprovalRequestUser**](UpdateWorkflowApprovalRequestUser.md) |  | 
**status** | **str** | The new approval status. | 

## Example

```python
from openapi_client.models.update_workflow_approval_request import UpdateWorkflowApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowApprovalRequest from a JSON string
update_workflow_approval_request_instance = UpdateWorkflowApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowApprovalRequest.to_json())

# convert the object into a dict
update_workflow_approval_request_dict = update_workflow_approval_request_instance.to_dict()
# create an instance of UpdateWorkflowApprovalRequest from a dict
update_workflow_approval_request_from_dict = UpdateWorkflowApprovalRequest.from_dict(update_workflow_approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


