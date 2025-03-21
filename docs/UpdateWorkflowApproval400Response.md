# UpdateWorkflowApproval400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_workflow_approval400_response import UpdateWorkflowApproval400Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkflowApproval400Response from a JSON string
update_workflow_approval400_response_instance = UpdateWorkflowApproval400Response.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkflowApproval400Response.to_json())

# convert the object into a dict
update_workflow_approval400_response_dict = update_workflow_approval400_response_instance.to_dict()
# create an instance of UpdateWorkflowApproval400Response from a dict
update_workflow_approval400_response_from_dict = UpdateWorkflowApproval400Response.from_dict(update_workflow_approval400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


